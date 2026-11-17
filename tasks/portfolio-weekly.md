# Úloha: Týdenní souhrn portfolia (pondělí, po Market Briefu)

**Cíl:** Jeden dokument, ze kterého Tomáš za 5 minut ví, jak na tom portfolio je, co se
u firem změnilo, jaké jsou signály a co přijde. Výstup: Claude Doc + `briefs/portfolio/YYYY-MM-DD.md`
podle `templates/portfolio-weekly.md`.

## 1. Ceny a ocenění

1. Dohledej aktuální ceny všech instrumentů z `config/portfolio.yaml` a kurzy USD, EUR,
   DKK, ILS a KRW vůči CZK. Ulož je do `state/prices.json`. Cena SMSH v ILS, ne v agorotech.
2. Spusť `python3 tools/portfolio.py --json /tmp/portfolio.json`.
3. Porovnej s minulým týdnem (`state.json → weekly.last_totals`): změna hodnoty po
   vlastnících a největší přírůstky a úbytky podle tickerů.
4. Ulož nové totály a váhy do `state.json → weekly.last_totals`.

## 2. Co se stalo u firem

- Projdi „Deník změn“ v dossierech za posledních 7 dní a alerty v `briefs/alerts/`.
- U firem bez záznamu za týden udělej rychlou kontrolu (Quartr `list_documents`, web,
  pokud jde o tier A s váhou nad 3 %).
- Tier B (watchlist, plánované nákupy): 1–2 věty ke každé firmě s novinkou.

## 3. Signály

Tabulka všech pozic tieru A: Ticker | Váha | Signál | Změna od minula | Důvod (1 věta) |
Co by to zvrátilo. Signály ber z dossierů a přehodnoť jen tam, kde jsou nová data.

## 4. Katalyzátory příští 2–4 týdny

Ze `state/calendar.md` a Quartr `list_events`: datum, firma, událost, co sledovat
a proč na tom záleží.

## 5. Rizika a struktura portfolia

- Koncentrace podle skupin (výstup `tools/portfolio.py`). Upozorni, když jedna skupina
  přesáhne 25 % nebo jedna pozice 15 %.
- Korelace témat: např. obrana (CSG, RHM, TKMS, SMSH, částečně TKA) reaguje na stejné
  zprávy (Ukrajina, rozpočty NATO); fintech (SOFI, NU, INTR, COIN) na sazby a risk appetite;
  biotech (IOVA, AQST, GUTS) na FDA a binární události.
- Odkaz na poslední Market Brief a jeho hlavní dopady na portfolio (1–3 věty).

## 6. Bratrovo portfolio (Michal)

Samostatná krátká sekce: hodnota, změna, jednotlivé akcie s novinkou. ETF jen hodnotou.
Signály se vztahují k jeho menší toleranci k riziku.

## 7. Údržba

- **Fronta deep dive:** co je hotové, co je další na řadě.
- **Chybějící data:** chybějící nákupní ceny (T212), firmy bez Quartr id a podobně. Stručně,
  ať Tomáš ví, co doplnit.
- `weekly.last_run` = teď.
