# Deep dive: SoFi Technologies (SOFI) – 18. 11. 2026

_Claude Doc: https://claude.ai/artifact/CiXe7b25dgUESk5MQPzM3J · Verze v1 (první deep dive, předchozí verze neexistuje). Cena pro výpočty 14,28 USD (close 17. 11. 2026, [Motley Fool](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/)); kotaci za 18. 11. se nepodařilo ověřit. Výpočty: Python skript ve scratchpadu běhu (sofi_valuation.py), váhy: `tools/portfolio.py` k 17. 11. 2026._

## Verdikt

**Signál: ⚡ Ke zvážení: redukovat (velikost pozice u Tomáše). Teze sama zůstává 🟡 Sledovat.** [Názor]

- **Důvod:** Pravděpodobnostně vážený výnos vychází na **+26 % za 2 roky (~12 % p. a.)**, tedy pod požadovaným výnosem **14–17 % p. a.** (30–37 % za 2 roky). Rozptyl scénářů je velmi široký (bear −42 %, bull +102 %). SOFI je přitom u Tomáše **největší pozice (14,3 %)**, zhruba dvojnásobek rámce 5–8 %, který odpovídá nízké až střední conviction. Provozně firma jede výborně. Problém je v tom, že zisk a book value na 2027 stojí na nezajištěných osobních úvěrech, které SoFi rekordně nabírá do rozvahy (+18 % q/q), a to v době, kdy Fed zvedá sazby a ocenění úvěrů dělá management přes fair value s tenkou rizikovou přirážkou. [Názor]
- **Scénáře (horizont ~2 roky, cíl k 11/2028):** Bear 30 % → **8,25 USD** · Base 45 % → **18,50 USD** · Bull 25 % → **28,90 USD** · vážená cena **18,02 USD**. [Odhad, výpočet v Pythonu]
- **Buy podle definice (+50 až +100 % za 1–3 roky) to není.** Vážený výnos by na úroveň požadovaného výnosu vyšel zhruba při ceně **13,2–13,9 USD** a na +50 % za 2 roky (~25 % p. a.) až kolem **11,5 USD**. [Odhad]
- **Michal (5,4 %):** pozice je mírně převážená vůči rámci 2–3 % pro jeho konzervativní ETF portfolio. Nepřikupovat, při odrazu zvážit snížení k ~3 %. [Názor]
- **Co by signál zvrátilo:** 🟢 / přikoupit: Q4 výsledky (29. 1. 2027) potvrdí cíle 2027 (EPS 0,90), předpoklad defaultů osobních úvěrů ve fair value modelu zůstane ≤5,1 %, all-in NCO ≤3,5 % a total capital ratio se stabilizuje nad ~14 % bez emise. Pak bych posunul pravděpodobnosti na 20/50/30 a vážený výnos vyjde ~17 % p. a. Druhá cesta je cena pod ~13 USD při nezměněných fundamentech. 🔴 Teze oslabena: předpoklad defaultů >5,5 % nebo all-in NCO >4 %, marky osobních úvěrů pod ~101 % par, škrt guidance, nová emise akcií nebo propad objemů LPB.

## Snapshot a kontext (kroky 0–1)

### Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor / subsektor | Consumer finance: digitální banka (national bank charter), úvěry, vklady, investice, B2B tech platforma (Galileo/Technisys) | [Quartr](https://web.quartr.com/m/companies/5065) |
| HQ, listing, ticker | San Francisco, USA · NASDAQ · SOFI | [10-Q Q3 2026](https://web.quartr.com/m/documents/3912143) |
| Cena | 14,28 USD (close 17. 11. 2026, −3,84 % za den) [Fakt] | [Motley Fool, 17. 11.](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/) |
| 52W low–high | 13,86–31,75 USD (StockAnalysis), resp. 13,86–30,42 USD (Fool; rozdíl je nejspíš intraday vs. close) [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/sofi/) |
| Market cap | 18,5 mld. USD = 14,28 × 1 296,6 mil. akcií (basic) [Fakt, výpočet]. Fool uvádí 19,3 mld. | [10-Q Q3](https://web.quartr.com/m/documents/3912143) |
| EV, net debt / EBITDA | U banky nedává smysl. Místo toho: CET1 16,9 %, total capital 17,0 % [Fakt] | [Quartr Q3](https://web.quartr.com/m/sources/s75086464345) |
| Tržby (TTM, GAAP) | 4,73 mld. USD (Q4 25–Q3 26) [Fakt, součet] | [Quartr financials](https://web.quartr.com/m/documents/3912143) |
| Marže | Adj. EBITDA 34 % (Q3) · GAAP čistá marže 17,4 % (Q3) · Hrubá marže a FCF u banky s úvěry držením k prodeji nedávají smysl (provozní CF 9M26 −9,2 mld. kvůli originacím HFS) [Fakt] | [Quartr Q3](https://web.quartr.com/m/events/718307), [CF 10-Q](https://web.quartr.com/m/documents/3912143) |
| Valuace | P/TBV 1,91× (TBVPS 7,48) · P/E 23,4× FY26 / 15,9× FY27 adj. EPS z guidance · forward P/E 18,1× (konsenzus NTM) [Fakt/výpočet] | [Quartr Q3](https://web.quartr.com/m/sources/s55434191519), [Fool](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/) |
| Free float / insideři | Free float ~99 % [Odhad]. CEO Noto drží ~11,96 mil. akcií (~0,9 %) | [TS2, 6/2026](https://ts2.tech/en/sofi-technologies-stock-nasdaqsofi-falls-as-insider-buying-meets-a-funding-cost-test/) |
| Short interest | 223,7 mil. akcií (~17,2 % akcií v oběhu), days to cover 3,7, k 30. 10. 2026. Za rok téměř dvojnásobek (118 mil. v 11/2025) [Fakt] | [Equibles](https://equibles.com/stocks/sofi/shortinterest) |
| CEO | Anthony Noto (od 2018) | [Quartr transcript Q3](https://web.quartr.com/m/sources/s66919776431428811924423) |
| IR | [investors.sofi.com](https://investors.sofi.com) | |
| Konsenzus | Hold (25 analytiků), průměrný cíl 20,84 USD, rozpětí ~12–30 USD [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/sofi/), [Beinsure, 28. 10.](https://beinsure.com/news/sofi-stock-price-forecast-wall-street-analysts-target-15-30/) |
| Denní likvidita | 38–78 mil. akcií/den v listopadu (~0,6–1,2 mld. USD), beta 2,24 → **nadprůměrná** likvidita [Fakt] | [StockAnalysis historie](https://stockanalysis.com/stocks/sofi/history/) |
| RSI 14 | 39,4 (Wilder, z closů 12. 10.–17. 11.) → slabé, ale ne přeprodané [Fakt, výpočet] | StockAnalysis historie + Fool, vlastní výpočet |

### Krok 1 – zdroj a kontext idey

- **Zdroj:** stávající pozice. Tomáš drží SOFI na dvou účtech (ibkr 12 ks za 18,71 USD, t212 52,9 ks za 9,59 USD, vážená nákupka 11,28 USD), Michal 2,8 ks za 17,05 USD (`config/portfolio.yaml`). Dossier vznikl při onboardingu 18. 11. 2026.
- **Proč je cena tam, kde je (−46 % YTD, ~−55 % z maxima):** [Fakt, zdroje u bodů]
  - březen 2026: short report Muddy Waters zpochybnil fair value účetnictví a výši odpisů ([Motley Fool, 24. 3.](https://www.fool.com/investing/2026/03/24/sofi-the-short-thesis/)),
  - Q1 a Q2: zklamání ze zisku vůči růstu tržeb. Guidance EPS se v červenci nezvedla kvůli vyšší dani a reinvesticím a Fed místo škrtů zvedá sazby ([TIKR, 3. 10.](https://www.tikr.com/blog/sofi-stock-is-down-43-in-2026-should-you-buy-the-dip-before-november), [Nasdaq/Fool, 16. 6.](https://www.nasdaq.com/articles/heres-whats-behind-sofis-big-decline-and-what-you-should-do-about-it)),
  - po Q3 (27. 10.) akcie vyskočila na 17,61 USD a do 17. 11. všechno vrátila, aniž by přišla firemní zpráva ([StockAnalysis historie](https://stockanalysis.com/stocks/sofi/history/)). Do toho padá makro: GS čeká hike v prosinci i v březnu (research/log, GS 13. a 16. 11.), Upstart 10. 11. snížil výhled kvůli makru a rostoucím defaultům ([TIKR, 11. 11.](https://www.tikr.com/blog/upstart-just-hit-a-new-52-week-low-after-falling-14-in-a-month-is-the-selling-overdone)) a fintech jako celek klesá (17. 11. Chime −3,85 %, [StockAnalysis](https://stockanalysis.com/stocks/CHYM)).
- **Trh firmy a výhled:** SoFi cílí na refinancování ~1,2 bil. USD dluhu z kreditních karet a ~400 mld. USD studentských úvěrů ([Quartr](https://web.quartr.com/m/sources/s72569206939)). Do 2030 chce 100 mil. produktů (dnes 26,7 mil.) a pět byznysů nad 1 mld. USD tržeb ([Quartr](https://web.quartr.com/m/sources/s84514821304681835707754)). Krátkodobě rozhodují sazby a spotřebitelský úvěrový cyklus: MS čeká zpomalení US spotřeby ze 3,8 % na 1,6 % ve 4Q (research/log, MS 15. 11.), GS čeká škrty Fedu až koncem 2027 (research/themes.md #fed). [Fakt/Názor]

## Teze a variant perception (krok 2)

**Teze v jedné větě:** SoFi je skutečně rostoucí franšíza. Akcie ale není tak levná, jak vypadá na P/E z guidance, a zároveň není tak rozbitá, jak tvrdí short-selleři. Výnos nad požadovanou laťku vyžaduje, aby ROTCE přešlo z ~10 % k 18–20 %, a to se v cyklu rostoucích sazeb musí teprve prokázat. [Názor]

- **Co si myslí trh:** Sell-side je rozdělený zhruba na třetiny (Citi 30 / Needham 24 USD Buy vs. MS 15 / KBW 16 / BofA 16,50 USD Underweight/Underperform, [Beinsure, 28. 10.](https://beinsure.com/news/sofi-stock-price-forecast-wall-street-analysts-target-15-30/)). Cena 14,28 je pod cíli medvědů, takže trh teď dává váhu bear táboru: úvěrovému riziku a kvalitě zisku. Forward P/E 18,1× při 14,28 USD implikuje NTM EPS ~0,79 USD, tedy pod guidance 0,90 na 2027. Trh managementu cíl na 2027 zatím nevěří. [Odhad, výpočet z [Fool](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/)]
- **Co si myslím já a proč je trh vedle:**
  1. **P/E je špatná kotva, správná je P/TBV vs. ROTCE.** Při 1,91× TBV trh už dnes počítá s udržitelným ROTCE **~15,5–17,5 %** (při ke 11–12 %, g 6 %), přičemž dnešní ROTCE je 9,9 % a z guidance na 2027 vychází ~12 %. „Levných 16× zisku 2027“ tak už v ceně má solidní exekuci. [Odhad, výpočet]
  2. **Fraud tail je menší, než naznačuje Muddy Waters.** Hotovostní tržby za Q3 byly 1,386 mld. USD, z toho 927 mil. hotovostní NII ([Quartr](https://web.quartr.com/m/sources/s42972698590)). Vklady jsou 90 % fundingu, CET1 16,9 %, CEO po short reportu nakupoval. Tvrzení MW o EBITDA o ~90 % nižší se s hotovostním NII těžko slučuje. [Názor]
  3. **Trh naopak podceňuje citlivost book value na úvěr a sazby.** Nesplacená jistina osobních úvěrů vzrostla za jediné čtvrtletí o 18 % na 30,9 mld. USD ([Quartr](https://web.quartr.com/m/sources/s69558816355)). Předpoklad defaultů ve fair value modelu roste (4,5 % 12/2025 → 4,77 % 6/2026 → **5,10 %** 9/2026) a diskontní přirážka nad benchmarkem se přitom **zúžila z 0,98 na 0,81 p. b.** ([10-Q](https://web.quartr.com/m/sources/s45899898916), [Q2 10-Q](https://web.quartr.com/m/sources/s68011501205)). Marky drží nad par (103,3 %) i díky tenčí přirážce. [Fakt/Názor]
- **Síla edge:** slabá až střední. Nemám informační výhodu v datech o úvěrech, jde o jinou interpretaci veřejných čísel. Variant perception existuje, ale vede k opatrnějšímu závěru, než je retailový konsenzus „buy the dip“, a zhruba v souladu se sell-side Hold. [Názor]

## Byznys model a KPI (krok 3)

### Co firma dělá a jak vydělává

- **Lending** (adj. tržby 807 mil. USD v Q3, +68 %, contribution margin 56 %): osobní, studentské (refinancování), hypoteční úvěry a nově SMB. Úvěry drží ve fair value a část prodává přes **Loan Platform Business (LPB)**, kde originuje pro třetí strany za poplatek (153 mil. USD v Q3, originace 3,8 mld.). [Fakt, [Quartr](https://web.quartr.com/m/sources/s61518397830), [LPB](https://web.quartr.com/m/sources/s79126704812)]
- **Financial Services** (525 mil. USD, +25 %): SoFi Money (vklady), Invest, kreditní karta, SoFi Plus (předplatné 10 USD/měsíc), krypto, stablecoin SoFiUSD. Zdroj levného fundingu a cross-sellu. [Fakt, [Quartr](https://web.quartr.com/m/sources/s50605395797)]
- **Technology Platform** (87 mil. USD, −24 % r/r, bez odchozího klienta +18 %): Galileo/Technisys, B2B processing a core banking. Contribution margin spadla z 28 % na 16 %. [Fakt, [Quartr](https://web.quartr.com/m/sources/s61518397830)]
- **Reporting:** tři segmenty, k tomu adjusted metriky (adj. net revenue bez přecenění servicing rights a reziduí, adj. EBITDA, adj. EPS). V Q3 se GAAP a adj. čistý zisk skoro kryjí (241 vs. 243 mil. USD). [Fakt, [Quartr](https://web.quartr.com/m/sources/s81489799796)]

### Moat

- **Pro:** levný a rostoucí vkladový funding (51,3 mld. USD, +5,8 mld. q/q) díky bankovní licenci, cross-sell (1,56 produktu na člena, 51 % nových produktů od stávajících členů), značka u mladších dobře vydělávajících klientů a vlastní technologický stack. [Fakt, [Quartr](https://web.quartr.com/m/sources/s70157095697)]
- **Proti:** produkty jsou z velké části komoditní (osobní úvěr, spořicí účet). Management sám říká, že sazba na vkladech nahrazuje náklady na pobočky a že brokered vklady jsou levnější než SoFi Money ([Quartr](https://web.quartr.com/m/sources/s86916025812579268515842)). Moat tedy stojí na lifetime value a cross-sellu, ne na nákladech fundingu. Licence a vkladový funding už nejsou unikátní. [Názor]

### Sektorové KPI (banka / spotřebitelský věřitel)

| KPI | Hodnota Q3 2026 | Komentář | Zdroj |
|---|---|---|---|
| NIM | 6,14 % (+16 bp q/q), mgmt čeká >5 % i dál | vysoké díky unsecured mixu | [Quartr](https://web.quartr.com/m/sources/s51302740678426719011779) |
| CET1 / total capital | 16,9 % / 17,0 % (total capital −180 bp q/q, cíl „low to mid-teens“) | kapitál se rychle spotřebovává | [Quartr](https://web.quartr.com/m/sources/s69005017082604098814350) |
| ROTCE | 9,9 % | cíl 20–30 % dlouhodobě | [Quartr](https://web.quartr.com/m/sources/s89778137908938805470571) |
| Osobní úvěry: all-in NCO / vykázané NCO / 90D delikvence | ~3,4 % / 2,26 % / 42 bp | vykázané NCO snižují prodeje delikventních úvěrů | [Quartr](https://web.quartr.com/m/sources/s56977026663) |
| FV model osobních úvěrů | kupon 12,78 %, default 5,10 %, CPR 25,9 %, diskont 5,56 % vs. benchmark (2Y SOFR) 4,75 % | default ↑, přirážka ↓ | [10-Q](https://web.quartr.com/m/sources/s45899898916), [ER](https://web.quartr.com/m/sources/s56977026663) |
| Marky úvěrů | osobní 103,3 % (−140 bp q/q), studentské 101,9 %, hypotéky 101,5 % | kumulativní FV úpravy 1,40 mld. = 14 % TBV, −628 mil. q/q | [Quartr](https://web.quartr.com/m/sources/s82335047779879622606148), [ER](https://web.quartr.com/m/sources/s69558816355) |
| Vintage ztráty | kohorty 4Q22–4Q25: kumulativní ztráty 4,71 % při 33 % zbývající jistiny vs. 6,62 % u vintage 2017. Tolerance 7–8 % | zatím lepší než minulý cyklus | [ER](https://web.quartr.com/m/sources/s56977026663) |
| Fee-based revenue | 571 mil. USD, 42 % adj. tržeb (cíl 50 %+) | origination fees ~270 mil. USD, 2,5× r/r | [Quartr](https://web.quartr.com/m/sources/s80690534719), [transcript](https://web.quartr.com/m/sources/s61451095838205498229654) |
| Členové / produkty | 17,1 mil. (+35 %) / 26,7 mil. (+44 %) | rekordní přírůstky | [Quartr](https://web.quartr.com/m/sources/s70157095697) |

### Produkt a recenze

- Trustpilot: 4,4/5 z 14 588 recenzí (80 % pětihvězdičkových, 11 % jednohvězdičkových). Chválí se rychlé schválení a výplata úvěru a přehledná aplikace. Stížnosti míří na nečekané poplatky, pomalé řešení fraudu a zamítnutí automatem bez možnosti mluvit s člověkem. [Fakt, [Trustpilot](https://uk.trustpilot.com/review/sofi.com?page=2), vzorek recenzí]
- Financer (10/2026): osobní úvěry 75/100, plus za soft-pull a výplatu ještě týž den, minus za minimální skóre 680 a nekonzistentní zákaznický servis. [Fakt, [Financer](https://financer.com/review/sofi/)]
- Souvislost [Názor]: stížnosti na poplatky sedí s tím, že přes 50 % nových osobních úvěrů už má origination fee ([transcript](https://web.quartr.com/m/sources/s61451095838205498229654)). Pro výnos je to dobré, pro značku riziko. Růst SoFi Plus v Q3 brzdil podvodný nábor, který se musel opravit ([transcript](https://web.quartr.com/m/sources/s65914472109718374718206)).

## Finance, alokace kapitálu, rozvaha a governance (kroky 4–7)

### Krok 4 – finance

| Rok | Tržby GAAP (mld. USD) | Růst | Zisk před zdaněním (mil. USD) | Čistý zisk (mil. USD) | Zdroj |
|---|---|---|---|---|---|
| 2021 | 0,98 | +74 % | −481 | −484 | [Quartr](https://web.quartr.com/m/documents/217893) |
| 2022 | 1,57 | +60 % | −319 | −320 | [Quartr](https://web.quartr.com/m/documents/217892) |
| 2023 | 2,12 | +35 % | −301 | −301 | [Quartr](https://web.quartr.com/m/documents/329305) |
| 2024 | 2,67 | +26 % | 233 | 499 (vč. daňového benefitu) | [Quartr](https://web.quartr.com/m/documents/1851132) |
| 2025 | 3,61 | +35 % | 526 | 481 | [Quartr 10-K](https://web.quartr.com/m/documents/2857886) |
| 9M 2026 | 3,70 | +43 % | 722 | 564 | [Quartr Q3](https://web.quartr.com/m/documents/3912143) |

- **Kvalita zisku:** [Fakt/Názor]
  - Rok 2024 je čistý zisk nafouknutý rozpuštěním daňové rezervy. V Q1 a Q2 2026 pomáhaly daňové benefity, v Q3 už daň 24 % ([Quartr](https://web.quartr.com/m/documents/3912143)). Pro 2027 guidance počítá s 24% daní ([Quartr](https://web.quartr.com/m/sources/s254211451375264743355)).
  - V Q3 vznikly ztráty z fair value přes 800 mil. USD, které ze ~734 mil. USD kompenzovaly zisky ze zajištění. Zbytek dopadu jde z jiných vstupů, které hedge nekryje ([transcript](https://web.quartr.com/m/sources/s66770362676634268395847)); 10-Q uvádí zisky ze swapů 684 mil. ([Quartr](https://web.quartr.com/m/sources/s50428276000)). Zajištění funguje na sazby, ne na úvěrové spready a defaulty.
  - Silnou stránkou je **hotovostní NII 927 mil. USD za čtvrtletí** ([Quartr](https://web.quartr.com/m/sources/s42972698590)). Slabou stránkou je, že část růstu tržeb tvoří origination fees (270 mil. USD), které se účtují okamžitě, zatímco úvěrové riziko běží po celou dobu úvěru. [Názor]
- **FCF:** nedá se smysluplně měřit, protože originace úvěrů držených k prodeji jdou přes provozní CF (9M26 −9,2 mld. USD, [Quartr](https://web.quartr.com/m/documents/3912143)). Lepší proxy je organický růst TBV: TBV +2,5 mld. r/r, z toho ~1,5 mld. z emise v 12/2025, organicky tedy ~1,0 mld. [Odhad, výpočet]
- **Přechodné vs. strukturální:** strukturální jsou růst členů a produktů, rostoucí podíl poplatků a vklady. Přechodné (nebo cyklické) jsou nízké NCO, rekordní originace osobních úvěrů (CFO sám čeká, že v 2027 se růst přesune k hypotékám a refinancování studentských úvěrů, [transcript](https://web.quartr.com/m/sources/s71852562926873467709287)) a zisky ze zajištění. [Názor]
- **Guidance:** FY26 adj. EPS 0,61, FY27 0,90 (tržby 6,4 mld., +27 %, čistá marže ~20 %, předpoklad dvou hiků) ([Quartr](https://web.quartr.com/m/sources/s58385744882730146331364)). Segmenty 2027: Lending +25 %, Tech +25 %, FS +35 %. Rozdíl ~300 mil. USD proti součtu segmentů jde podle CFO na „corporate line“ ([transcript](https://web.quartr.com/m/sources/s85271785697729253457880), [corporate](https://web.quartr.com/m/sources/s51989833958322778530149)). [Fakt]

### Krok 5 – alokace kapitálu

- **Dividendy a buybacky:** žádné. Veškerý kapitál jde do růstu rozvahy. [Fakt, [CF](https://web.quartr.com/m/documents/2857886)]
- **Emise:** v prosinci 2025 veřejná emise za 1,5 mld. USD (54,5 mil. akcií, ~27,5 USD/akcie) ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/1818874/000181887425000225/sofi-20251204.htm), [Investing.com](https://ng.investing.com/analysis/sofi-slides-as-545mshare-offering-tests-valuation-after-a-strong-2025-rally-212490)). Počet akcií 1Q25 1 104 mil. → 3Q26 1 297 mil. (**+17 % za 18 měsíců**) ([Quartr](https://web.quartr.com/m/documents/3912143)). Emise nad TBV zvedá TBVPS, takže část +25% růstu TBVPS je emisní efekt. [Fakt/Odhad]
- **SBC:** 262 mil. USD (2025), 220 mil. USD za 9M26 ([Quartr](https://web.quartr.com/m/documents/3912143)), tedy trvalé ředění ~1–2 % ročně. [Fakt/Odhad]
- **M&A:** Peach Finance a Composer v Q2 2026 za 70,1 mil. USD hotově, goodwill 31,7 mil. ([Quartr](https://web.quartr.com/m/sources/s62555810050)). Tržby akvizic nejsou zveřejněné, takže implikovaný násobek (se synergiemi ani bez nich) spočítat nejde. Starší velké akvizice (Galileo, Technisys) stojí za většinou goodwillu 1,43 mld. USD. Tech Platform, kam patří, dnes meziročně klesá a contribution margin má 16 %, takže návratnost těchto akvizic je zatím slabá. [Fakt: goodwill [Quartr](https://web.quartr.com/m/documents/3912143); hodnocení Názor]
- **Splatnost konvertibilek 2026** (428 mil. USD) byla 15. 10. vypořádána hotově, bez ředění ([Quartr](https://web.quartr.com/m/sources/s62951447826)). [Fakt]

### Krok 6 – rozvaha

- Aktiva 67,8 mld. USD, vlastní kapitál 11,3 mld., TBV 9,7 mld. ([Quartr](https://web.quartr.com/m/documents/3912143)). Vklady 51,3 mld. (90 % fundingu). [Fakt]
- Dluh 3,9 mld. USD (+2,0 mld. q/q, hlavně warehouse; kapacita warehouse 7,2 mld., čerpáno 2,1 mld.) ([Quartr](https://web.quartr.com/m/sources/s51946050923)). Konvertibilky 862,5 mil. USD s kupónem 1,25 % splatné v březnu 2029 ([Quartr](https://web.quartr.com/m/sources/s47001208588)), další facilita 486 mil. se splatností 2028 ([Quartr](https://web.quartr.com/m/sources/s70162041051)). Likvidita 15,9 mld. ([Quartr](https://web.quartr.com/m/sources/s62036147584)). AFS cenné papíry nesou nerealizovanou ztrátu 168 mil. USD, z 99 % jde o Treasuries a agency MBS. [Fakt]
- **Kapitál je klíčové omezení.** CFO uvádí 9,6 mld. USD kapitálu, RWA 56 mld. a při cílovém poměru 13,5 % volnou kapacitu ~15 mld. RWA. Dalších ~14 mld. přinesou zisky a SBC do konce 2027 ([transcript](https://web.quartr.com/m/sources/s65333407541804400762656), [2](https://web.quartr.com/m/sources/s57532818116959372263475)). Total capital ratio ale v Q3 klesl o 180 bp, což odpovídá přírůstku RWA ~5 mld. za čtvrtletí. **Při tomto tempu vystačí 29 mld. kapacity zhruba na 6 čtvrtletí, tedy do ~1Q28.** Pak musí SoFi zpomalit růst rozvahy (víc LPB, méně NII), nebo znovu shánět kapitál. [Odhad, výpočet]
- **Citlivost TBV:** kdyby se osobní úvěry přecenily na par, TBV klesne o ~0,78 mld. (−8 %, TBVPS 6,88). Při přecenění všech úvěrů na par o ~1,06 mld. (−11 %). +100 bp diskontní sazby u osobních úvěrů znamená ~−0,34 USD na akcii TBV. [Odhad, výpočet: daň 24 %, duration 1,8 roku]
- Net debt / EBITDA: u banky nerelevantní.

### Krok 7 – vlastnictví a governance

- **Free float** ~99 %, bez kontrolujícího akcionáře a bez dual-class struktury [Odhad]. Short interest 17 % akcií ([Equibles](https://equibles.com/stocks/sofi/shortinterest)).
- **Insideři:** [Fakt]
  - CEO Noto po short reportu v březnu nakoupil zhruba za 0,5 mil. USD ([Motley Fool](https://www.fool.com/investing/2026/03/24/sofi-the-short-thesis/)) a v létě přidal ~130 tis. akcií za ~17,29 USD ([TS2](https://ts2.tech/en/sofi-technologies-stock-nasdaqsofi-falls-as-insider-buying-meets-a-funding-cost-test/)).
  - Ostatní insideři od srpna do října prodávali v malém: Keough 10 203 ks za 14,72 USD (20. 10.), CTO Rishel 18 624 ks za 17,50 USD (21. 9.). V září proběhlo hromadné vesting a srážka daní ([Insiderset](https://www.insiderset.com/stocks/SOFI/insider-transactions)). Žádné nákupy na volném trhu v říjnu ani listopadu.
- **Short report Muddy Waters (3/2026):** [Fakt; obsah tvrzení je tvrzení MW, ne fakt]
  - tvrdí, že vstupy fair value modelu jsou zavádějící, že skutečná NCO osobních úvěrů je ~6 % (místo vykázaných 2,8 % za Q4 25) kvůli prodejům delikventních úvěrů a VIE mimo rozvahu, že adj. EBITDA je po úpravách o ~90 % nižší a že se aktivuje marketing (194 mil.),
  - dále tvrdí, že Noto a Lapointe vybrali přes 58 mil. USD přes prepaid variable forwards,
  - SoFi report označila za nepřesný a zvažovala právní kroky ([Motley Fool](https://www.fool.com/investing/2026/03/24/sofi-the-short-thesis/), [Pulse](https://www.pulse.bot/fintech/news/muddy-waters-publishes-18-b-fairvalue-critique-of-sofi-sparking-shortsell-surge-5b5d8d66-e7aa-40cf-adc3-2909d86cae0c)).
  - Moje hodnocení [Názor]: tvrzení o 90% EBITDA nesedí s hotovostním NII. Body o tenké diskontní přirážce a o tom, že vykázané NCO je podhodnocené prodeji delikventních úvěrů, ale platí, a sama SoFi uvádí vedle vykázaných 2,26 % „all-in“ 3,4 %. Ratingové agentury podle MW počítají u ABS SoFi s defaulty ~5 %, což zhruba odpovídá vlastnímu předpokladu SoFi 5,10 %.
- **Hromadná žaloba** zákazníka SoFi Securities (kontraktní spor) běží u soudu v N. D. Cal. ([10-Q](https://web.quartr.com/m/sources/s45877629022)), zatím bez materiálního dopadu. Změnu auditora ani významné transakce se spřízněnými stranami jsem v podkladech nenašel (neověřováno do hloubky). [Fakt/Názor]

## Požadovaný výnos a valuace (kroky 8–9)

### Krok 8 – rizikový profil a požadovaný výnos

**Baseline:** 10Y UST je ~5,1 % (GS, 16. 11. 2026, research/log). Riziková prémie akciového trhu ~4–5 % dává výnos pasivní alternativy (široký US index) zhruba **9–10 % p. a.** [Odhad]

**Rizikové faktory SOFI:**

1. **Nezajištěný spotřebitelský úvěr rostoucí v utahovacím cyklu (prémii zvyšuje výrazně).** Osobní úvěry tvoří 61 % úvěrového portfolia a jejich jistina rostla o 18 % q/q. Předpoklad defaultů se za tři čtvrtletí zvedl ze 4,5 na 5,1 %. Fed v září zvýšil na 3,75–4,00 % ([Quartr](https://web.quartr.com/m/sources/s80497687512)) a GS čeká další dva hiky. Nesezónované vintage z rekordního roku 2026 projdou zkouškou právě v 2027. Odhaduji +2 až +3 p. b.
2. **Netransparentní zisk přes fair value (prémii zvyšuje).** Kumulativní FV úpravy jsou 14 % TBV, diskontní přirážka 0,81 p. b. nad 2Y SOFR, adjusted metriky a otevřený spor se short-sellerem. Investor nemůže kvalitu zisku ověřit zvenku a bude ji ověřovat až cyklus. Odhaduji +1 až +2 p. b.
3. **Závislost na kapitálových trzích a kapitálu (prémii zvyšuje).** Pro rezidua osobních úvěrů je jen omezený okruh kupců ([Quartr](https://web.quartr.com/m/sources/s45877629022)), kapitál ubývá o ~180 bp za čtvrtletí, v 2025 proběhly emise a SBC běží. Pokud LPB zamrzne, musí SoFi úvěry držet a kapitál dojde dřív. Odhaduji +1 p. b.
4. **Chování akcie (zvyšuje mírně).** Beta 2,24, short interest 17 % a silná retailová základna vedou k velkým výkyvům a riziku, že akcii prodávám ve špatnou chvíli. Výborná likvidita naopak žádnou prémii za nelikviditu nevyžaduje. Odhaduji +0,5 p. b.
5. **Bankovní licence, kapitálový polštář a exekuce managementu (prémii snižuje).** 90 % fundingu jsou vklady, CET1 16,9 %, EPS překonal odhady v 15 ze 16 kvartálů ([Fool](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/)) a guidance se letos zvedala. CEO s historií nákupů vlastních akcií. Odhaduji −1 až −2 p. b.

**Závěr:** Čistá prémie nad baseline vychází zhruba na +4 až +7 p. b., takže **požadovaný výnos je 14–17 % p. a.** Spodní hranici beru, pokud Q4 a guidance na 2027 projdou bez škrtu a úvěrové metriky zůstanou stabilní. Horní hranice platí, dokud se fair value model a úvěrová kvalita nepotvrdí skutečnými ztrátami v cyklu. Z pohledu Tomášova portfolia jde o firmu s pákovou expozicí na US spotřebitele, proto bych se k dolnímu konci (výnos indexu) nepřibližoval. [Názor]

**Horizont:** ~2 roky (do 11/2028). Teze se potvrdí nebo vyvrátí na výsledcích 2027 (Q4 2027 vyjde koncem ledna 2028) a na tom, jak vintage 2026 projdou rokem vyšších sazeb. Na konci horizontu bude trh oceňovat FY2029. [Odhad]

### Krok 9 – valuace

**Multiples vs. peers** [Fakt, zdroje u řádků; data k různým dnům]

| Firma | Proč srovnávat | Valuace | Poznámka | Zdroj |
|---|---|---|---|---|
| **SOFI** | – | fwd P/E 18,1× · 15,9× FY27 guide · P/TBV 1,91× | ROTCE 9,9 %, tržby +44 % | výpočet, [Fool](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/) |
| NU (Nu Holdings) | digitální banka, cross-sell, unsecured | fwd P/E 12,9×, P/E 16,6× (13. 11.) | konsenzus Buy | [StockAnalysis](https://stockanalysis.com/stocks/nu/) |
| ALLY | US digitální banka bez poboček | P/TBV 0,78×, P/E TTM 7,8×, ROE ~10 % (17. 11.) | zralá, auto úvěry | [FinSpry](https://finspry.com/stocks/ally/statistics) |
| LendingClub | digitální banka, osobní úvěry, marketplace | P/B 1,46×, P/E 11,2×, ROE ~9 % | datum dat nejasné (pravděpodobně jaro 2026) | [TipRanks](https://www.tipranks.com/stocks/lc/statistics) |
| Upstart | AI lender, prodej úvěrů | ~8,2× forward normalizovaný zisk (před propadem 10. 11.) | snížil guidance, defaulty rostou | [TIKR, 11. 11.](https://www.tikr.com/blog/upstart-just-hit-a-new-52-week-low-after-falling-14-in-a-month-is-the-selling-overdone) |
| Robinhood | retailový broker / super-app | fwd P/E ~26× (11. 11.) | bez úvěrového rizika | [TIKR, 11. 11.](https://www.tikr.com/blog/robinhood-rises-5-as-record-trading-day-shows-cautiously-aggressive-customers-buying-the-dip) |
| Chime | neobanka, debit/vklady | fwd P/E 34,2×, P/S ~4,8× (17. 11.) | bez úvěrové rozvahy | [StockAnalysis](https://stockanalysis.com/stocks/CHYM) |

Čtení [Názor]: Vůči bankám s podobným ROTCE (ALLY 0,8×, LC ~1,5× book) má SOFI zhruba dvojnásobnou prémii na TBV. Ospravedlňuje ji jen růst a cesta k vyššímu ROTCE. Na P/E je SOFI dražší než NU, který roste podobně a má vyšší ziskovost. Násobky Robinhoodu a Chime nejsou fér srovnání, protože tyto firmy nenesou úvěrové riziko. SOFI je hybrid a trh ho oceňuje mezi bankou a fintechem.

**Excess return model (P/TBV vs. ROTCE)** [Odhad, výpočet]
- P/TBV = 1 + (ROTCE − ke) / (ke − g). Při dnešních 1,91× trh implikuje udržitelné ROTCE **15,5 %** (ke 11 %, g 6 %) až **18,4 %** (ke 12 %, g 5 %).
- Z guidance na 2027 vychází ROTCE ~12 %, cíl managementu je 20–30 % ([transcript](https://web.quartr.com/m/sources/s74138636689686370535633)). Trh tedy počítá s tím, že SoFi zhruba polovinu cesty k cíli ujde.

**Reverse DCF na EPS** (bez dividend, do konce 2031) [Odhad, výpočet]
- Při ke 12 % a exit P/E 12× potřebuje dnešní cena EPS 2031 **~2,10 USD**, tedy CAGR **28 %** z FY26 (0,61) nebo **24 %** z guidance FY27 (0,90). Při exit P/E 15× stačí EPS ~1,68 (CAGR 22 %, resp. 17 %).
- Pro srovnání: ambice „4× zisk do 2030“ z run-rate Q3 (0,72 USD) znamená EPS ~2,9, „3×“ ~2,2 ([transcript](https://web.quartr.com/m/sources/s89036267966467482268782)). **Trh tedy zhruba počítá s tím, že SoFi splní „3×“ verzi plánu.** Nejde o pesimistické ocenění, spíš o neutrální až mírně skeptické.

**Tři scénáře** (horizont 2 roky, cíl = forward P/E × EPS FY2029E, kontrola přes P/TBV) [Odhad, výpočet v Pythonu]

| Scénář | Pravděpodobnost | EPS 27 / 28 / 29 | Násobek | Cílová cena | Výnos (2 roky / p. a.) | P/TBV v cíli, ROTCE 28 | Klíčový předpoklad |
|---|---|---|---|---|---|---|---|
| Bear | 30 % | 0,60 / 0,62 / 0,75 | 11× | **8,25 USD** | −42 % / −24 % | ~1,0×, ~8 % | Úvěrový cyklus: all-in NCO osobních úvěrů 5–6 %, přecenění úvěrů dolů (~−0,6 mld. po dani), slabší LPB a škrt guidance 2027, ROTCE uvízne pod ke |
| Base | 45 % | 0,84 / 1,08 / 1,32 | 14× | **18,50 USD** | +29 % / +14 % | ~1,9×, ~12 % | Lehce pod guidance 2027 (konsenzus ~0,8), NCO stabilní ~3,5–4 %, růst se přelije do poplatků, kapitál vystačí bez emise |
| Bull | 25 % | 0,95 / 1,30 / 1,70 | 17× | **28,90 USD** | +102 % / +42 % | ~2,8×, ~14 % (2029 ~17–18 %) | Guidance překonána, fee mix k 50 %, ROTCE míří k 20 %, Fed ve 2H27 škrtá (GS) a pomáhá fundingu i markům |

- **Vážená cílová cena: 18,02 USD → +26 % za 2 roky, ~12,3 % p. a.**
- **Požadovaný výnos: 14–17 % p. a. (30–37 % za 2 roky) → vážený výnos je pod laťkou.**
- Citlivost: při pravděpodobnostech 40/40/20 vychází 16,47 USD (~7 % p. a.), při 20/50/30 19,56 USD (~17 % p. a.). Směrodatná odchylka výnosu napříč scénáři je 53 %. [Odhad, výpočet]
- Cena, při které by vážený výnos byl 14 % / 17 % / 25 % p. a.: 13,86 / 13,16 / 11,53 USD. [Odhad, výpočet]
- Transakční srovnání: relevantní M&A pro celou firmu neexistuje.

## Base rate, rizika a protiargument (kroky 10–11)

### Krok 10 – base rate check

- **Fintech věřitelé závislí na prodeji úvěrů a fair value v utahovacím cyklu:** Upstart v 2022 (zamrzlý funding, přecenění úvěrů, a znovu teď v 11/2026 škrt výhledu kvůli defaultům, [TIKR](https://www.tikr.com/blog/upstart-just-hit-a-new-52-week-low-after-falling-14-in-a-month-is-the-selling-overdone)), LendingClub v 2016 (aféra kolem prodejů úvěrů a odchod CEO). Výsledkem byly hluboké propady a dlouhé ocenění kolem book value. Úspěšnost „projít bez škrábnutí“ je nízká. [Názor, události obecně známé]
- **Vkladově financované digitální/spotřebitelské banky:** ALLY se dlouhodobě obchoduje kolem 1× TBV (dnes 0,78×, [FinSpry](https://finspry.com/stocks/ally/statistics)). Prémii nad 2× TBV si historicky udržely jen firmy, které prokázaly ROTCE nad ~15 % skrz celý úvěrový cyklus (Capital One po 2000, dnes NU v LatAm). [Názor]
- **Závěr:** SoFi má proti fintech skupině lepší výchozí pozici (licence, vklady, kapitál), ale cyklem jako banka s velkou unsecured rozvahou ještě neprošla. Base rate pro „re-rating nad 2,5× TBV před prvním testem cyklu“ je podle mě nízký, odhadem pod 30 %, a s tím zhruba sedí pravděpodobnost bull scénáře 25 %. [Názor]

### Krok 11 – rizika podle závažnosti

1. **Úvěrová kvalita osobních úvěrů v 2027.** Rekordní nesezónované vintage 2026, rostoucí předpoklad defaultů, zpomalení spotřeby (MS) a čtení z Upstartu. Úder přichází dvojitě: přes odpisy a přes přecenění celého portfolia drženého ve fair value. [Fakt/Názor]
2. **Fair value a diskontní přirážka.** Při současných vstupech je portfolio na 103,3 % par. Kombinace širších spreadů a vyšších defaultů může TBV srazit o 8–11 % bez jediné „špatné“ zprávy v P&L. Zajištění kryje jen benchmarkové sazby. [Odhad]
3. **Kapitál a ředění.** Při tempu RWA z Q3 kapitálová kapacita vydrží do ~1Q28. Hrozí zpomalení NII, nebo (v horším případě) další emise za nízkou cenu. [Odhad]
4. **LPB a poptávka investorů po úvěrech.** Omezený okruh kupců reziduí. Poptávka je teď silná (dva noví partneři, [transcript](https://web.quartr.com/m/sources/s57464075286015431828880)), ale v risk-off prostředí se rychle otočí. [Fakt/Názor]
5. **Sazby.** Guidance 2027 předpokládá dva hiky. Pokud bude utahování delší (GS) nebo inflace přetrvá (MS), poroste cena fundingu a diskontní sazby. Rychlé škrty by naopak pomohly markům, ale snížily výnos aktiv. [Fakt/Názor]
6. **Regulace a krypto.** GENIUS Act a požadavky OCC na stablecoiny platí od 18. 1. 2027. Bez schválení by SoFi musela přerušit vydávání SoFiUSD ([Quartr](https://web.quartr.com/m/sources/s70760725130)). Dopad na zisk je malý, reputační a provozní riziko větší. [Fakt]
7. **Governance a sentiment.** Spor s Muddy Waters, short interest 17 %, insideři kromě CEO prodávají. [Fakt]

**Nejsilnější protiargument proti mé (opatrné) tezi:** Management letos dvakrát zvedl guidance tržeb, vydal výhled na 2027 o kvartál dřív a růst o 44 % ukázal v nejvolatilnějším prostředí sazeb za roky. Vintage ztráty jsou o ~190 bp lepší než u kohorty 2017, origination fees zlepšují ROE o 200–300 bp ([transcript](https://web.quartr.com/m/sources/s86272996849581500699490)) a NII roste o 59 % r/r ([Quartr](https://web.quartr.com/m/sources/s55434191519)). Pokud úvěrový cyklus přijde mírný (soft landing, Fed škrtá ve 2H27 podle GS), dívá se trh na firmu s 20%+ růstem EPS za ~16× zisku a bull scénář (+100 %) je realističtější než 25 %. Redukce u 52W minima by pak byla prodej na dně. [Názor]

## Conviction, pozice, katalyzátory a monitoring (kroky 12–13)

### Krok 12 – conviction a velikost pozice

- **Conviction: nízká až střední.** Rozptyl scénářů je velmi široký (−42 % až +102 %, směrodatná odchylka 53 %) a edge z kroku 2 je spíš interpretační než informační. [Názor]
- **Tomáš (agresivnější, koncentrované portfolio):** rámcová velikost **5–8 %** portfolia. Současná váha je **14,3 %** (největší pozice, `tools/portfolio.py` 17. 11.), tedy **převážená zhruba 2×**. Celý fintech blok (SOFI, NU, INTR) dělá 20 % portfolia. Bear scénář při současné váze znamená ~−6,0 p. b. na celém portfoliu, při 7% váze ~−3,0 p. b. [Fakt/Odhad, výpočet] → **⚡ Ke zvážení: redukovat k ~7–8 %.** Spěchat na 52W minimu není nutné: rozumné je postupně, třeba část před Q4 výsledky a zbytek podle toho, jak dopadne potvrzení guidance 29. 1. 2027. Tomáš je s pozicí v zisku ~+27 % (nákupka 11,28 USD). [Názor]
- **Michal (konzervativní, 63 % ETF):** rámcová velikost **2–3 %**. Současná váha je **5,4 %** (`tools/portfolio.py`), tedy **mírně převážená**. Pozice je ve ztrátě −16 % (nákupka 17,05 USD). Bear scénář dělá ~−2,3 p. b. na portfoliu. → Nepřikupovat, při odrazu (nad ~17 USD) zvážit snížení k ~3 %. [Názor]
- Nejsem finanční poradce. Tohle je podklad pro Tomášovo rozhodnutí, ne pokyn.

### Krok 13 – katalyzátory a monitoring

| Datum | Událost | Co sledovat |
|---|---|---|
| 24. 11. 2026 | FINRA short interest (settlement 13. 11.) | pokračuje růst nad 224 mil. akcií? ([Equibles](https://equibles.com/stocks/sofi/shortinterest)) |
| prosinec 2026 | FOMC (GS čeká hike) | delší utahování = tlak na diskontní sazby a marky |
| 18. 1. 2027 | Účinnost požadavků GENIUS Act / OCC | schválení nebo výjimka pro SoFiUSD ([Quartr](https://web.quartr.com/m/sources/s70760725130)) |
| 29. 1. 2027 | Q4 2026 + oficiální guidance 2027 ([Quartr](https://web.quartr.com/m/events/782073)) | potvrzení EPS 0,90, předpoklad defaultů, kapitálový poměr, mix LPB vs. rozvaha |
| konec 4/2027 | Q1 2027 | první čtvrtletí s vintage 2026 v plné splácecí fázi |
| konec 1/2028 | Q4 2027 | splnění 2027 = potvrzení / vyvrácení teze |

**Potvrdí tezi (posun k 🟢):** splnění Q4 (adj. EPS 0,19) a potvrzení EPS 0,90 na 2027 · předpoklad defaultů osobních úvěrů ≤5,1 % a all-in NCO ≤3,5 % · total capital ratio stabilizovaný nad ~14 % bez emise · fee-based podíl ≥45 % · ROTCE nad 12 % do 2H27.

**Vyvrátí tezi (🔴):** předpoklad defaultů >5,5 % nebo all-in NCO >4 % · marky osobních úvěrů <101 % · škrt guidance · emise akcií · pokles originací LPB pod ~3 mld. za čtvrtletí · výrazný růst brokered/wholesale fundingu nad 15 % fundingu.

**KPI pro Tracker:** NIM · CET1 / total capital · ROTCE · all-in NCO a 90D delikvence osobních úvěrů · FV vstupy (default, diskont vs. benchmark, marky) · originace LPB · fee-based podíl · vklady · členové a produkty · zředěný počet akcií.

## Zdroje (krok 14)

- **Quartr – firma a eventy:** [SoFi (5065)](https://web.quartr.com/m/companies/5065) · [Q3 2026 event + summary](https://web.quartr.com/m/events/718307) · [Q4 2026 event](https://web.quartr.com/m/events/782073)
- **Quartr – dokumenty:** [10-Q Q3 2026](https://web.quartr.com/m/documents/3912143) · [Earnings release Q3 2026](https://web.quartr.com/m/documents/3912144) · [Slides Q3 2026](https://web.quartr.com/m/documents/4363860) · [Transcript Q3 2026](https://web.quartr.com/m/documents/4364866) · [10-Q Q2 2026](https://web.quartr.com/m/documents/3669941) · [10-K 2025](https://web.quartr.com/m/documents/2857886) · [ER Q4 2025](https://web.quartr.com/m/documents/2697691) · [10-Q Q3 2025](https://web.quartr.com/m/documents/2245072) · roční data [2021](https://web.quartr.com/m/documents/217893), [2022](https://web.quartr.com/m/documents/217892), [2023](https://web.quartr.com/m/documents/329305), [2024](https://web.quartr.com/m/documents/1851132)
- **Quartr – klíčové pasáže:** [FV vstupy 10-Q](https://web.quartr.com/m/sources/s45899898916) · [FV vstupy Q2](https://web.quartr.com/m/sources/s68011501205) · [Loans at FV](https://web.quartr.com/m/sources/s69558816355) · [NCO a vintage](https://web.quartr.com/m/sources/s56977026663) · [Guidance](https://web.quartr.com/m/sources/s81537281477) · [Kapitál / RWA](https://web.quartr.com/m/sources/s65333407541804400762656) · [Total capital −180 bp](https://web.quartr.com/m/sources/s69005017082604098814350) · [Marky](https://web.quartr.com/m/sources/s82335047779879622606148) · [FV ztráty vs. hedge](https://web.quartr.com/m/sources/s66770362676634268395847) · [ROTCE cesta](https://web.quartr.com/m/sources/s74138636689686370535633) · [Konvertibilky 2029](https://web.quartr.com/m/sources/s47001208588)
- **Repo:** research/log/2026-11.md (GS 13. a 16. 11. – sazby, MS 15. 11. – spotřeba, JPM 9. a 13. 11.) · research/themes.md (#fed/#us-rates, #fintech/#us-consumer-credit) · companies/SOFI/dossier.md · `tools/portfolio.py` (17. 11. 2026)
- **Broker / sell-side (přes web):** [Beinsure, 28. 10. 2026](https://beinsure.com/news/sofi-stock-price-forecast-wall-street-analysts-target-15-30/) (Citi, Needham, GS, MS, KBW, BofA…)
- **Ceny a tržní data:** [Motley Fool, 17. 11. 2026](https://www.fool.com/investing/2026/11/17/sofi-targeting-100-million-products-2030-what-10000-invested-today-could-be-worth-if-it-gets-there/) · [StockAnalysis SOFI](https://stockanalysis.com/stocks/sofi/) · [StockAnalysis historie](https://stockanalysis.com/stocks/sofi/history/) · [Equibles short interest](https://equibles.com/stocks/sofi/shortinterest)
- **Peers:** [NU](https://stockanalysis.com/stocks/nu/) · [Chime](https://stockanalysis.com/stocks/CHYM) · [ALLY – FinSpry](https://finspry.com/stocks/ally/statistics) · [LC – TipRanks](https://www.tipranks.com/stocks/lc/statistics) · [Upstart – TIKR](https://www.tikr.com/blog/upstart-just-hit-a-new-52-week-low-after-falling-14-in-a-month-is-the-selling-overdone) · [Robinhood – TIKR](https://www.tikr.com/blog/robinhood-rises-5-as-record-trading-day-shows-cautiously-aggressive-customers-buying-the-dip)
- **Kontext poklesu a short report:** [Motley Fool – short thesis, 24. 3. 2026](https://www.fool.com/investing/2026/03/24/sofi-the-short-thesis/) · [Pulse, 26. 3. 2026](https://www.pulse.bot/fintech/news/muddy-waters-publishes-18-b-fairvalue-critique-of-sofi-sparking-shortsell-surge-5b5d8d66-e7aa-40cf-adc3-2909d86cae0c) · [Muddy Waters – report (PDF, nečten přímo)](https://muddywatersresearch.com/wp-content/uploads/2026/03/MWR_SOFI_11QUESTIONS_0200321.pdf) · [Nasdaq/Fool, 16. 6. 2026](https://www.nasdaq.com/articles/heres-whats-behind-sofis-big-decline-and-what-you-should-do-about-it) · [Nasdaq/Fool, 6. 7. 2026](https://www.nasdaq.com/articles/why-sofi-stock-plummeted-32-first-half-2026) · [TIKR, 3. 10. 2026](https://www.tikr.com/blog/sofi-stock-is-down-43-in-2026-should-you-buy-the-dip-before-november)
- **Emise 12/2025:** [SEC 8-K, 4. 12. 2025](https://www.sec.gov/Archives/edgar/data/1818874/000181887425000225/sofi-20251204.htm) · [Investing.com](https://ng.investing.com/analysis/sofi-slides-as-545mshare-offering-tests-valuation-after-a-strong-2025-rally-212490)
- **Insideři:** [Insiderset](https://www.insiderset.com/stocks/SOFI/insider-transactions) · [TS2, 6/2026](https://ts2.tech/en/sofi-technologies-stock-nasdaqsofi-falls-as-insider-buying-meets-a-funding-cost-test/)
- **Produkt:** [Trustpilot](https://uk.trustpilot.com/review/sofi.com?page=2) · [Financer, 10. 10. 2026](https://financer.com/review/sofi/)
- **Nedostupné v tomto běhu:** stránky StockAnalysis pro LC, ALLY, HOOD a UPST (blokováno / rate limit). Peers jsou proto z alternativních zdrojů s různými daty.
