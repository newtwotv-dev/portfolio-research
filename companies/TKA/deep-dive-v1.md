# Deep dive: thyssenkrupp (TKA) – 18. 11. 2026

_Claude Doc: https://claude.ai/artifact/GkBaGCzmLvqSAAWNLD4KtE · Verze v1 (první deep dive). Cena pro výpočty 11,62 EUR (XETRA close 17. 11. 2026, `state/prices.json`), 18. 11. ve 14:30 intraday 11,43 EUR ([Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-guidance-fuer-stahlgeschaeft-angehoben-945280)). Výpočty SOTP a scénářů: Python skript ve scratchpadu běhu (tka_sotp.py), váhy z `tools/portfolio.py` k 17. 11. Výsledky FY 2025/26 a výhled 2026/27 přijdou až 8. 12. 2026, analýza je tedy „před výsledky“._

## Verdikt

**Signál: ⚡ Ke zvážení: redukovat (velikost pozice u Tomáše). Teze sama zůstává 🟡 Sledovat.** [Názor]

- **Důvod:** Po rally (+38 % za rok) vychází SOTP v base scénáři zhruba na dnešní cenu. Trh už počítá s ocelí s udržitelnou EBITDA **~0,6–0,9 mld. EUR**, letos má ~0,43 mld. (Steel CMD). Další upside potřebuje, aby ocel došla k ambici 1,2 mld.+ a odešla z holdingu i se svými penzemi. **Vážený výnos je +6 % za 1,5 roku (~4 % p. a.), požadovaný 12–15 % p. a.**, a rozptyl scénářů je velký (−56 % / +76 %). U Tomáše je TKA druhá největší pozice (**13,4 %**). S TKMS a TKCC tvoří „rodina thyssenkrupp“ **~17,7 % portfolia**. [Odhad/Názor, výpočet v Pythonu]
- **Scénáře (horizont ~1,5 roku, k 5/2028):**
    - Bear 25 % → **5,10 EUR**
    - Base 50 % → **12,00 EUR**
    - Bull 25 % → **20,40 EUR**
    - vážená cena **12,37 EUR**. [Odhad]
- **Buy podle definice (+50 až +100 % za 1–3 roky) to není.** Laťku požadovaného výnosu by vážený výnos splnil při ceně **~10,0–10,4 EUR**, +50 % při ~8,2 EUR. [Odhad]
- **Proti sell-side:** Konsenzus má 5× Buy a 1× Hold s cílem ~16,75 EUR ([Börse Express, 10. 11.](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-abspaltung-von-tk-accelis-vollzogen-960794)). Podle mě dává oceli plnou hodnotu ambice a podceňuje penze (~6 EUR na akcii) a holdingové náklady. [Názor]
- **Michal:** TKA nedrží.
- **Co by signál zvrátilo:**
    - 🟢 **Posun k ponechání velikosti:** 8. 12. přinese výhled FCF před M&A na 2026/27 aspoň kolem nuly, ocel s adj. EBITDA nad ~0,6 mld. a konkrétní plán oddělení oceli včetně jejích penzí (~2,3 mld.). K tomu KONE closing poběží podle plánu. Pak posunu pravděpodobnosti na 15/50/35 a vážený výnos vyjde ~13 % p. a., tedy na spodní hraně laťky. Stejně tak cena pod ~10,4 EUR při stejných fundamentech.
    - 🔴 **Teze oslabena:** výhled oceli pod 0,43 mld. EBITDA, další odklad nebo přečerpání DRI, FCF 2026/27 pod −0,5 mld., zablokování dealu KONE × TKE nebo struktura oceli, ve které penze zůstanou v holdingu. [Názor]

## Snapshot a kontext (kroky 0–1)

### Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor | Průmyslový holding v transformaci: ocel (Steel Europe), TKMS 51 %, tk accelis 51 %, automotive, Decarbon (Uhde, Polysius, nucera >50 %), 16,2 % v TK Elevator + akcionářská půjčka | [Quartr – struktura](https://web.quartr.com/m/sources/s77822038526) |
| HQ, listing | Essen · XETRA, ADR TKAMY · ISIN DE0007500001 | [Quartr](https://web.quartr.com/m/sources/s67245427553) |
| Cena | 11,62 EUR (17. 11.), −9,6 % za týden, −10,4 % za měsíc [Fakt] | [Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-guidance-fuer-stahlgeschaeft-angehoben-945280) |
| 52W low–high | 6,41–14,21 EUR (před 28. 10. včetně tk accelis ≈ 1,22 EUR na akcii) [Fakt] | [Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-abspaltung-von-tk-accelis-vollzogen-960794) |
| Market cap | **7,23 mld. EUR** (622,5 mil. akcií) [Fakt, výpočet] | [Quartr](https://web.quartr.com/m/sources/s67245427553) |
| EV | Konsolidovaně ~13,4 mld.: mcap + minority za tržní ceny ~3,6 + penze ~5,2 − net cash 2,6. U holdingu je relevantnější SOTP [Odhad] | [Quartr call](https://web.quartr.com/m/sources/s68486709636665933636294) |
| Tržby TTM | ~32,6 mld. EUR [Fakt, součet kvartálů] | [Quartr financials](https://web.quartr.com/m/documents/3670772) |
| Marže 9M 25/26 | hrubá 12,5 % · adj. EBIT 2,4 % (reported 0,2 %) · čistá −1,3 % · FCF před M&A −1,94 mld. (sezónně) [Fakt] | [Quartr](https://web.quartr.com/m/sources/s78350736447) |
| Net debt / EBITDA | Net cash 2,62 mld. (30. 6.), likvidita 5,3 mld. Ukazatel bez penzí nedává smysl [Fakt] | [Quartr Q3](https://web.quartr.com/m/events/556986) |
| Valuace | P/B ~0,8×, fwd P/E ~13× (20. 10., před spin-offem) [Fakt] | [StockAnalysis](https://stockanalysis.com/quote/etr/TKA/statistics/) |
| Free float / insideři | Krupp-Stiftung **21 %** → free float ~79 %. Insideři ~2 % [Fakt] | [Der Aktionär](https://www.deraktionaer.de/nachricht/krupp-stiftungguteszeitfensterfuerverselbststaendigungvonthyssen-stahl-558238.html), [StockAnalysis](https://stockanalysis.com/quote/etr/TKA/statistics/) |
| CEO / CFO | Miguel López / Axel Hamann · Steel Europe: Marie Jaroni | [Quartr](https://web.quartr.com/m/sources/s72885216108381171776118) |
| IR | [thyssenkrupp.com/en/investors](https://www.thyssenkrupp.com/en/investors/calendar) | |
| Konsenzus | 6 domů 5× Buy / 1× Hold, cíl 16,75 EUR. DB Buy 17 (29. 10.), BofA Buy 22, Citi Buy 20, DZ Buy 16 (srpen, před spin-offem), JPM Neutral 12,80 (13. 7.), LBBW Kaufen 18 [Fakt] | [Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-abspaltung-von-tk-accelis-vollzogen-960794), [ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/thyssenkrupp-s-elevator-exit-could-hand-it-3-4bn-and-a-fresh-chapter-in-its-re-rating/70023598), [JPM](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-jpmorgan-hebt-ziel-auf-1280-euro-927681) |
| Likvidita | ~1,8 mil. akcií denně (20D k 20. 10.) ≈ 20–35 mil. EUR → **průměrná** vzhledem k velikosti [Fakt/Odhad] | [StockAnalysis](https://stockanalysis.com/quote/etr/TKA/history/) |
| RSI 14 | Neověřeno, listopadovou řadu nemám. Po −10 % za měsíc odhaduji ~30–35 (k 20. 10. bylo 46) [Odhad] | StockAnalysis |

### Krok 1 – zdroj a kontext idey

- **Zdroj:** stávající pozice. Tomáš drží 68,29 ks na t212 s nákupkou 7,65 EUR, TKMS a TKCC má ze spin-offů s nákupkou 0 (`config/portfolio.yaml`). Dossier vznikl při onboardingu 18. 11. 2026.
- **Proč je cena tam, kde je:**
    - **Duben:** KONE kupuje TK Elevator a TKA dostane ~3,3 mld. EUR, akcie za den +10 % ([ad-hoc-news 30. 4.](https://www.ad-hoc-news.de/boerse/news/ueberblick/thyssenkrupp-s-elevator-windfall-a-3-27-billion-payout-that-could/69261214)).
    - **Srpen–září:** silné Q3 a guidance adj. EBIT zvednutá na 600–900 mil., upgrady a maximum ~15,6 EUR v polovině září.
    - **Od konce září dolů:** Steel CMD (28. 9.) nepřinesl strukturu oddělení oceli, 28. 10. odečet tk accelis (~1,22 EUR, technický), DRI odloženo na 2029 a 12.–13. 11. komentáře SSAB (TKA −2,5 %, [ad-hoc-news 13. 11.](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/thyssenkrupp-shares-retreat-as-ssab-warning-and-duisburg-delay-test-the-green-steel-story/70505809)). Očištěno o TKCC je to od maxima zhruba −17 %. [Fakt/výpočet]
- **Trh a výhled:** Hodnota TKA je v podílech (TKMS, tk accelis, nucera, KONE/TKE) a v osudu oceli. Trh plochých ocelí v EU je podle tkSE stabilní na ~77–78 Mt do 2030. Safeguards EU od 7/2026 kryjí >80 % objemu ([CMD](https://web.quartr.com/m/sources/s66305853606)). GS (13. 11. 2026) drží EU Industrial G&S Neutral a čeká HDP eurozóny 0,9 % v 2027 a TTF 31 EUR/MWh koncem 2027 (research/log, themes #eu-industry). Levnější plyn je pro Duisburg zásadní. [Fakt/Názor]

## Teze a variant perception (krok 2)

**Teze v jedné větě:** TKA je dnes zhruba férově oceněný holding. Listované podíly, výnos z KONE a hotovost pokrývají ~130 % market capu, ale penze (~6 EUR na akcii) a holdingové náklady to vracejí zpátky. Výnos nad laťku vyžaduje, aby ocel došla k ~1,2 mld. EBITDA **a** odešla i se svými penzemi, a to se rozhodne až v letech 2027–28. [Názor]

- **Co si myslí trh:** Narativ „za ocel trh nic neplatí“ už neplatí. Při mých base vstupech pro ostatní části implikuje dnešní cena hodnotu oceli (po cash-outech, před penzemi) **1,3–2,6 mld. EUR**, podle holdingového diskontu 0–15 %. To odpovídá udržitelné EBITDA **~0,6–0,9 mld.** při 4,5× (výpočet v kroku 9). Sell-side jde ještě dál, 5 ze 6 domů má Buy. [Odhad/Fakt]
- **Co si myslím já:** Self-help v oceli je reálný. >50 % upliftu je podle tkSE „locked-in“ ([CMD](https://web.quartr.com/m/sources/s65714431503)), restrukturalizace s odbory je podepsaná, HKM je pryč a safeguards fungují (SSAB 28. 10.: importní zásoby v EU odbourány, ceny výš, [Kitco](https://www.kitco.com/news/off-the-wire/2026-10-28/ssab-tops-profit-expectations-eu-import-curbs-boost-steel-prices)). EBITDA ale ještě není FCF. Do 2029 ocel spotřebuje ~1,5 mld. na zbytek DRI, HKM platby a restrukturalizaci. Penze ~2,3 mld. jsou dnes problém holdingu. [Názor]
- **Proč je sell-side podle mě vedle:**
    1. Penze ~4,7 mld. připadají na holding [Odhad]. Bez jejich odchodu s ocelí se diskont nezavře a o kapitálové struktuře oceli management mluvit odmítá ([Quartr](https://web.quartr.com/m/sources/s92234665096059543026968)).
    2. Holdingové náklady jsou ~180 mil. ročně (HQ 9M −134 mil.). Po spin-offu navíc přestane jít 30–35 mil. alokace na tk accelis ([Quartr](https://web.quartr.com/m/sources/s65459415209)).
    3. Výnos z KONE přijde nejdřív ve 2Q27, zčásti (~75 %) v akciích KONE a pod hloubkovou prověrkou DOJ. [Názor]
- **Edge:** Je interpretační (SOTP a penze) a míří **proti sell-side, ne proti ceně**. Silnou variant perception proti dnešní ceně nemám, proto signál řeší velikost pozice, ne přikoupení. [Názor]

## Byznys model, segmenty a KPI (krok 3)

### Co firma dělá a jak vydělává

TKA se mění na „štíhlý finanční holding“ se samostatnými byznysy, ve kterých si drží většinu ([Quartr](https://web.quartr.com/m/sources/s72885216108381171776118)). Segmenty jsou zatím plně konsolidované. Holding sám žije z dividend a z hodnoty podílů. [Fakt]

| Segment / aktivum | Podíl TKA | Tržby 9M 25/26 | Adj. EBIT 9M 25/26 (24/25) | Poznámka | Zdroj |
|---|---|---|---|---|---|
| TKMS (Marine Systems) | 51 %, kotováno | 1,89 mld. | 110 mil. (85) | backlog 20,1 mld., cíl marže >7 %, růst ~10 % | [Quartr](https://web.quartr.com/m/sources/s50861554587) |
| tk accelis (Materials Services) | 51 %, kotováno od 28. 10. | 9,13 mld. | 178 mil. (82) | LTM adj. EBITDA 327 mil. (2,8 %), cíl 4–5 % | [Quartr](https://web.quartr.com/m/sources/s48376170932), [tk accelis](https://web.quartr.com/m/sources/s56269473830) |
| Steel Europe | 100 % | 7,04 mld. | 373 mil. (177) | CMD: FY25/26E adj. EBITDA ~0,43 mld., ambice 1,2 mld.+ | [Quartr](https://web.quartr.com/m/sources/s48376170932), [CMD](https://web.quartr.com/m/sources/s65714431503) |
| Automotive Technology | 100 % | 5,06 mld. | 98 mil. (98) | slabá poptávka, restrukturalizace | [Quartr](https://web.quartr.com/m/sources/s46445083094) |
| Decarbon Technologies | 100 %, nucera >50 % | 2,12 mld. | −18 mil. (76) | odklady projektů. Nucera: net cash 627 mil., strategická revize | [Quartr](https://web.quartr.com/m/sources/s65556942833) |
| Corporate HQ | – | – | −134 mil. (−141) | holdingové náklady | [Quartr](https://web.quartr.com/m/sources/s44702662871) |
| TK Elevator | 16,2 % + půjčka + prioritní akcie | – | – | fair value akcií 1,64 mld. (30. 6.), deal s KONE | [Quartr](https://web.quartr.com/m/sources/s67651320639) |

**Rozpor v číslech oceli:** Segment vykázal za 9M adj. EBIT 373 mil., Steel CMD přitom uvádí adj. EBITDA za celý FY25/26E jen ~0,43 mld. ([CMD](https://web.quartr.com/m/sources/s55342264213)). Definice ani perimetr tedy nejsou stejné (standalone tkSE vs. segment). Pro valuaci beru konzervativnější CMD bázi, ověřit 8. 12. [Fakt/Názor]

### Moat

- **Ocel: slabý až střední.** Pozitiva: #2 v EU plochých ocelích, ~65 % prémiového mixu, jediný výrobce top tříd GOES v EU, >70 % zákazníků do 500 km ([CMD](https://web.quartr.com/m/sources/s78898120483)). Negativa: cyklus, energie, CO2 a závislost na ochraně EU. [Fakt/Názor]
- **TKMS: silný.** Konvenční ponorky jsou oligopol, backlog je ~8× tržby ([Quartr](https://web.quartr.com/m/sources/s65928844758)). [Fakt]
- **tk accelis:** #1 v DE/EU a #3 v Severní Americe, top 10 zákazníků pod 10 % tržeb, ale nízké marže distribuce ([Quartr](https://web.quartr.com/m/sources/s50637236846)). [Fakt]
- **Holding: žádný.** Hodnotu tvoří alokace kapitálu. [Názor]

### Sektorové KPI (ocel / obrana)

| KPI | Hodnota | Zdroj |
|---|---|---|
| Ocel – FTE | ~27 tis. (9/2024) → ~16 tis. ve FY29/30, ~4 tis. hotovo | [CMD](https://web.quartr.com/m/sources/s78792029210) |
| Ocel – uplift EBITDA | restrukturalizace ≥0,3 + HKM exit ≥0,3 (plně od FY28/29) + non-FTE >0,2 mld. + trh a mix; objemy 8,7–9,0 Mt | [CMD](https://web.quartr.com/m/sources/s45266549035) |
| Ocel – capex | base ~0,5 mld. po DRI | [CMD](https://web.quartr.com/m/sources/s60060630615) |
| Ocel – DRI | ~3 mld. capex, 2 mld. dotace, net dosud ~0,3 mld., start 2029 | [Quartr](https://web.quartr.com/m/sources/s75286002496999052384657), [net](https://web.quartr.com/m/sources/s68113481832067869331134) |
| Ocel – penze | ~2,4 mld. (30. 9. 2025, z toho ~0,1 HKM), platby ~0,2 mld. ročně | [CMD](https://web.quartr.com/m/sources/s81740869604) |
| TKMS | backlog 20,1 mld., book-to-bill ~2× | [Quartr](https://web.quartr.com/m/sources/s56502108080) |

### Produkt a recenze

- **Ocel:** Dlouhodobí OEM partneři (Toyota, Porsche, Volvo) a JV Tagal pro čínské OEM v EU ([CMD](https://web.quartr.com/m/sources/s85493027531)). Order intake oceli za 9M +1 % ve slabém trhu. [Fakt]
- **TKMS:** Kanada ho vybrala jako preferovaného dodavatele až 12 ponorek a Německo objednalo 4 fregaty MEKO ([Quartr](https://web.quartr.com/m/sources/s67244780107)). To je nejsilnější „recenze“ od zákazníků. [Fakt]
- **Decarbon:** Zelený vodík a cement jsou ztrátové a nesou technická rizika ([Quartr](https://web.quartr.com/m/sources/s52809546605720709955099)). [Fakt]

## Finance, alokace kapitálu, rozvaha a governance (kroky 4–7)

### Krok 4 – finance

| FY (do 30. 9.) | Tržby | EBITDA (reported) | Čistý zisk | Zdroj |
|---|---|---|---|---|
| 2021/22 | 41,1 mld. | 3,25 mld. | 1,22 mld. | [Quartr](https://web.quartr.com/m/documents/130487) |
| 2022/23 | 37,5 mld. | 1,68 mld. | −1,99 mld. | [Quartr](https://web.quartr.com/m/documents/268947) |
| 2023/24 | 35,0 mld. | 0,90 mld. | −1,45 mld. | [Quartr](https://web.quartr.com/m/documents/1785564) |
| 2024/25 | 32,8 mld. | 1,49 mld. | 0,53 mld. (adj. EBIT 0,64, FCF před M&A 0,36) | [Quartr](https://web.quartr.com/m/documents/2490630), [AGM](https://web.quartr.com/m/sources/s290436860250011190217) |
| 9M 2025/26 | 24,4 mld. | 0,25 mld. | −0,31 mld. (FCF před M&A −1,94) | [Quartr](https://web.quartr.com/m/sources/s78350736447) |
| Guidance FY25/26 | −3 až −1 % | – | −0,7 až −0,4 mld. (adj. EBIT 0,6–0,9, FCF −0,6 až −0,3) | [Quartr](https://web.quartr.com/m/sources/s89333945752814833987864) |

- **Trend:** Tržby padají pátý rok (exity, ceny oceli), adj. EBIT roste díky self-help. Reported čísla jsou zaplevelená one-offy. Za 9M šlo o restrukturalizaci ~0,5 mld., odpis HKM 276 mil., write-up oceli +407 mil. a −99 mil. z přecenění půjčky TKE ([Quartr](https://web.quartr.com/m/sources/s69047325573)). Kladný čistý zisk FY24/25 stál na one-offech. [Fakt]
- **Kvalita zisku:** Nízká. Adj. EBIT marže 2,4 % a slabá konverze na FCF (capex 1,2–1,3 mld., restrukturalizace až 0,25 mld., odliv záloh TKMS). [Fakt/Názor]
- **Přechodné vs. strukturální:**
    - Strukturální: úspory v oceli (−3,5 tis. FTE YTD), safeguards (v číslech zatím nejsou), růst tk accelis v Severní Americe.
    - Přechodné: write-upy kolem HKM, část marže tk accelis z přecenění zásob ([Quartr](https://web.quartr.com/m/sources/s59541706342189203240426)), claims v automotive. Q4 zatíží dekonsolidace HKM v nízkých stovkách mil. ([Quartr](https://web.quartr.com/m/sources/s61710472899554210626387)). [Fakt]
- **Implikovaný Q4:** Pro splnění FCF guidance musí Q4 přinést **+1,3 až +1,6 mld.** Je to sezónně obvyklé, ale je to klíčová kontrola 8. 12. ([Quartr](https://web.quartr.com/m/sources/s80624101311757081681928)). [Výpočet]

### Krok 5 – alokace kapitálu

- **Portfolio:** Spin-offy TKMS a tk accelis (po 49 % akcionářům), prodej HKM, zbytku AST a Automation Engineering ([Quartr](https://web.quartr.com/m/sources/s83545601487)). Hodnota spin-offů šla akcionářům, ne do kasy holdingu. López 51% podíly prodávat nechce ([Quartr](https://web.quartr.com/m/sources/s76148079777702356074815)). [Fakt]
- **TK Elevator → KONE:**
    - **Deal:** EV 29,4 mld. EUR = 5 mld. cash + až 270 mil. nových akcií KONE + refinancování ~9,2 mld. dluhu ([Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/kone-agrees-buy-tk-elevator-132708315.html)). [Fakt]
    - **Co dostane TKA** (podle Reuters/JPM): **0,81 mld. cash + až 2,46 mld. v akciích KONE (~5,5 % spojené firmy)**, celkem ~3,27 mld., Jefferies/JPM až 3,4 mld. ([Reuters přes GBAF](https://www.globalbankingandfinance.com/thyssenkrupp-line-4-billion-payday-kone-tk-elevator-deal/)). To je ~43,7 mil. akcií KONE (referenční cena ~56,3 EUR), při dnešních 57,82 EUR ([Nordnet](https://www.nordnet.fi/markkinakatsaus/osakekurssit/16103263-kone-corporation)) **~3,34 mld. hrubě**. [Fakt/výpočet]
    - **Daně:** podle CFO „insignificant“ ([Quartr](https://web.quartr.com/m/sources/s69184270830275094482592)). [Fakt]
    - **Nejistoty:**
        - Rozpad plnění (půjčka, prioritní a kmenové akcie) ani lock-up nejsou veřejně potvrzené, čísla jsou odhady bank.
        - TKA v Q3 posunula očekávané splacení bezúročné půjčky a zaúčtovala −99 mil. ([Quartr](https://web.quartr.com/m/sources/s61834361682)), část hodnoty tedy může přijít později.
        - DOJ dělá hloubkovou prověrku a KONE chystá prodej aktiv ([Investment Monitor](https://www.investmentmonitor.ai/news/doj-antitrust-probe-kone-tk-elevator-deal/)).
    - **Implikovaný násobek:** EBITDA TKE ve zdrojích nemám, násobek proto nepočítám. KONE čeká synergie ~0,7 mld. ročně. [Fakt]
- **Capex, dividenda:** capex snížen na 1,2–1,3 mld., dividenda 0,15 EUR (~93 mil.), buyback žádný. Návrh dividendy přijde 8. 12. [Fakt]
- **Hodnocení:** Historický track record je špatný (Steel Americas, neúspěchy s ocelí). Současný management ale TKMS, tk accelis, HKM i KONE dotáhl. [Názor]

### Krok 6 – rozvaha

- **Konsolidovaně:** net financial assets 2,62 mld. (30. 6. 2026, 30. 9. 2025 to bylo 4,9 mld.), likvidita 5,3 mld. Finanční dluh ~1,0 mld., CP čerpáno 79 mil. ([Quartr](https://web.quartr.com/m/sources/s60064479929), [AGM](https://web.quartr.com/m/sources/s290436860250011190217)). [Fakt]
- **Holdingová net cash (bez dceřinek s minoritami):** 2,62 − TKMS 0,83 − nucera 0,63 + net dluh tk accelis 0,74 = **~1,9 mld. k 30. 6.** Po sezónním Q4 a snížení páky tk accelis odhaduji **~2,7–2,9 mld. k 30. 9.** ([TKMS](https://web.quartr.com/m/sources/s65928844758), [nucera](https://web.quartr.com/m/sources/s65556942833), [tk accelis](https://web.quartr.com/m/sources/s72505173532)). [Odhad]
- **Financování holdingu:** RCF 1,7 mld. + garanční linka 1,25 mld., nečerpáno. Covenant LTV (čistý dluh vs. hodnota podílů TKMS, nucera, TKE, tk accelis) je max. 55 %, dnes −14 %. Při překročení se zřizuje zajištění na podíly ([Quartr](https://web.quartr.com/m/sources/s60064479929)). [Fakt]
- **Penze:** ~5,2 mld. konsolidovaně, z toho ~polovina ocel. Na HKM přešly jen nízké stovky mil., část přešla na tk accelis ([Quartr](https://web.quartr.com/m/sources/s93583010189065710518933), [tk accelis](https://web.quartr.com/m/sources/s52698206825683097051163)). Na holding podle mě připadá **~4,7 mld.** [Odhad]. Platby ~0,3–0,4 mld. ročně podle analytika na callu ([Quartr](https://web.quartr.com/m/sources/s75290832968599479559676)). [Fakt/Odhad]
- **Net debt / EBITDA s penzemi:** ~2,6 mld. čistého dluhu, tedy ~1,5–1,7× adj. EBITDA [Odhad]. Rating a splatnosti jsem neověřoval.

### Krok 7 – vlastnictví a governance

- **Krupp-Stiftung (21 %, blokační vliv):** podporuje osamostatnění oceli „vlastní silou“ bez státu a ve spin-offnuté oceli by si podíl nechala ([Der Aktionär, 14. 10.](https://www.deraktionaer.de/nachricht/krupp-stiftungguteszeitfensterfuerverselbststaendigungvonthyssen-stahl-558238.html)). [Fakt]
- **Institucionálové:** GS 4,81 % (převážně instrumenty), MS 3,9 %, BlackRock navyšuje ([ad-hoc-news 16. 11.](https://www.ad-hoc-news.de/boerse/news/corporate-news/thyssenkrupp-stock-goldman-sachs-cuts-holding-below-5-prozent/70521822)). Jde spíš o obchodní pozice. [Fakt/Názor]
- **Insideři:** Celé představenstvo koupilo 18.–19. 2. 2026 akcie za **~0,49 mil. EUR** při ~10,94 EUR (~9,7 EUR po odečtu TKCC) ([directors' dealings](https://ucpcdn.thyssenkrupp.com/_binary/UCP5thyssenkruppAG/f0eb4e30-aec3-4450-ba53-c9cc8f9db1f9/Directors-Dealings-Meldung-Internet-202526-E2.pdf)). Prodeje jsem nenašel. [Fakt]
- **Struktura a odbory:** TKMS, tk accelis a nucera jsou KGaA, TKA je kontroluje s 51 %. Spolurozhodování a IG Metall jsou tvrdé omezení: listopadové stávky (Saarland, Rasselstein, [Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-abspaltung-von-tk-accelis-vollzogen-960794)) a kritika dealu KONE × TKE. [Fakt]
- **Účetní citlivost:** Ocenění TKE je Level 3, diskontní sazba kmenových akcií se snížila z 11,29 na 9,14 % ([Quartr](https://web.quartr.com/m/sources/s67651320639)). Write-upy oceli stojí na předpokladech. Změnu auditora jsem neověřoval. [Fakt]

## Požadovaný výnos a valuace (kroky 8–9)

### Krok 8 – rizikový profil a požadovaný výnos

**Baseline:** 10Y Bund ~3,3 % (GS, 13. 11. 2026). S prémií ~4,5–5 % vychází pasivní evropský index na **~8–8,5 % p. a.** GS přitom čeká u STOXX 600 za 12 měsíců jen 5,5 % (research/log). [Odhad/Fakt]

**Rizikové faktory TKA:**

1. **Penze jako skrytá páka (zvyšuje výrazně, +1,5 až +2 p. b.).** ~4,7 mld. proti mcap 7,2 mld. Plán, ve kterém ocel penze nevezme, by stál jednotky eur na akcii. Jindal neuzavřel i kvůli penzím ([Construction World/Reuters](https://www.constructionworld.in/amp/steel-news/jindal-steel-deal-with-thyssenkrupp-at-risk-over-pensions-and-energy/89006)).
2. **Cykličnost a politická závislost oceli (zvyšuje, +1,5 až +2 p. b.).** EBITDA marže ~4 %, závislost na safeguards, čínském dovozu, energii a hladině Rýna. SSAB 12.–13. 11. ukázala, jak rychle se sentiment otočí.
3. **Exekuce restrukturalizace a DRI (zvyšuje, +1 až +1,5 p. b.).** 11 tis. míst, IG Metall, DRI za 3 mld. odložené na 2029, tender na vodík se teprve připravuje. Historie TKA je plná projektů, které stály víc a trvaly déle.
4. **Složitost holdingu a konglomerátní diskont (zvyšuje, +1 p. b.).** Sedm hodnotových bloků, dva v Level 3. Realizace hodnoty záleží na managementu a Krupp-Stiftung.
5. **Kotva v listovaných podílech, net cash a nákupech insiderů (snižuje, −1 až −1,5 p. b.).** Listované podíly za 3,7 mld. jsou denně ocenitelné, TKE se mění v cash a likvidní akcie KONE a management doručuje milníky. Likvidita akcie je dobrá.

**Závěr:** Čistá prémie +4 až +6 p. b. dává **požadovaný výnos 12–15 % p. a.** Spodní hranice platí, když ocel dostane vlastní kapitálovou strukturu včetně penzí, horní, dokud penze a DRI zůstávají v holdingu. U druhé největší pozice koncentrovaného portfolia bych nešel pod 12 %. [Názor]

**Horizont ~1,5 roku (do 5/2028):** Do té doby proběhnou výsledky FY25/26 (8. 12.) a FY26/27 (12/2027), KONE closing (nejdřív 2Q27) a rozhodnutí o struktuře oceli. CEO 28. 10. řekl, že ocel je další kandidát na IPO ([GMK Center](https://gmk.center/en/news/thyssenkrupp-prepares-steel-division-for-spin-off-ceo/)). Plný efekt HKM exitu (FY28/29) a start DRI (2029) jsou až za horizontem. [Odhad]

### Krok 9 – valuace

**SOTP při dnešních cenách (base vstupy)** [Fakt u tržních cen, jinak Odhad, výpočet v Pythonu]

| Blok | mld. EUR | EUR/akcie | Jak | Zdroj |
|---|---|---|---|---|
| TKMS 51 % | 2,44 | 3,92 | 32,4 mil. ks × 75,30 (63,53 mil. akcií celkem) | [Quartr](https://web.quartr.com/m/sources/s65928844758) |
| tk accelis 51 % | 0,79 | 1,27 | 32,4 mil. ks × 24,34 (31,1 mil. rozdáno = 49 %) | [trend.at](https://www.trend.at/news/tk-accelis-bei-borsendebut-mit-177-milliarden-euro-bewertet) |
| nucera ~50,2 % | 0,49 | 0,79 | 63,3 mil. ks × ~7,76 | [stock3](https://stock3.com/aktien/thyssenkrupp-nucera-64433222) |
| TKE → KONE | 2,9 | 4,66 | hrubě 3,34 mld., ~13% srážka za čas, riziko dealu a strukturu | krok 5 |
| Steel Europe (EV po cash-outech, před penzemi) | 2,3 | 3,73 | 0,85 mld. EBITDA × 4,5 − 1,5 mld. (DRI ~0,7, HKM ~0,3, restrukturalizace ~0,5) | [CMD](https://web.quartr.com/m/sources/s65714431503), [HKM](https://web.quartr.com/m/sources/s66903194223940684512062) |
| Automotive Technology | 1,0 | 1,61 | ~7× normalizovaný adj. EBIT ~0,14 mld. | [Quartr](https://web.quartr.com/m/sources/s48376170932) |
| Decarbon bez nucera | 0,3 | 0,48 | opční hodnota | [Quartr](https://web.quartr.com/m/sources/s46445083094) |
| Holdingové náklady | −0,9 | −1,45 | −0,15 mld. ročně × 6 | [Quartr](https://web.quartr.com/m/sources/s44702662871) |
| Penze (holding) | −3,76 | −6,04 | ~4,7 mld. × 0,8 (daňový štít krácený o ztráty) | [Quartr](https://web.quartr.com/m/sources/s93583010189065710518933) |
| Holdingová net cash | +2,7 | +4,34 | krok 6 | |
| **NAV** | **8,28** | **13,31** | | |
| Diskont 10 % → **base** | **7,45** | **~12,0** | proti 11,62 → **+3 %** | |

- **Kontrola:** Listované podíly samy dělají 51 % mcap, s TKE a hotovostí **129 %**. „Zbytek“ (ocel, automotive, Decarbon) minus penze a holding tedy trh oceňuje na −2,1 mld. [Výpočet]
- **Reverse SOTP (co trh platí za ocel):** Dnešní cena implikuje ocel (po cash-outech) za **1,27 / 2,08 / 2,55 mld.** při holdingovém diskontu 0 / 10 / 15 %. To odpovídá udržitelné EBITDA **0,62 / 0,80 / 0,90 mld.** při 4,5×, proti ~0,43 letos a ambici 1,2+. Trh tedy už počítá se zhruba polovinou až třemi čtvrtinami cesty. [Odhad, výpočet]

**Multiples vs. peers** [Fakt, StockAnalysis, data k různým dnům]

| Firma | Proč | EV/EBITDA TTM | fwd P/E | P/B | Datum |
|---|---|---|---|---|---|
| **TKA** | – | ~11× (zkreslené one-offy) | ~13× | 0,80× | 20. 10. ([odkaz](https://stockanalysis.com/quote/etr/TKA/statistics/)) |
| ArcelorMittal | integrovaná ocel EU | 10,3× | 10,6× | 0,79× | 23. 10. ([odkaz](https://stockanalysis.com/stocks/mt/statistics/)) |
| Salzgitter | německá ocel, kupec HKM | 9,5× | 9,1× | 0,58× | 19. 10. ([odkaz](https://stockanalysis.com/quote/etr/SZG/statistics/)) |
| voestalpine | prémiová ocel a zpracování | 6,0× | 11,5× | 1,00× | 17. 9. ([odkaz](https://stockanalysis.com/quote/vie/VOE/statistics/)) |
| SSAB | prémiová ocel | 4,7× | 9,4× | 0,83× | nejasné, spíš starší ([odkaz](https://stockanalysis.com/quote/sto/SSAB.B/statistics/)) |
| Klöckner & Co | distribuce (vs. tk accelis) | 17,4× | 23,7× | 0,92× | 12. 8. ([odkaz](https://stockanalysis.com/quote/etr/KCO/statistics/)) |

Čtení [Názor]: Vysoké TTM násobky ArcelorMittalu a Salzgitteru jsou dané depresivní EBITDA. Na normalizovanou EBITDA se evropská ocel historicky obchoduje kolem 4–6×, proto pro tkSE beru 4,0 / 4,5 / 5,0×. Diskont TKA tedy nevzniká v ocelářském násobku, ale v penzích a holdingu. tk accelis je na ~5,8× LTM adj. EBITDA (EV ~1,9 mld.). Proti Klöckneru na cyklickém dně je levný, distribuce má ale nízké marže. [Odhad]

**Transakce:** KONE × TKE je už v SOTP. U oceli je „cenovka“ spíš negativní: Jindal neuzavřel kvůli penzím, energii a investicím ([Börsen-Zeitung](https://www.boersen-zeitung.de/unternehmen-branchen/verkauf-der-stahlsparte-von-thyssenkrupp-erneut-auf-eis)). [Fakt]

**Tři scénáře** (horizont 1,5 roku, cíl = NAV × (1 − diskont)) [Odhad, výpočet v Pythonu]

| Scénář | p | Ocel (EBITDA × násobek − cash-outy) | Listované podíly | TKE | Penze / net cash | Diskont | Cíl | Výnos (1,5 r. / p. a.) |
|---|---|---|---|---|---|---|---|---|
| Bear | 25 % | 0,55 × 4,0 − 1,6 = 0,6 | −20 % (2,97) | 2,5 | −4,0 / 2,2 | 15 % | **5,10 EUR** | −56 % / −43 % |
| Base | 50 % | 0,85 × 4,5 − 1,5 = 2,3 | dnes (3,72) | 2,9 | −3,76 / 2,7 | 10 % | **12,00 EUR** | +3 % / +2 % |
| Bull | 25 % | 1,2 × 5,0 − 1,3 = 4,7 | +20–25 % (4,63) | 3,3 | −3,5 / 3,0 | 5 % | **20,40 EUR** | +76 % / +46 % |

- **Bear:** Ocel uvízne kolem 0,5 mld. (energie, slabá EU, oslabení safeguards), DRI se prodraží, IPO oceli nevyjde, obrana se přecení dolů a KONE se protáhne s ústupky. TKA zůstane „TKMS proxy s penzemi“.
- **Base:** Ocel ~0,85 mld. do FY27/28, KONE closing ve 2H27, struktura oceli se rýsuje, ale penze zůstávají v holdingu.
- **Bull:** Ocel splní 1,2 mld.+ a odejde (IPO nebo spin-off) i s penzemi, TKMS uzavře Kanadu, TKE přinese plných ~3,3 mld. a holdingové náklady klesnou.
- **Vážená cena 12,37 EUR → +6,4 % za 1,5 roku (~4,2 % p. a.) vs. požadovaných 12–15 % p. a. (~19–23 % za 1,5 roku) → výrazně pod laťkou.**
- **Citlivost:** Při pravděpodobnostech 30/50/20 vychází 11,60 EUR (~0 % p. a.), při 20/50/30 13,14 EUR (~8,5 % p. a.), při 15/50/35 13,90 EUR (~12,7 % p. a.). Směrodatná odchylka výnosu je 47 %. Cena pro 12 % / 15 % p. a.: 10,43 / 10,03 EUR. [Výpočet]
- **Rozpor se sell-side:** Můj base je ~30 % pod konsenzem 16,75. Rozdíl dělají penze, ocel (0,85 vs. 1,2 mld.) a diskont. Nejblíž mému pohledu je JPM (Neutral 12,80). [Názor]

## Base rate, rizika a protiargument (kroky 10–11)

### Krok 10 – base rate check

- **Německé rozdělování konglomerátů:** Siemens (Healthineers, Energy) a Daimler (Truck) ukazují, že spin-offy hodnotu odemknout umí. Diskont se ale zavíral až po odchodu problémového byznysu i s jeho závazky. [Názor, obecně známé]
- **TKA a ocel:** JV s Tatou zablokovala EU (2019), Liberty (2021) a EPCG/Křetínský se rozpadly, Jindal je pozastavený (5/2026). Peníze z Elevatoru (17,2 mld., 2020) z velké části shořely v provozu. Base rate „oddělit ocel napoprvé a i s penzemi“ je u TKA **nízký**. [Fakt/Názor]
- **Ocelářské spin-offy:** Aperam (2011) a Outokumpu/Inoxum (2012) byly po oddělení roky pod tlakem cyklu. Spin-off sám o sobě není katalyzátor, pokud nepřijde v dobré fázi cyklu. [Názor]
- **Holdingové diskonty:** Evropské holdingy mají běžně 15–40 % k NAV. TKA je dnes ~13 % pod mým base NAV, což je při tolika Level 3 aktivech a penzích mělký diskont. [Názor/Výpočet]
- **Závěr:** Bull (25 %) vyžaduje, aby TKA porazila vlastní historii. Nad 30 % bych ho zvedl až po konkrétním plánu oceli s penzemi.

### Krok 11 – rizika podle závažnosti

1. **Penze a struktura oddělení oceli.** Odchod oceli bez penzí, nebo s dotací hotovosti od holdingu, je přímý odpis hodnoty na akcii. [Názor]
2. **Ocelářský cyklus, energie a politika.** Slabá EU poptávka a závislost na safeguards a CBAM. **Rozpor:** SSAB 28. 10. hlásila lepší rovnováhu trhu a vyšší ceny ve Q4 ([Kitco](https://www.kitco.com/news/off-the-wire/2026-10-28/ssab-tops-profit-expectations-eu-import-curbs-boost-steel-prices)), 12.–13. 11. ale její komentáře evropskou ocel stáhly ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/thyssenkrupp-shares-retreat-as-ssab-warning-and-duisburg-delay-test-the-green-steel-story/70505809)). [Fakt]
3. **DRI.** Odklad na 2029, drahý vodík, závazek 1,04 mld. ([Quartr](https://web.quartr.com/m/sources/s46148955936)). Dotace 2 mld. platí, přečerpání ale nese TKA. [Fakt]
4. **Záporný FCF.** Net cash klesl za 9 měsíců z 4,9 na 2,6 mld. a FY26/27 ponese DRI, HKM a restrukturalizaci. Pokud Q4 nedoručí +1,3 až +1,6 mld., guidance padne. [Fakt/Odhad]
5. **KONE × TKE.** Prověrka DOJ (a nejspíš EU), ~75 % plnění v akciích KONE, posunuté splacení půjčky. [Fakt]
6. **Korelace s obranou.** TKMS tvoří 34 % mcap TKA, takže přecenění obrany (CSG, RHM v listopadu, themes #eu-defense) jde rovnou do TKA. [Výpočet]
7. **Automotive a Decarbon.** Slabá poptávka, legacy projekty, nucera s vyšší ztrátou a strategickou revizí ([Quartr](https://web.quartr.com/m/sources/s83477655322)). [Fakt]
8. **Odbory a governance.** IG Metall, spolurozhodování a blokační vliv Krupp-Stiftung. [Fakt]

**Nejsilnější protiargument proti mé (opatrné) tezi:** Management za 13 měsíců dotáhl TKMS, tk accelis, HKM i KONE, tedy přesně to, co předchozí vedení roky nezvládlo. Ocel má poprvé za dekádu pohromadě podepsanou restrukturalizaci, exit z HKM, safeguards a klesající plyn (GS: TTF z ~93 na 46 EUR/MWh do 2Q27, research/log). Pokud FY26/27 ukáže 0,7–0,8 mld. EBITDA a IPO oceli vezme i penze, NAV vyskočí k ~20 EUR a dnešní cena je levná. Krupp-Stiftung spin-off podporuje a insideři nakupovali. Redukce před 8. 12. by pak byla prodej před katalyzátorem. [Názor]

## Conviction, pozice, katalyzátory a monitoring (kroky 12–13)

### Krok 12 – conviction a velikost pozice

- **Conviction: nízká až střední.** Rozptyl −56 % až +76 % (směrodatná odchylka 47 %), edge je interpretační a proti ceně slabý. Klíčová rozhodnutí jsou v rukou managementu, Krupp-Stiftung, regulátorů a odborů. [Názor]
- **Tomáš:** rámcová velikost **TKA 5–8 %**, současná **13,4 %** (`tools/portfolio.py`, 17. 11.), tedy **převážená ~2×**.
    - **Rodina thyssenkrupp:** TKA 13,4 % + TKMS 3,5 % + TKCC 0,7 % = **~17,7 %**. Je to jedna korelovaná sázka. Look-through expozice na TKMS je **~8 %** (3,5 % + 13,4 % × 0,34), na tk accelis ~2,2 %. Obrana celkem (s RHM a CSG) dělá 25 % portfolia. Rozumný strop pro celou rodinu je ~10–12 %. [Výpočet/Názor]
    - **Dopad bear scénáře:** ~−7,6 p. b. na celém portfoliu při dnešní váze, ~−4,5 p. b. při 8 %. [Výpočet]
    - **→ ⚡ Ke zvážení: redukovat TKA k ~7–8 %.** [Názor]
        - Postupně: část před 8. 12. (snižuje riziko eventu), zbytek podle výhledu 2026/27 a plánu pro ocel. Pokud 8. 12. přinese 🟢 spouštěče z Verdiktu, zbytek nechat.
        - Expozice na TKMS je čistší přímo než přes TKA s penzemi a ocelí. Malé pozice TKMS a TKCC bych neřešil.
        - Tomáš je v TKA ~+52 % v zisku. Před prodejem si zkontroluj data nákupů kvůli 3letému časovému testu (v repu je nemám).
- **Michal:** TKA nedrží.
- Nejsem finanční poradce. Tohle je podklad pro Tomášovo rozhodnutí, ne pokyn.

### Krok 13 – katalyzátory a monitoring

| Datum | Událost | Co sledovat |
|---|---|---|
| 7. 12. 2026 | TKMS FY25/26 ([Quartr](https://web.quartr.com/m/events/401365)) | marže vs. 6,5 %, Kanada, výhled, dividenda |
| **8. 12. 2026** | **TKA FY25/26 + výhled 26/27** ([Quartr](https://web.quartr.com/m/events/722119)) | Q4 FCF +1,3 až +1,6 mld., výhled FCF 26/27, ocel adj. EBITDA 26/27 (laťka 0,6 mld.), net cash 30. 9., penze, dividenda, struktura oceli, holdingové náklady, definice EBIT/EBITDA oceli |
| prosinec–leden | DOJ/EU k KONE × TKE | nápravná opatření, harmonogram |
| 5. 2. 2027 | Valná hromada | dividenda, struktura |
| 11. 2. 2027 | Q1 26/27 ([Quartr](https://web.quartr.com/m/events/735368)) | ocel s plným efektem safeguards |
| 13. 5. 2027 | Q2 26/27 ([Quartr](https://web.quartr.com/m/events/802167)) | trajektorie oceli k 0,85 mld., restrukturalizační cash-outy |
| nejdřív 2Q 2027 | Closing KONE × TKE | 0,81 mld. cash + ~44 mil. akcií KONE, lock-up, půjčka |
| 2027 | Rozhodnutí o IPO/spin-offu oceli | podíl TKA, **kolik penzí odejde**, počáteční rozvaha |
| 2027–2029 | DRI: tender na vodík, stavba | capex vs. 3 mld., termín 2029 |

**Potvrdí tezi:** výhled FCF 26/27 ≥ ~0 · ocel adj. EBITDA 26/27 ≥ 0,6 mld. · plán oddělení oceli s jejími penzemi (~2,3 mld.) · holdingová net cash ≥ 2,5 mld. k 30. 9. · KONE closing bez podstatných ústupků · holdingové náklady pod 0,15 mld.

**Vyvrátí tezi (🔴):** ocel < 0,43 mld. nebo nové provize · přečerpání nebo odklad DRI · FCF 26/27 < −0,5 mld. · konsolidovaná net cash < ~1,5 mld. · zablokování nebo výrazná změna dealu KONE · penze zůstanou v holdingu nebo holding musí oceli přidat hotovost.

**KPI pro Tracker:** adj. EBIT skupiny a segmentů · adj. EBITDA oceli (EUR/t, Mt) · FCF před M&A · net cash (konsolidovaná a holdingová) · penze · ceny TKMS, TKCC, nucera a KONE (SOTP) · diskont k NAV · stav KONE × TKE · DRI · backlog TKMS.

## Zdroje (krok 14)

Odkazy na konkrétní pasáže (Quartr sources, web) jsou u čísel v textu. Hlavní zdroje:

- **Quartr – TKA:** [firma (5770)](https://web.quartr.com/m/companies/5770) · [Q3 2025/26 event + transcript](https://web.quartr.com/m/events/556986) · [9M report 2025/26](https://web.quartr.com/m/documents/3670772) · [Q2 report](https://web.quartr.com/m/documents/3312701) · [Q1 report](https://web.quartr.com/m/documents/2807753) · [Steel CMD 28. 9. 2026](https://web.quartr.com/m/documents/4208784) · [FY 2025/26 event 8. 12.](https://web.quartr.com/m/events/722119) · roční data [FY24/25](https://web.quartr.com/m/documents/2490630), [FY23/24](https://web.quartr.com/m/documents/1785564), [FY22/23](https://web.quartr.com/m/documents/268947), [FY21/22](https://web.quartr.com/m/documents/130487)
- **Quartr – dceřinky:** [TKMS Q3 release](https://web.quartr.com/m/documents/3681765) · [TKMS 9M report](https://web.quartr.com/m/documents/3685644) · [tk accelis prezentace 10/2026](https://web.quartr.com/m/documents/4364129) · [nucera 9M](https://web.quartr.com/m/sources/s65556942833)
- **Repo:** research/log/2026-11.md (GS 13. 11. 2026) · research/themes.md (#eu-industry, #eu-energy, #eu-defense) · companies/TKA/dossier.md · `tools/portfolio.py`, `state/prices.json` (17. 11.)
- **Sell-side (web):** DB, 29. 10. 2026 ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/corporate-news/thyssenkrupp-aktie-deutsche-bank-senkt-kursziel-auf-17-euro/70433800)) · Citi, BofA, DZ, srpen 2026 ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/thyssenkrupp-s-elevator-exit-could-hand-it-3-4bn-and-a-fresh-chapter-in-its-re-rating/70023598)) · JPM, 13. 7. 2026 ([Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-jpmorgan-hebt-ziel-auf-1280-euro-927681)) · LBBW, ~9. 11. ([Finanztrends](https://www.finanztrends.de/news/thyssenkrupp-aktie-duisburger-anlage-rutscht-auf-2029/)) · konsenzus ([Börse Express](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-abspaltung-von-tk-accelis-vollzogen-960794))
- **KONE × TKE:** [Reuters přes GBAF](https://www.globalbankingandfinance.com/thyssenkrupp-line-4-billion-payday-kone-tk-elevator-deal/) · [Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/kone-agrees-buy-tk-elevator-132708315.html) · [Investment Monitor](https://www.investmentmonitor.ai/news/doj-antitrust-probe-kone-tk-elevator-deal/) · [Nordnet – KONE](https://www.nordnet.fi/markkinakatsaus/osakekurssit/16103263-kone-corporation)
- **Ocel a struktura:** [GMK Center](https://gmk.center/en/news/thyssenkrupp-prepares-steel-division-for-spin-off-ceo/) · [Der Aktionär](https://www.deraktionaer.de/nachricht/krupp-stiftungguteszeitfensterfuerverselbststaendigungvonthyssen-stahl-558238.html) · [Construction World/Reuters](https://www.constructionworld.in/amp/steel-news/jindal-steel-deal-with-thyssenkrupp-at-risk-over-pensions-and-energy/89006) · [Börsen-Zeitung](https://www.boersen-zeitung.de/unternehmen-branchen/verkauf-der-stahlsparte-von-thyssenkrupp-erneut-auf-eis) · [ad-hoc-news 13. 11.](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/thyssenkrupp-shares-retreat-as-ssab-warning-and-duisburg-delay-test-the-green-steel-story/70505809) · [Kitco – SSAB](https://www.kitco.com/news/off-the-wire/2026-10-28/ssab-tops-profit-expectations-eu-import-curbs-boost-steel-prices)
- **Ceny, insideři:** [Börse Express 18. 11.](https://www.boerse-express.com/news/articles/thyssenkrupp-aktie-guidance-fuer-stahlgeschaeft-angehoben-945280) · [StockAnalysis TKA](https://stockanalysis.com/quote/etr/TKA/statistics/) · [trend.at](https://www.trend.at/news/tk-accelis-bei-borsendebut-mit-177-milliarden-euro-bewertet) · [stock3 – nucera](https://stock3.com/aktien/thyssenkrupp-nucera-64433222) · [directors' dealings (PDF)](https://ucpcdn.thyssenkrupp.com/_binary/UCP5thyssenkruppAG/f0eb4e30-aec3-4450-ba53-c9cc8f9db1f9/Directors-Dealings-Meldung-Internet-202526-E2.pdf)
- **Neověřeno:** listopadové denní ceny (RSI je odhad) · aktuální multiples SSAB · přesný rozpad plnění z dealu KONE pro TKA a lock-up · penze připadající na TKMS a tk accelis (odhad ~0,5 mld.) · rating a splatnosti dluhopisů · přesný podíl v nucera (IR: „> 50 %“).
