# Portfolio Research

Automatizovaný research nad Tomášovým portfoliem. Do repa není potřeba sahat, všechno
řídí Claude. Tenhle soubor je jen orientace.

## Jak to funguje

```
Gmail (broker reporty) ──► Research Inbox ──► research/ (log, house views, témata)
                                                   │
Quartr (výsledky, calls) ──► Portfolio Tracker ◄───┤──► companies/<TICKER>/dossier.md
                                   │               │
                                   ▼               ▼
                             alerty (při      Market Brief (po)
                             události)        Týdenní souhrn (po)
```

- **Denně ráno**: zpracují se nové reporty a zkontrolují se firmy. Dokument přijde jen
  při podstatné události (výsledky, změna signálu, velký pohyb, FDA, M&A…).
- **V pondělí ráno**: Market Brief a týdenní souhrn portfolia.
- **Průběžně**: jeden deep dive denně podle fronty (`state/state.json`), dokud nejsou
  pokryté všechny firmy.
- Watchlist na Quartru se kontroluje při každém běhu a nové firmy se zakládají samy.

## Povely

Otevři novou session v Claude Code s tímhle repem (nebo pokračuj v libovolném běhu)
a napiš třeba:

- `pošli mi brief` / `brief za poslední 3 dny`
- `co je nového u Micronu`
- `analyzuj TNE Korea`
- `koupil jsem 10 SOFI za 15 USD na T212`
- `stav portfolia`
- `co říkají banky o AI capexu`
- `přesuň brief na pátek`

Úplný seznam je v `tasks/on-demand.md`.

## Struktura

Viz tabulka „Mapa repa“ v `CLAUDE.md`.
