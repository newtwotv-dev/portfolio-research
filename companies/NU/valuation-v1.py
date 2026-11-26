# NU valuace v1 – 26. 11. 2026
# Horizont ~2 roky (cíl k 11/2028), ocenění na forward 2029E (P/E), kontrola přes P/B vs. ROE.
# Vstupy: Quartr Q3 2026 (vlastní kapitál 14 344,9 mil. USD, zisk po čtvrtletích), 20-F 2025
# (goodwill 409,4 + nehmotná aktiva 601,7 mil. USD, 4 860,6 mil. akcií k 1. 3. 2026),
# StockAnalysis (4,84 mld. akcií, konsenzus adj. EPS 2026 0,93), WallStreetZen (EPS 2027 1,18 / 2028 1,51).
# Všechny výstupy jsou [Odhad], pokud není uvedeno jinak.

price = 12.36            # close 25. 11. 2026 (Yahoo)
shares = 4.84            # mld. akcií (StockAnalysis)
equity_q3 = 14.345       # mld. USD, Q3 2026 (Quartr slide 32)
gw_int = 0.4094 + 0.6017 # goodwill + nehmotná aktiva YE2025 (20-F)
tbv = equity_q3 - gw_int
ni_q = {'Q4 25': 0.8948, 'Q1 26': 0.8714, 'Q2 26': 1.0611, 'Q3 26': 1.0916}
ni_ttm = sum(ni_q.values())
mcap = price * shares

print("=== Snapshot ===")
print(f"Mcap {mcap:.1f} mld. USD | P/E TTM {mcap/ni_ttm:.1f}x (zisk TTM {ni_ttm:.2f}) | "
      f"P/B {mcap/equity_q3:.2f}x | P/TBV {mcap/tbv:.2f}x (TBV ~{tbv:.1f})")
cons = {'2026 adj': 0.93, '2027': 1.18, '2028': 1.51}
for k, v in cons.items():
    print(f"  P/E konsenzus {k}: {price/v:.1f}x")

# ---------- RSI 14 (Wilder) z closů StockAnalysis + 24./25. 11. ----------
closes = [14.73, 14.56, 14.51, 15.09, 15.05, 14.73, 15.16, 12.59, 12.40, 11.97, 12.05, 11.61,
          11.62, 11.61, 11.99, 11.74, 12.03, 12.36, 12.08, 12.32, 11.83, 13.22, 12.68, 12.33,
          12.08, 11.82, 11.27, 11.80, 12.36 / 1.042, 12.36]  # 24. 11. dopočten z +4,2 % 25. 11.
ch = [b - a for a, b in zip(closes[:-1], closes[1:])]
g = [max(c, 0) for c in ch]; l = [max(-c, 0) for c in ch]
ag = sum(g[:14]) / 14; al = sum(l[:14]) / 14
for i in range(14, len(ch)):
    ag = (ag * 13 + g[i]) / 14; al = (al * 13 + l[i]) / 14
print(f"RSI14 (Wilder, 15. 10.–25. 11.): {100 - 100/(1 + ag/al):.1f}")

# ---------- Reverse excess-return (residual income) model ----------
# Hodnota = BV0 + sum((ROE_t - ke) * BV_{t-1} / (1+ke)^t) + TV. ROE fade lineárně z 30 % na ROE_T
# během 10 let, růst knihy fade z 25 % na g_T. Hledá se ROE_T, které ospravedlní dnešní cenu.
def ri_value(roe_T, ke, gT=0.05, roe0=0.30, g0=0.25, n=10, bv0=equity_q3):
    bv = bv0; val = bv0
    for t in range(1, n + 1):
        roe = roe0 + (roe_T - roe0) * (t - 1) / (n - 1)
        gr = g0 + (gT - g0) * (t - 1) / (n - 1)
        val += (roe - ke) * bv / (1 + ke) ** t
        bv *= 1 + gr
    tv = (roe_T - ke) * bv / (ke - gT) / (1 + ke) ** n
    return (val + tv) / shares

def solve_roe(ke, gT=0.05, **kw):
    lo, hi = 0.0, 0.8
    for _ in range(100):
        mid = (lo + hi) / 2
        if ri_value(mid, ke, gT, **kw) > price: hi = mid
        else: lo = mid
    return mid

print("\n=== Reverse excess-return: jaké trvalé ROE (rok 10+) implikuje cena 12,36 ===")
for ke in (0.12, 0.13, 0.14, 0.15):
    print(f"  ke {ke:.0%}: ROE_T {solve_roe(ke):.1%} (růst knihy 25 % → 5 %, ROE z 30 %)")
print("  citlivost: rychlejší zpomalení knihy (18 % → 5 %), ke 13 %: "
      f"ROE_T {solve_roe(0.13, g0=0.18):.1%}")
