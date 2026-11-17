# Úloha: Market Brief (týdenní, pondělí)

**Cíl:** Ucelený přehled toho, co se dělo na trzích, co je nového, co to může přinést
a co nás čeká. Na konci propojení s portfoliem. Výstup: Claude Doc + `briefs/market/YYYY-MM-DD.md`
podle `templates/market-brief.md`.

**Období:** od posledního briefu (`state.json → market_brief.last_period_end`) do teď.
Při prvním běhu posledních 7 dní. Na povel z chatu může být období jiné, třeba „za poslední
3 dny“.

Předpoklad: Research Inbox proběhl dnes. Pokud ne, spusť ho nejdřív.

## 1. Podklady

1. **Research log** za období: `research/log/` (všechny záznamy), `research/house-views.md`
   (sekce Log změn za období) a `research/themes.md` (🔥 témata a nové poznámky).
2. **Předchozí brief** (`briefs/market/` nejnovější): co jsme minule čekali, co se
   naplnilo a co ne. Navazuj na něj, neopakuj ho.
3. **Tržní data z webu** (s odkazy na zdroj), stav k poslední zavírací ceně a změna za období:
   - Indexy: S&P 500, Nasdaq 100, Russell 2000, STOXX 600, DAX, CAC 40; stručně Hang Seng
     nebo Hang Seng Tech, TA-35, KOSPI nebo KOSDAQ.
   - Nejlepší a nejhorší sektory US i EU, výrazné rotace (value/growth, small/large).
   - VIX.
   - Okrajově: US 2Y a 10Y výnos, EUR/USD, USD/CZK, EUR/CZK, Brent, zemní plyn TTF, zlato,
     měď, BTC.
4. **Kalendář na další týden** (web): Fed/ECB (zasedání, projevy), CPI/PCE, NFP, PMI,
   ISM, aukce Treasuries, opční expirace, geopolitické termíny. Plus earnings a události
   firem z portfolia ze `state/calendar.md`.

## 2. Analýza

- Z reportů vytáhni **3–6 hlavních témat** období. Ke každému: co se děje, co na to říkají
  instituce (jmenovitě), kde se shodují a kde rozcházejí, a co to může přinést (scénáře,
  rizika). Tagy [Fakt] / [Odhad] / [Názor].
- **Změny doporučení** za období (z house-views) jako přehledná tabulka.
- **Co jsme čekali vs. co se stalo** (z předchozího briefu), stručně a poctivě.
- **Výhled:** co nás čeká a na co se dívat. U každé události uveď, proč je důležitá
  a co by znamenalo překvapení oběma směry.

## 3. Dopad na portfolio

Pro každé hlavní téma najdi firmy, kterých se týká: podle pole `themes` v `universe.yaml`
a podle aktuálního stavu v dossierech (`companies/*/dossier.md`).

- Tabulka: Téma → dotčené pozice → směr dopadu (+/−/?) → komentář.
- Pokud z makra plyne signál pro konkrétní pozici, uveď ho podle pravidel v `CLAUDE.md`
  a zapiš ho do dossieru.
- Upozorni na koncentrace, které téma zvýrazňuje (např. obrana 25 %+ portfolia při
  zprávách o příměří, fintech při pohybu sazeb).

## 4. Výstup a stav

- Dokument podle `templates/market-brief.md`, česky. Délka zhruba 2–4 strany: hutně,
  bez vaty.
- Nové poznatky o tématech zapiš zpět do `research/themes.md` (sekce „Výhled“ u tématu).
- Události z kalendáře přidej do `state/calendar.md`.
- `market_brief.last_run` = teď, `market_brief.last_period_end` = konec období.
