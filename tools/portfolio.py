#!/usr/bin/env python3
"""Ocenění portfolia v CZK.

Čte config/portfolio.yaml, config/universe.yaml a state/prices.json
a vypíše markdown tabulky: hodnota po účtech a vlastnících, váhy,
nerealizovaný P&L tam, kde je známá nákupní cena, a expozici podle sektorů.

Použití:
    python3 tools/portfolio.py                # markdown na stdout
    python3 tools/portfolio.py --json out.json  # navíc strojově čitelný výstup

Formát state/prices.json:
{
  "as_of": "2026-11-23",
  "fx_to_czk": {"USD": 21.0, "EUR": 24.3, "DKK": 3.25, "ILS": 5.9, "KRW": 0.015},
  "prices": {"SOFI": 14.83, "SMSH": 16.04, ...}   # v hlavní měně instrumentu (ILS, ne agoroty)
}
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Chybí PyYAML: pip install pyyaml --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
SUBUNITS = {"ILA": ("ILS", 100), "GBX": ("GBP", 100)}  # cenová jednotka -> (měna, dělitel)


def load():
    portfolio = yaml.safe_load((ROOT / "config/portfolio.yaml").read_text())
    universe = yaml.safe_load((ROOT / "config/universe.yaml").read_text())["instruments"]
    prices = json.loads((ROOT / "state/prices.json").read_text())
    return portfolio, universe, prices


def czk(v):
    return f"{v:,.0f}".replace(",", " ")


def to_main_unit(value, unit):
    if unit in SUBUNITS:
        return value / SUBUNITS[unit][1]
    return value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="uložit výsledek i jako JSON")
    args = ap.parse_args()

    portfolio, universe, prices = load()
    fx = prices["fx_to_czk"]
    px = prices["prices"]
    owners = portfolio["owners"]

    rows, missing = [], set()
    for acc in portfolio["accounts"]:
        for pos in acc["positions"]:
            t = pos["ticker"]
            meta = universe.get(t, {})
            ccy = meta.get("ccy")
            if t not in px or ccy not in fx:
                missing.add(t if t not in px else f"FX {ccy}")
                continue
            price = px[t]
            value_czk = pos["qty"] * price * fx[ccy]
            avg = pos.get("avg_price")
            pnl_pct = None
            if avg:
                avg_main = to_main_unit(avg, pos.get("price_unit") or meta.get("price_unit"))
                pnl_pct = (price / avg_main - 1) * 100
            rows.append({
                "owner": acc["owner"], "account": acc["id"], "ticker": t,
                "name": meta.get("name", t), "sector": meta.get("group") or meta.get("sector", "?"),
                "qty": pos["qty"], "price": price, "ccy": ccy,
                "value_czk": value_czk, "pnl_pct": pnl_pct,
            })
        for ccy, amt in (acc.get("cash") or {}).items():
            if ccy in fx:
                rows.append({"owner": acc["owner"], "account": acc["id"], "ticker": f"CASH_{ccy}",
                             "name": f"Hotovost {ccy}", "sector": "Hotovost", "qty": amt, "price": 1,
                             "ccy": ccy, "value_czk": amt * fx[ccy], "pnl_pct": None})

    out = [f"_Ocenění k {prices.get('as_of', '?')}, kurzy: " +
           ", ".join(f"{k}/CZK {v}" for k, v in fx.items()) + "_\n"]

    for owner_id, owner in owners.items():
        orows = [r for r in rows if r["owner"] == owner_id]
        if not orows:
            continue
        total = sum(r["value_czk"] for r in orows)
        out.append(f"\n### {owner['name']} – celkem {czk(total)} CZK\n")

        # agregace po tickeru napříč účty
        agg = defaultdict(lambda: {"value_czk": 0.0, "accounts": [], "pnl": []})
        for r in orows:
            a = agg[r["ticker"]]
            a["value_czk"] += r["value_czk"]
            a["accounts"].append(r["account"])
            a.update(name=r["name"], price=r["price"], ccy=r["ccy"], sector=r["sector"])
            if r["pnl_pct"] is not None:
                a["pnl"].append(f"{r['account']}: {r['pnl_pct']:+.1f} %")
        out.append("| Ticker | Název | Cena | Hodnota CZK | Váha | Účty | Nerealiz. P&L |")
        out.append("|---|---|---|---:|---:|---|---|")
        for t, a in sorted(agg.items(), key=lambda kv: -kv[1]["value_czk"]):
            out.append(f"| {t} | {a['name']} | {a['price']:.2f} {a['ccy']} | "
                       f"{czk(a['value_czk'])} | {a['value_czk'] / total * 100:.1f} % | "
                       f"{', '.join(sorted(set(a['accounts'])))} | {'; '.join(a['pnl']) or '–'} |")

        sect = defaultdict(float)
        for r in orows:
            sect[r["sector"]] += r["value_czk"]
        out.append("\n**Expozice podle sektorů:** " + ", ".join(
            f"{s} {v / total * 100:.0f} %" for s, v in sorted(sect.items(), key=lambda kv: -kv[1])))

        accs = defaultdict(float)
        for r in orows:
            accs[r["account"]] += r["value_czk"]
        out.append("\n**Po účtech:** " + ", ".join(
            f"{a} {czk(v)} CZK" for a, v in sorted(accs.items(), key=lambda kv: -kv[1])))

    if missing:
        out.append(f"\n⚠️ Chybí cena nebo kurz pro: {', '.join(sorted(missing))}")

    print("\n".join(out))
    if args.json:
        Path(args.json).write_text(json.dumps({"rows": rows, "missing": sorted(missing)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
