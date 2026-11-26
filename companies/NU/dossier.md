# Nu Holdings (NU) – dossier

_Poslední aktualizace: 26. 11. 2026 · Tier: A · Skupina: Fintech · Quartr: [Nu (id 11343)](https://web.quartr.com/m/companies/11343) · IR: [ir.nu](https://www.investidores.nu/en/)_
_Poslední deep dive: [v1 – 26. 11. 2026](deep-dive-v1.md) ([Claude Doc](https://claude.ai/artifact/4bd5LE66A6hFaCHC3eRcwU)) · valuace [valuation-v1.py](valuation-v1.py)_

## Signál

**Aktuální:** 🟡 **Sledovat: držet, přikupovat až pod ~11,4 USD.** Deep dive v1: vážený cíl 17,10 USD (+38 % za 2 roky, ~17,6 % p. a.) je v horní části požadovaného výnosu 14–18 % p. a., ale pod hranicí Buy (+50 %). Cena 12,36 USD (25. 11.) už nese škrt odhadů (10,5× konsenzu EPS 2027, P/TBV ~4,5×) a trh počítá s ROE kolem 24–27 %. Rané delikvence na IEP se zlepšují (15–90: 8,2 → 8,0 %), NPL 90+ ale roste (7,3 %) a náklady na úvěr rostou o 73 % r/r. Velikost: Tomáš 5,7 % v rámci 4–6 %, Michal 3,6 % mírně nad rámcem 2–3 %. [Názor] · _od 26. 11. 2026_ · [deep-dive-v1](deep-dive-v1.md)
**Co by ho zvrátilo:** 🟢 / přikoupit: Investor Day (8. 12.) s cílem ROE ≥ 28 % a návratem kapitálu a Q4 (24. 2. 2027) s NPL 15–90 na IEP ≤ 8,0 %, NPL 90+ ≤ 7,5 % a růstem portfolia ≥ 25 % FXN (pravděpodobnosti 20/50/30 → ~21 % p. a.). Nebo cena pod ~11,4 USD při nezměněných fundamentech. 🔴: NPL 90+ > 8 % nebo NPL 15–90 > 5,3 %, rekurentní RA NIM < 11 %, ROE < 26 % ve dvou kvartálech, regulační strop na úroky karet, USD/BRL dlouhodobě nad 6,2, velká akvizice. Definitivně by tezi rozbilo, kdyby náklady na úvěr rostly víc než dvojnásobně proti portfoliu i po zpomalení růstu.

| Datum | Signál | Důvod | Zdroj |
|---|---|---|---|
| 26. 11. 2026 | 🟡 Sledovat (držet, přikupovat pod ~11,4 USD) | Deep dive v1: bear/base/bull 7,96 / 17,10 / 26,26 USD (25/50/25 %), vážený výnos ~17,6 % p. a. vs. požadovaných 14–18 %, pod hranicí Buy. Sklon mírně pozitivní | [deep-dive-v1](deep-dive-v1.md) |
| 19. 11. 2026 | 🟡 Sledovat | Onboarding. Silné Q3 (zisk +31 % r/r FXN, efficiency 19,3 %), ale NPL 90+ 7,3 % a makro Brazílie. Výchozí stav do deep dive | [Quartr Q3 2026](https://web.quartr.com/m/events/695612) |

## Pozice

| Účet | Vlastník | Počet | Prům. cena | Měna | Váha v portfoliu vlastníka |
|---|---|---|---|---|---|
| t212_tomas (Trading 212) | Tomáš | 28,28745092 | 11,35 | USD | **5,7 %** (k 25. 11. 2026, `tools/portfolio.py`) · rámec deep dive 4–6 % |
| t212_michal (Trading 212) | Michal | 2,04878811 | 11,20 | USD | **3,6 %** (k 25. 11. 2026, `tools/portfolio.py`) · rámec deep dive 2–3 % |

Nerealizovaný P&L při 12,36 USD (close 25. 11.): Tomáš +8,9 %, Michal +10,4 % (CZK, `tools/portfolio.py`). Fintech blok u Tomáše (SOFI + NU + INTR) je 20 % portfolia, NU a INTR jsou společně sázka na Brazílii a BRL. [Fakt, výpočet]

## Snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor / subsektor | Diversified Banks (GICS). Digitální banka / fintech platforma v Latinské Americe (Brazílie, Mexiko, Kolumbie) plus Nu U.S. a Nu Global [Fakt] | [Quartr](https://web.quartr.com/m/companies/11343), [Quartr Q3](https://web.quartr.com/m/events/695612) |
| Země HQ, listingy | Provoz hlavně v Brazílii (São Paulo), holding Nu Holdings Ltd. na Kajmanech (ISIN KYG6683N1034). NYSE (NU), BDR v Brazílii (ROXO34) [Fakt] | universe.yaml, [Suno](https://www.suno.com.br/noticias/?p=634854) |
| Market cap / EV | **59,8 mld. USD** při 12,36 USD a 4,84 mld. akcií [Fakt, výpočet] ([StockAnalysis](https://stockanalysis.com/stocks/nu/)). EV u banky nedává smysl | |
| Cena, 52W low–high | **12,36 USD** (close 25. 11. 2026, +4,2 %, Yahoo). 52W 11,20–18,98 USD, close 20. 11. 11,27 USD [Fakt]. RSI 14 ~45 [Odhad, výpočet] | [StockAnalysis](https://stockanalysis.com/stocks/nu/), [historie](https://stockanalysis.com/stocks/nu/history/) |
| Free float / insider ownership | Vélez ~18,6 % akcií, 74,4 % hlasů (třída B 20 hlasů); Junqueira 9,9 % hlasů; free float ~78 %. Controlled company (výjimky NYSE) [Fakt / Odhad] | [Quartr 20-F](https://web.quartr.com/m/sources/s78165777277) |
| Tržby (TTM) | Manažerské hrubé tržby TTM 22,3 mld. USD (Q4 25 až Q3 26), čistý zisk TTM 3,92 mld. USD [Fakt, výpočet]. Pozn.: onboarding uváděl „IFRS TTM 21,87 mld.“, Quartr standardizovaná data ale za Q4 25–Q2 26 obsahují manažerské tržby | [Quartr slide 20](https://web.quartr.com/m/sources/s53721092878), [Q3 release](https://web.quartr.com/m/documents/3696872) |
| Gross / EBIT / FCF / net margin | U banky místo marží: ROE 32 %, efficiency ratio 19,3 %, NIM 22,5 %, risk-adjusted NIM 12,1 % (rekurentně 12,7 %), čistý zisk / manažerské tržby 17,4 % [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s85040634664) |
| Net debt / EBITDA | n/a (banka). Kapitál 9,9 mld. USD (požadavek 4,2, přebytek 2,1, holding 3,6), funding 43,7 mld. USD vs. čisté úvěry 24,7 mld. USD (57 %) [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s64063137101) |
| CEO | David Vélez (zakladatel, CEO, předseda), CFO Rob Livingston od 13. 7. 2026 (ex Visa, Capital One). CTO Eric Young odchází (TIKR 3. 11.) [Fakt] | [Yahoo/GuruFocus](https://finance.yahoo.com/markets/stocks/articles/nu-holdings-shares-down-22-150833630.html), [TIKR](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up) |
| Konsenzus (rating, cílová cena) | Buy, 23 analytiků (14 SB / 5 B / 3 H / 1 S), průměrný cíl 17,63 USD (rozpětí 12–23) k 20. 11. 2026 [Fakt] ([StockAnalysis](https://stockanalysis.com/stocks/nu/forecast/)). P/E TTM 15,3×, na konsenzus EPS 2027 (1,18) 10,5×, P/B 4,2×, P/TBV ~4,5× [Odhad, výpočet; EPS [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nyse/nu/stock-forecast)] | |
| Denní likvidita | v listopadu typicky 38–90 mil. ks denně, 13. 11. 152,6 mil., 26. 10. 339,7 mil. [Fakt], tedy cca 0,5–1,1 mld. USD denně [Odhad]. Vůči velikosti firmy nadprůměrná [Odhad] | [StockAnalysis – historie](https://stockanalysis.com/stocks/nu/history/) |

## Byznys v kostce

Nu je největší digitální banka v Latinské Americe: 142,6 mil. klientů, z toho 120 mil. v Brazílii (65 % dospělé populace), 16,6 mil. v Mexiku a 6,1 mil. v Kolumbii, s aktivitou 83,6 %. [Fakt, [Quartr Q3](https://web.quartr.com/m/events/695612)] Vydělává na úvěrech (kreditní karty, nezajištěné a zajištěné půjčky; portfolio 41,6 mld. USD, +33 % r/r FXN), na poplatcích a na floatu z vkladů (47,5 mld. USD). Hrubý zisk se dělí zhruba 34 % úvěry, 30 % poplatky a 36 % float. [Fakt, tamtéž] Moat stojí na nejnižších nákladech na klienta v regionu (efficiency ratio 19,3 %, cost to serve 1,1 USD měsíčně při ARPAC 17,7 USD), škále dat pro underwriting a levném fundingu (vklady za 87 % mezibankovní sazby). [Fakt/Názor] Nově expanduje mimo LatAm: Nu U.S. (bankovní licence, účty ve všech 50 státech) a Nu Global (multiměnový účet na stablecoinech, 37 zemí). Management drží dopad obou do efficiency ratio do 100 bp ročně v 2026 i 2027. [Fakt, [Quartr Q3](https://web.quartr.com/m/sources/s320475772465768940656)]

## Investiční teze

**Tomášova teze:** (doplnit)

**Teze z deep dive v1 (26. 11. 2026):** Trh oceňuje Nu jako brazilskou banku před úvěrovým cyklem: 10,5× konsenzu EPS 2027, P/TBV ~4,5× (nejníž za 3 roky) a reverse excess-return model implikuje, že ROE zestárne z 30 % na ~24–27 %. Rané delikvence na IEP se přitom zlepšují (růst NPL 90+ je z velké části mix, IEP 61 % portfolia) a ROE stojí hlavně na nákladové výhodě a floatu, ne jen na úvěrech. I opatrný base (zisk ~15–20 % pod konsenzem, blízko Itaú BBA, P/E 12× beze změny) dává ~17–18 % p. a. Variant perception je mírná: normalizované ROE ~25 % (Citi) není absurdní a růst nákladů na úvěr (+73 % r/r proti portfoliu +33 %) je reálné riziko. Na Buy je potřeba cena pod ~11,4 USD nebo důkaz na Investor Day a ve Q4/Q1. [Názor]

**Scénáře** (z [deep dive v1](deep-dive-v1.md), horizont 2 roky, cíl k 11/2028 na forward zisk 2029E):

| Scénář | Pravděpodobnost | Cílová cena | Klíčový předpoklad |
|---|---|---|---|
| Bear | 25 % | **7,96 USD** (−36 %) | Brazilská recese a předlužení, zisk 2027/28/29 3,8 / 4,1 / 4,6 mld. USD, ROE ~18–19 %, USD/BRL 6+, P/E 8,5× (ocenění jako Itaú) |
| Base | 50 % | **17,10 USD** (+38 %) | Zisk 4,9 / 5,9 / 7,0 mld. USD (~15–20 % pod konsenzem), NPL 90+ 7–7,5 %, Mexiko roste, bez buybacku, P/E 12× |
| Bull | 25 % | **26,26 USD** (+112 %) | Měkké přistání, Selic dolů od 2H27, BRL 5,25, návrat kapitálu z Investor Day, zisk 5,4 / 6,9 / 8,6 mld. USD, P/E 15× |

Vážený cíl **17,10 USD → ~17,6 % p. a.** vs. požadovaný výnos **14–18 % p. a.** Buy (+50 %) pod ~11,4 USD. [Odhad, `valuation-v1.py`]

**Potvrdí:** Investor Day s cílem ROE ≥ 28 % a rámcem návratu kapitálu, Q4 s NPL 15–90 na IEP ≤ 8,0 % a NPL 90+ ≤ 7,5 % při růstu portfolia ≥ 25 % FXN, ROE ≥ 27 % i v sezónně slabém Q1 2027, efficiency pod 20 % i v 2027, Mexiko viditelně ziskové, USD/BRL k 5,25 a začátek snižování Selic. · **Vyvrátí:** NPL 90+ > 8 % nebo NPL 15–90 > 5,3 %, rekurentní RA NIM < 11 %, ROE < 26 % ve dvou kvartálech, růst úvěrů pod ~20 %, stropy BCB na úroky karet, dopad Nu U.S. nad 100 bp efficiency, velká akvizice, USD/BRL dlouhodobě nad 6,2. [Názor]

## KPI ke sledování

| KPI | Poslední hodnota | Předchozí | Trend | Zdroj |
|---|---|---|---|---|
| Klienti / aktivita | 142,6 mil. (+3,7 mil. q/q), aktivita 83,6 % (Brazílie 86,3 %) | 7. kvartál růstu aktivity v Brazílii | ↑ [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s333843379185350436264) |
| ARPAC / cost to serve (měsíční) | 17,7 USD (+21 % r/r FXN) / 1,1 USD (+10 %) | 13,8 / 0,9 USD (Q3 25) | ↑ [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s85040634664) |
| Úvěrové portfolio | 41,6 mld. USD (+33 % r/r, +6 % q/q FXN), karty 65 % | – | ↑ [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s363043016162357380160) |
| Náklady na úvěr vs. portfolio | náklady na úvěr 1,79 mld. USD (+73 % r/r v USD) vs. portfolio +33 % FXN; IFRS ~16 % portfolia anualizovaně | ~12,9 % (Q3 25) | ↑ (horší) [Fakt / výpočet] | [Quartr P&L](https://web.quartr.com/m/sources/s49694977009) |
| NIM / risk-adjusted NIM | 22,5 % / 12,1 % (rekurentně 12,7 %) | RA NIM 12,4 % (Q2), rekurentně 11,9 %; 10,8 % (Q3 25) | → [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s341835218117467205805) |
| NPL 15–90 / NPL 90+ (portfolio) | 4,86 % / 7,3 %, krytí 90+ 234 % | NPL 90+ 6,9 % (Q2), obojí +0,6 pb r/r | ↑ (horší) [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s333986209578134247816) |
| NPL 15–90 / 90+ (na IEP) | 8,0 % / 12,1 %, IEP 61 % portfolia | 8,2 % / 11,6 % (Q2), IEP 59 % | 15–90 ↓ (lepší), 90+ ↑ [Fakt] | [Quartr release](https://web.quartr.com/m/sources/s44417884325) |
| ROE / efficiency ratio | 32 % / 19,3 % | ROE 33 % (Q2), 31 % (Q3 25). Efficiency 20,3 % (Q3 25) | ROE → , efficiency ↓ (lepší) [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s50729500569) |
| Cena vkladů | 87 % mezibankovní sazby | 88 % (Q2), 89 % (Q3 25) | ↓ (lepší) [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s303136289867126839765) |
| Kapitál | 9,9 mld. USD (přebytek 2,1 + holding 3,6) | – | → [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s64063137101) |
| Makro: USD/BRL, Selic | BRL ~5,6–5,9 (listopad), Selic ~13,75 % | Q3 průměr 5,14 | BRL ↓ (horší) [Fakt] | `research/themes.md` #em-fx, #latam |

## Poslední výsledky

**Q3 2026 (zveřejněno 12. 11. 2026 po zavření):** manažerské tržby rekordních 6,26 mld. USD (+37 % r/r FXN), IFRS tržby 5,82 mld. USD, čistý zisk 1,09 mld. USD (+31 % r/r FXN), ROE 32 %. [Fakt, [Quartr Q3](https://web.quartr.com/m/events/695612)] Proti konsenzu: EPS 0,22 USD vs. odhad 0,23 a tržby 5,82 vs. 5,91 mld. USD, tedy mírně pod [Fakt, [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-nu-holdings-misses-q3-2026-estimates-stock-rises-93CH-5023700)], podle Bloombergu ale zisk v souladu s odhady [Fakt, [NeoFeed](https://neofeed.com.br/negocios/nubank-lucra-us-11-bilhao-ve-roe-recuar-e-se-prepara-para-cenario-mais-dificil-em-2027/)]. Trh ocenil zlepšení guidance efektivity a 13. 11. akcie vzrostla o 11,75 % na 13,22 USD. [Fakt, [StockAnalysis](https://stockanalysis.com/stocks/nu/history/)] Přechodné: jednorázový náklad 63 bp v RA NIM kvůli pohledávkám od platebních institucí v mimosoudní likvidaci (~53 mil. USD čistého zisku). Bez něj RA NIM vzrostl na 12,7 %. [Fakt, [Quartr](https://web.quartr.com/m/sources/s196195452895135801587), [call](https://web.quartr.com/m/sources/s60719956775760815323824)] Strukturální: náklady na riziko rostou (credit cost 1,79 mld. USD, cca +73 % r/r) a NPL 90+ stoupá. Management to vysvětluje vědomým rozšířením rizika a vyšším podílem úročených zůstatků (61 % vs. 59 %). Na IEP se rané delikvence zlepšily (8,2 → 8,0 %). [Fakt, [NeoFeed](https://neofeed.com.br/negocios/nubank-lucra-us-11-bilhao-ve-roe-recuar-e-se-prepara-para-cenario-mais-dificil-em-2027/), [Quartr](https://web.quartr.com/m/sources/s44417884325)]

## Guidance a management

- FY 2026 efficiency ratio **19–19,5 % (dřív ~20 %)**. Q4 náklady sezónně vyšší (odložené výdaje a nábor). [Fakt, [Quartr](https://web.quartr.com/m/sources/s335482071934274693927)]
- Nu U.S. a Nu Global dohromady max. 100 bp dopad na efficiency ratio v 2026 i 2027. [Fakt, [Quartr](https://web.quartr.com/m/sources/s320475772465768940656)]
- Na 2027 žádný výhled růstu úvěrů, management ale nevidí důvod k prudkému zpomalení. Efektivní daňová sazba 2027 v pásmu „low-to-mid 20 %“. RA NIM má v Q4 zůstat silný, Q1 má sezónně vyšší cost of risk. [Fakt, [Quartr](https://web.quartr.com/m/sources/s234153363746762918999)]
- Tón: CFO připustil, že udržet tempo růstu úvěrů v Brazílii bude při velikosti Nu náročné. V modelech podle něj počítají s recesí „od zítřka“. [Fakt, [NeoFeed](https://neofeed.com.br/negocios/nubank-lucra-us-11-bilhao-ve-roe-recuar-e-se-prepara-para-cenario-mais-dificil-em-2027/)] Akvizice jen s extrémně vysokou laťkou, priorita je organický růst. [Fakt, [Quartr](https://web.quartr.com/m/sources/s288787207006442592415)]
- Prostor pro kapitálovou optionalitu (9,9 mld. USD kapitálu, z toho přebytek 2,1 + 3,6 na holdingu, tj. ~6 % market capu). Dividendy ani buyback zatím nikdy. Dlouhodobé cíle a alokaci kapitálu má přinést první Investor Day 8. 12. [Fakt/Názor]

## Katalyzátory

| Datum | Událost | Proč na tom záleží |
|---|---|---|
| 8. 12. 2026 | [Investor Day 2026](https://web.quartr.com/m/events/744463) (první v historii) | Cíl ROE (≥ 28 % = pozitivní), rámec návratu kapitálu (buyback/dividenda), cíle pro Mexiko a Nu U.S. Varování: vize bez čísel, signál velkého M&A |
| prosinec 2026 – 1Q27 | COPOM (datum nenalezeno), rozpočet 2027, ministr financí, pravidla BCB proti předlužení | Selic 12,5 % (GS) vs. 13,75 % (MS) vs. trh 15 % (ING); USD/BRL nad 6,0 = riziko |
| 24. 2. 2027 (po zavření US trhu) | [Výsledky Q4 2026](https://web.quartr.com/m/events/800028) | Plnění guidance efektivity, NPL 15–90 na IEP ≤ 8,0 % a 90+ ≤ 7,5 %, růst ≥ 25 % FXN, výhled 2027; translační dopad slabšího BRL |
| ~5/2027 | Výsledky Q1 2027 | Sezónně nejvyšší cost of risk, test ROE ≥ 27 % |
| průběžně 2027 | Mexiko: bankovní licence (payroll účty, vyšší pojištění vkladů), Digital Economy Law (schválen 20. 10.); Kolumbie: změna výpočtu úrokového stropu | Druhý růstový motor mimo Brazílii |
| 2H27 | Selic a BRL | SG čeká snižování od 3Q27, MS až v 2028; GS/SG/MS USD/BRL 5,25 koncem 2027 |

## Rizika

1. **Kvalita aktiv:** NPL 90+ 7,3 % a rostoucí, credit cost +73 % r/r vs. portfolio +33 %. Rozšiřování rizika v nezajištěných půjčkách v zadlužené Brazílii, rekordní originace v září. [Fakt/Názor]
2. **Makro a politika Brazílie:** Lulovo znovuzvolení (26. 10. close −17 %, nejhorší den v historii akcie; EWZ −21 %), Selic 12,5–15 % podle domu a trhu, HDP 2027 0,6–1,2 %, možná US cla. [Fakt, [StockAnalysis](https://stockanalysis.com/stocks/nu/history/), [Stocktwits](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy), `research/themes.md` #latam]
3. **Regulace:** opatření BCB k odpovědnému úvěrování, úrokové stropy (Kolumbie: usury cap), zákaz sázek v Brazílii (zatím bez dopadu). [Fakt, [Quartr Q3](https://web.quartr.com/m/events/695612)]
4. **Alokace kapitálu a expanze mimo LatAm:** hromadění kapitálu ředí ROE, Nu U.S. a Nu Global zatím bez prokázané unit economics, otevřená možnost M&A. [Názor]
5. **Měna:** výnosy v BRL/MXN/COP, akcie v USD, Tomáš a Michal v CZK, tedy dvojí kurzové riziko. BRL −10 % ≈ −8 % zisku v USD. [Fakt / Odhad]
6. **Crowding a management:** HF drží ~10 % kapitalizace (GS 20. 11.), nový CFO a odchod CTO v jednom roce, controlled company. [Fakt]

## Broker views a zmínky

| Datum | Instituce | Co říká | Odkaz do logu |
|---|---|---|---|
| 20. 11. 2026 | konsenzus | Buy, 23 analytiků (14 SB / 5 B / 3 H / 1 S), průměrný cíl 17,63 USD (z 18,77 v polovině října ⬇️) | web: [StockAnalysis](https://stockanalysis.com/stocks/nu/forecast/), [Investing](https://uk.investing.com/equities/nu-holdings-consensus-estimates) |
| 20. 11. 2026 | GS (HFTM) | Na VIP listu nejoblíbenějších longů HF (47 fondů, 21× v top 10); HF drží 10 % kapitalizace (crowding), YTD −29 %. Relativní propad VIP koše je podobný jako u dna trhu v 12/2008 a 5/2022 | log 2026-11 · GS 20. 11. (HFTM) |
| 18. 11. 2026 | Tracker | Q3 2026: tržby 6,26 mld. USD, zisk 1,09 mld., ROE 32 %, guidance efektivity 19–19,5 %, NPL 90+ 7,3 %. 13. 11. +11,75 %. Investor Day 8. 12. | briefs/alerts/2026-11-18.md |
| 18. 11. 2026 | Gavekal | Makro kontext: slabší USD vůči EUR mění CZK přepočet US pozic včetně NU | log 2026-11 · Gavekal 18. 11. |
| 16. 11. 2026 | SG | Makro kontext: BRL mírně konstruktivní (USD/BRL 5,25 koncem 2027), Selic 13,75 % a snižování od 3Q27 na 12,75 %, politické riziko Lula 4.0 | log 2026-11 · SG 16. 11. |
| 15. 11. 2026 | MS | LatAm tým: Brazílie EW → UW (globální PDF ještě EW), Mexiko EW | log 2026-11 · MS 15. 11. |
| 15. 11. 2026 | GS | Ropa: okrajově BRL (Brazílie jako zdroj nabídky ropy) | log 2026-11 · GS 15. 11. |
| 13. 11. 2026 | GS | EM Kickstart: Brazílie OW → MW (HDP 2027 0,6 %, Selic 12,5 % koncem 2027), Mexiko ↑ OW, EM banky OW | log 2026-11 · GS 13. 11. |
| 13. 11. 2026 | GS | FX Outlook: BRL 5,25, carry, ale nižší ropa a fiskální riziko | log 2026-11 · GS 13. 11. |
| 11. 11. 2026 | UBP | EM lokální měny OW, Lulovo znovuzvolení zasáhlo EM fondy | log 2026-11 · UBP 11. 11. |
| 10. 11. 2026 | GS | Top of Mind: 4. Lulovo období jen s mírnou fiskální konsolidací | log 2026-11 · GS 10. 11. |
| 3. 11. 2026 | TIKR (konsenzus) | průměrný cíl 18,80 USD, P/TBV 4,6× vs. 3letý průměr 8,3×, odchází CTO | web: [TIKR](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up) |
| 29. 10. 2026 | Itaú BBA | Hold, cíl 18 → 15 USD; růst portfolia 2027 37 → 26 %, zisk 19 % / 22 % pod konsenzem 2027/28 | web: [Seu Dinheiro](https://www.seudinheiro.com/2026/empresas/e-agora-nubank-itau-bba-corta-preco-alvo-e-alerta-o-pior-ainda-pode-estar-por-vir-miql/) |
| 26. 10. 2026 | Monness | iniciace Buy, cíl 20 USD | web: [Stocktwits](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy), [StockAlarm](https://pro.stockalarm.io/quote/NU/analysts) |
| 20. 10. 2026 | UBS | Buy, cíl 18,20 → 20,50 USD | web: [StockAlarm](https://pro.stockalarm.io/quote/NU/analysts) |
| 1. 10. 2026 | GS (Labarta) | Hold, 23 USD (neobvyklá kombinace, možná chyba zdroje) | web: [StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/) |
| 16. 9. 2026 | Itaú BBA | Downgrade na Hold, cíl 20 → 18 USD (výhled Brazílie) | web: [Investing.com](https://uk.investing.com/equities/nu-holdings) |
| 15. 6. 2026 | Citi | Buy → Neutral, 18 → 13 USD; dlouhodobé ROE 30 → 25 %, zisk 2027 4,4 mld. USD | web: [NeoFeed](https://neofeed.com.br/negocios/apos-bofa-citi-rebaixa-nubank-por-risco-na-carteira-de-credito/en/) |
| 2. 6. 2026 | BofA | Neutral → Underperform, 16 → 10 USD (férový násobek 13× forward) | web: [Nasdaq/Fool](https://www.nasdaq.com/articles/it-too-soon-call-bottom-nu-holdings-stock) |

**Rozpor:** GS (13. 11.) i MS LatAm (15. 11.) snižují Brazílii (MW, resp. UW), SG (16. 11.) je k BRL mírně konstruktivní a UBP (11. 11.) drží EM lokální měny OW. Pro NU je to smíšené: GS zároveň zvedá Mexiko na OW a drží EM banky OW, což podporuje mexickou část teze. Selic: GS 12,5 % vs. SG 12,75 % vs. MS 13,75 % vs. trh 15 % (ING). Mezi analytiky Nu: Itaú BBA a Citi vidí zisk výrazně pod konsenzem, většina (19 z 23) drží Buy. Deep dive v1 je v base blízko skeptiků. [Fakt / Názor]

## Deník změn

| Datum | Změna | Zdroj |
|---|---|---|
| 19. 11. 2026 | Onboarding (rychlý dossier) | Tracker |
| 19. 11. 2026 | Novinky od 18. 11.: bez nových firemních zpráv. Cena 12,08 USD (−2,03 %, 18. 11.), od skoku 13. 11. zpět o cca 9 % | [Stock Events](https://stockevents.app/th/stock/NU) |
| 26. 11. 2026 | **Deep dive v1.** Signál 🟡 Sledovat potvrzen (držet, přikupovat pod ~11,4 USD). Scénáře 7,96 / 17,10 / 26,26 USD (25/50/25 %), vážený ~17,6 % p. a. vs. požadovaných 14–18 %. Rámec pozice Tomáš 4–6 % (dnes 5,7 %), Michal 2–3 % (3,6 %). Nové KPI: NPL na IEP, náklady na úvěr vs. portfolio, kapitál, USD/BRL. Doplněna vlastnická struktura (Vélez 74,4 % hlasů), výměna CFO/CTO, sell-side (Itaú BBA, Citi, BofA, Monness), doplněn close dne voleb 26. 10. (−17 %; onboarding uváděl −12 % přes noc) a upřesněny TTM tržby (manažerské 22,3 mld.) | [deep-dive-v1](deep-dive-v1.md) |

## Zdroje

- Quartr: [firma](https://web.quartr.com/m/companies/11343) · [Q3 2026 event](https://web.quartr.com/m/events/695612) · [earnings release](https://web.quartr.com/m/documents/3696872) · [slides](https://web.quartr.com/m/documents/4257984) · [transcript](https://web.quartr.com/m/documents/4595512) · [20-F 2025](https://web.quartr.com/m/documents/3232655) · [Investor Day 8. 12.](https://web.quartr.com/m/events/744463) · [Q4 2026 (24. 2. 2027)](https://web.quartr.com/m/events/800028)
- Deep dive: [deep-dive-v1.md](deep-dive-v1.md) (kompletní seznam zdrojů v kroku 14) · [valuation-v1.py](valuation-v1.py)
- Research log: research/log/2026-11.md (GS 10., 13., 15. a 20. 11., UBP 11. 11., MS 15. a 20. 11., SG 16. a 23. 11., ING 12. 11., BCA 11. a 18. 11., Gavekal 6. a 18. 11.), briefs/alerts/2026-11-18.md
- Web: [StockAnalysis (cena, konsenzus)](https://stockanalysis.com/stocks/nu/) · [StockAnalysis – forecast](https://stockanalysis.com/stocks/nu/forecast/) · [StockAnalysis – ratingy](https://stockanalysis.com/stocks/nu/ratings/) · [StockAnalysis – historie](https://stockanalysis.com/stocks/nu/history/) · [WallStreetZen (EPS 2027/28)](https://www.wallstreetzen.com/stocks/us/nyse/nu/stock-forecast) · [TIKR 3. 11.](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up) · [Seu Dinheiro – Itaú BBA](https://www.seudinheiro.com/2026/empresas/e-agora-nubank-itau-bba-corta-preco-alvo-e-alerta-o-pior-ainda-pode-estar-por-vir-miql/) · [NeoFeed – Citi/BofA](https://neofeed.com.br/negocios/apos-bofa-citi-rebaixa-nubank-por-risco-na-carteira-de-credito/en/) · [Nasdaq/Fool – BofA](https://www.nasdaq.com/articles/it-too-soon-call-bottom-nu-holdings-stock) · [Stocktwits 26. 10.](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy) · [Yahoo/GuruFocus – CFO](https://finance.yahoo.com/markets/stocks/articles/nu-holdings-shares-down-22-150833630.html) · [NeoFeed 12. 11.](https://neofeed.com.br/negocios/nubank-lucra-us-11-bilhao-ve-roe-recuar-e-se-prepara-para-cenario-mais-dificil-em-2027/) · [Investing.com – Q3 vs. odhady](https://www.investing.com/news/transcripts/earnings-call-transcript-nu-holdings-misses-q3-2026-estimates-stock-rises-93CH-5023700) · [Investing.com – Itaú BBA](https://uk.investing.com/equities/nu-holdings) · [StockAlarm – analytici](https://pro.stockalarm.io/quote/NU/analysts) · [Stocktwits 25. 10. (volby)](https://stocktwits.com/news-articles/markets/equity/why-is-nu-stock-plunging-nearly-12-overnight/cZUdkmJRBUr) · [Suno (BDR ROXO34)](https://www.suno.com.br/noticias/?p=634854) · [Stock Events](https://stockevents.app/th/stock/NU) · [TIKR 13. 11.](https://www.tikr.com/es/blog/nu-holdings-soars-11-on-record-1-1-billion-profit-as-it-takes-first-steps-beyond-latin-america)