print(f"  ilustrace: ROE drží 30 % trvale, ke 14 % → hodnota {ri_value(0.30, 0.14):.2f} USD/akcii")
print(f"  ilustrace: ROE padá na 22 % (úroveň Itaú), ke 14 % → hodnota {ri_value(0.22, 0.14):.2f} USD/akcii")

# ---------- Reverse DCF na EPS ----------
eps26 = (sum(list(ni_q.values())[1:]) + 1.05) / 4.85   # 9M 2026 + Q4E 1,05 mld. (Q4 nese slabší BRL: průměr Q3 5,14, v listopadu ~5,5–5,9), IFRS
print(f"\nEPS 2026E (IFRS, 9M + Q4E 1,05 mld.): {eps26:.2f}")
for ke in (0.14, 0.16):
    for pe in (10, 12, 14):
        need = price * (1 + ke) ** 5 / pe
        cagr = (need / eps26) ** (1 / 5) - 1
        print(f"  ke {ke:.0%}, exit P/E {pe}x v 2031: potřebný EPS 2031 {need:.2f} → CAGR {cagr:.1%}")

# ---------- Scénáře ----------
H = 2.0
sh28 = shares * 1.005 ** 3   # mírné ředění ~0,5 %/rok (2024→2026 ~0,4 %/rok)
ni26 = sum(list(ni_q.values())[1:]) + 1.05
sc = {
    # zisk 2027/28/29 (mld. USD), forward P/E na zisk 2029E v 11/2028, výplata (buyback) z zisku
    'bear': dict(p=0.25, ni=(3.8, 4.1, 4.6), pe=8.5, payout=0.0),
    'base': dict(p=0.50, ni=(4.9, 5.9, 7.0), pe=12.0, payout=0.0),
    'bull': dict(p=0.25, ni=(5.4, 6.9, 8.6), pe=15.0, payout=0.0),
}
print(f"\n=== Scénáře (H = {H} r., zisk 2026E {ni26:.2f} mld., akcie 11/2028 {sh28:.2f} mld.) ===")
ws = 0
for k, s in sc.items():
    n27, n28, n29 = s['ni']
    eps29 = n29 / sh28
    tgt = eps29 * s['pe']
    bv26 = equity_q3 + 1.05
    bv27 = bv26 + n27; bv28 = bv27 + n28
    roe28 = n28 / ((bv27 + bv28) / 2); roe29 = n29 / (bv28 + n29 / 2)
    pb = tgt * sh28 / bv28
    cagr = (n29 / ni26) ** (1 / 3) - 1
    ws += s['p'] * tgt
    print(f"{k}: zisk 27/28/29 {n27}/{n28}/{n29} (CAGR 26–29 {cagr:.0%}) | EPS29 {eps29:.2f} × {s['pe']}x "
          f"= {tgt:.2f} USD ({tgt/price-1:+.0%}, p. a. {(tgt/price)**(1/H)-1:+.1%}) | ROE 28 {roe28:.0%}, "
          f"ROE 29 {roe29:.0%}, P/B v cíli {pb:.1f}x (kniha 2028 {bv28:.1f} bez buybacku)")
ret = ws / price - 1
print(f"Vážený cíl {ws:.2f} USD → {ret:+.1%} za {H} r., {(1+ret)**(1/H)-1:+.1%} p. a.")
for H2 in (1.5, 3.0):  # pozn.: stejný cíl rozložený do kratší/delší doby, ne nový scénář
    print(f"  p. a. při H = {H2}: {(1+ret)**(1/H2)-1:+.1%}")

def wtd(pb, pm, pu):
    return pb * sc['bear_t'] + pm * sc['base_t'] + pu * sc['bull_t']
for k in ('bear', 'base', 'bull'):
    s = sc[k]; sc[k + '_t'] = s['ni'][2] / sh28 * s['pe']
for probs in ((0.30, 0.50, 0.20), (0.20, 0.50, 0.30), (0.35, 0.45, 0.20)):
    w = wtd(*probs)
    print(f"  citlivost P {probs}: vážený cíl {w:.2f} USD, {(w/price)**(1/H)-1:+.1%} p. a.")
print(f"Cena pro +50 % k váženému cíli (hranice Buy): {ws/1.5:.2f} USD")
for r in (0.14, 0.16, 0.18):
    print(f"Cena, při které vážený výnos = {r:.0%} p. a.: {ws/(1+r)**H:.2f} USD")

# ---------- Citlivost na BRL ----------
# ~80 % zisku z Brazílie (odhad: 120 z 143 mil. klientů, 38,6 ze 47,5 mld. vkladů) → BRL −10 % ≈ −8 % zisku v USD
for fx in (-0.15, -0.10, +0.05):
    print(f"BRL {fx:+.0%} vůči USD → zisk v USD ≈ {0.8*fx:+.1%} (base cíl ≈ "
          f"{sc['base_t']*(1+0.8*fx):.2f} USD)")
