# Deep dive: Aquestive Therapeutics (AQST) – 18. 11. 2026

_Claude Doc: https://claude.ai/artifact/NaAfpAtZTFi5dfKvkKobL8 · Verze v1 (první deep dive). Cena pro výpočty 3,70 USD (18. 11. 2026 vnitrodenně, `state/prices.json`). Výpočty: Python skript ve scratchpadu běhu (aqst_valuation.py), váhy: `tools/portfolio.py` k 17. 11. 2026._

## Verdikt

**Signál: ⚡ Ke zvážení: redukovat (velikost pozice před PDUFA 16. 3. 2027). Teze sama: 🟡 Sledovat.** [Názor]

- **Důvod:** Schválení Anaphylmu považuju za pravděpodobné (~75 %), ale trh ho už z velké části zaplatil. EV AQST je ~430 mil. USD, tedy prakticky stejně jako EV ARS Pharma (~433 mil. USD), která přitom bezjehlový epinefrin (neffy) už prodává za ~130 mil. USD ročně. Neffy má po dvou letech jen ~5 % trhu a firma pořád pálí hotovost. Aquestive by šla na trh jako druhá, s 75 obchodníky a s royalty zátěží (RTW, bývalí věřitelé). [Názor]
- **Scénáře (horizont ~15 měsíců, do výsledků Q4 2027 ~ únor/březen 2028):** CRL znovu 25 % → **1,00 USD** · schválení s pomalým launchem 50 % → **2,15 USD** · schválení s dobrou adopcí 25 % → **6,45 USD** · vážená cena **~2,93 USD** (−21 %, −17 % p. a.). [Odhad, výpočet v Pythonu]
- **Požadovaný výnos 25–35 % p. a.** (32–45 % za horizont) → vážený výnos je hluboko pod ním. **Buy (+50 až +100 % za 1–3 roky) to není.** Ani při optimističtějších pravděpodobnostech 15/40/45 nevychází víc než ~+5 %. Vážený výnos by se s požadovaným potkal zhruba při ceně **2,0–2,2 USD**. [Odhad]
- **Pozice:** u Tomáše 10,9 % portfolia (3. největší) v jediné binární události. Rámec pro tuhle conviction je **3–4 %**. Ke zvážení je snížit pozici ještě před PDUFA a zbytek nechat jako opci na dobrý launch. Michal AQST nedrží. [Názor]
- **Co by signál zvrátilo:** 🟢 / držet plnou velikost: schválení s čistým labelem (včetně tolerance aplikace na jazyk) dřív než 16. 3., ex-US partnerství s upfrontem ≥50 mil. USD, rychlé pokrytí plátci (≥50 % komerčních životů do 6 měsíců) nebo tržby Anaphylmu ≥25 mil. USD za první dvě celá čtvrtletí, tedy rychleji než neffy. Druhá cesta je pokles ceny k ~2,2 USD při nezměněných fundamentech. 🔴 Teze oslabena: druhé CRL, požadavek FDA na novou studii, propadnutí RTW financování (deadline 30. 6. 2027) nebo emise akcií pod ~3 USD.

_Verze v1. Cena pro výpočty 3,70 USD (18. 11. 2026 vnitrodenně), váhy z `tools/portfolio.py` k 17. 11. 2026. Plná verze v repu: `companies/AQST/deep-dive-v1.md`._

## Snapshot a kontext (kroky 0–1)

### Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor / subsektor | Specialty pharma: výroba orálních filmů (PharmFilm) pro licenční partnery + vlastní pipeline epinefrinových prodrugů (AdrenaVerse) [Fakt] | [Quartr](https://web.quartr.com/m/companies/12753), [8-K Q3](https://web.quartr.com/m/sources/s85216864243) |
| HQ, listing, ticker | Warren, New Jersey, USA (výroba v Indianě) · NASDAQ · AQST [Fakt] | [8-K Q3](https://web.quartr.com/m/sources/s83226216108) |
| Cena | 3,70 USD (18. 11. 2026 vnitrodenně) [Fakt] | `state/prices.json` (tracker) |
| 52W low–high | 2,93–7,08 USD [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/aqst/) |
| Market cap | 465 mil. USD = 3,70 × 125,69 mil. akcií k 30. 9. [Fakt, výpočet] | [8-K Q3, rozvaha](https://web.quartr.com/m/sources/s51258862134) |
| EV | ~430 mil. USD = 465 + dluh 55 − hotovost 90,3 (k 30. 9., bez royalty závazků a bez 10 mil. od Etonu z října) [Fakt, výpočet] | [10-Q Q3](https://web.quartr.com/m/events/731227) |
| Tržby TTM | 48,8 mil. USD (Q4 25–Q3 26) [Fakt, součet] | [Quartr financials](https://web.quartr.com/m/documents/4002760) |
| Marže TTM | hrubá 65 % · EBIT −114 % · čistá −162 % (obsahuje jednorázovou ztrátu 11,7 mil. ze splacení dluhu) · FCF ~−41 mil. (−84 %) [Fakt/výpočet] | [Quartr financials](https://web.quartr.com/m/documents/4002760), [8-K](https://web.quartr.com/m/sources/s61701945476) |
| Net debt / EBITDA | n/a: čistá hotovost ~35 mil. USD, EBITDA záporná (adj. EBITDA 2026 guidance −30 až −35 mil.) [Fakt] | [8-K Q3](https://web.quartr.com/m/sources/s73177524137) |
| Free float / insideři | Float 113,1 mil. ks (~90 %), insideři 3,98 %, instituce 50,6 % [Fakt] | [StockAnalysis statistics](https://stockanalysis.com/stocks/aqst/statistics/) |
| Short interest | 29,3 mil. ks (~23 % akcií, ~26 % floatu), days to cover 13,2, k 30. 10. 2026. Za rok +48 % [Fakt] | [Equibles](https://equibles.com/stocks/aqst/shortinterest) |
| CEO | Daniel Barber (CFO Ernie Toth, CCO Sherry Korczynski, dříve šéfka značky EpiPen v Mylanu) [Fakt] | [Quartr, Jefferies 16. 11.](https://web.quartr.com/m/sources/s79633192708809437160423) |
| IR | [investors.aquestive.com](https://investors.aquestive.com) | |
| Konsenzus | Strong Buy (9 analytiků), průměrný cíl 9,33 USD [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/aqst/statistics/) |
| Denní likvidita | Průměr 2,2 mil. ks/den (~8 mil. USD, ~1,8 % market capu) → **nadprůměrná** vzhledem k velikosti [Fakt, výpočet] | [Equibles](https://equibles.com/stocks/aqst/shortinterest) |
| RSI 14 | 27,1 k 19. 10. 2026 (přeprodané). Aktuální hodnotu se nepodařilo ověřit [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/aqst/statistics/) |

### Krok 1 – zdroj a kontext idey

- **Zdroj:** stávající pozice z Quartr watchlistu. eToro 36,65 ks za 4,12 USD (otevřeno 21. 10. 2026) a T212 154,9 ks za 3,13 USD, vážený průměr 3,32 USD, nerealizovaně +11,5 % (`config/portfolio.yaml`, `tools/portfolio.py`). [Fakt]
- **Proč je cena tam, kde je:**
    - Původní NDA Anaphylmu FDA v lednu 2026 odmítla (CRL z 30. 1. 2026). Výhrady se týkaly jen balení a návodu: v human factors studii měli lidé problém otevřít sáček a film si někteří dávali na jazyk místo pod něj. Účinnost ani výrobu FDA nezpochybnila. Akcie paradoxně vyskočila z ~2,95 na ~4,1–4,3 USD, protože trh čekal horší CRL. [Fakt] ([Benzinga](https://www.benzinga.com/news/fda/26/02/50309975/whats-going-on-with-aquestive-therapeutics-stock-after-fda-update-for-lead-allergic-treatment), [Parameter](https://parameter.io/aquestive-therapeutics-aqst-stock-fda-rejects-allergy-treatment-over-packaging-concerns))
    - Resubmise proběhla 16. 9. 2026. FDA ji 15. 10. přijala jako **Class 2** (šestiměsíční review, PDUFA 16. 3. 2027). Akcie během dvou dnů spadla ze 4,61 na 3,78 USD (−18 %), protože trh doufal v kratší Class 1. [Fakt] ([8-K Q3](https://web.quartr.com/m/sources/s83226216108), [StockAnalysis historie](https://stockanalysis.com/stocks/aqst/history/))
    - Slabé Q3 (tržby 7,6 mil., −41 % y/y kvůli načasování objednávek Suboxone), short interest na ročním maximu a vlažná čísla neffy (Q3 jen +7 % y/y). [Fakt] ([8-K](https://web.quartr.com/m/sources/s73177524137), [ARS Q3](https://www.biospace.com/press-releases/ars-pharma-reports-business-highlights-and-third-quarter-2026-financial-results))
- **Trh:** v USA je podle firmy 30–40 mil. lidí s rizikem anafylaxe, ale předepisuje se jen ~5–5,5 mil. receptů ročně (růst mid-single digit). Firma čeká 7,5 mil. receptů a trh ~2 mld. USD v roce 2029 při cenách značkových produktů. To je projekce managementu [Odhad]. Dominují generické autoinjektory (150–350 USD za 2 ks), dále EpiPen a Auvi-Q. Neffy (nosní sprej, ARS Pharma) je od 8/2024 první bezjehlová alternativa. ([Quartr, Jefferies](https://web.quartr.com/m/sources/s85946548797285570209512), [Quartr](https://web.quartr.com/m/sources/s67238953817051599212465), [Medfinder](https://www.medfinder.com/blog/how-to-help-patients-save-money-on-neffy-providers-guide))

## Teze a variant perception (krok 2)

- **Co si myslí trh (sell-side):** 9 analytiků má Strong Buy s cílem ~9,33 USD. Anaphylm je podle nich „lepší neffy“: nejrychlejší absorpce (Tmax 12 min vs. 20 min u autoinjektoru), lepší farmakodynamika a forma velikosti poštovní známky, ve které 51 z 53 lidí preferovalo film před sprejem. Po schválení prý přijde přecenění. [Fakt: ratingy; tvrzení o produktu podle firmy] ([StockAnalysis](https://stockanalysis.com/stocks/aqst/statistics/), [Quartr, Jefferies](https://web.quartr.com/m/sources/s50888518562205277733577))
- **Co si myslí shorti:** short interest ~26 % floatu sází na druhé CRL, ředění nebo pomalý launch. [Fakt: data; motivace: Názor]
- **Můj pohled:** schválení je pravděpodobnější, než shorti tvrdí (~75 %). CRL bylo úzké a review se má týkat jen CRL položek. Upside po schválení je ale **mnohem menší, než naznačuje sell-side**, protože:
    1. **Benchmark neffy:** první celý rok 72,2 mil. USD, 2026 ~110–115 mil. při masivní DTC kampani, podíl na trhu 5 % (9 % v targetovaných ordinacích). ARS po škrtech v marketingu stále prodělává. [Fakt] ([ARS FY25](https://www.biospace.com/press-releases/ars-pharmaceuticals-reports-fourth-quarter-and-full-year-2025-financial-results-and-updates-on-neffy-epinephrine-nasal-spray-commercialization), [ARS Q3](https://www.biospace.com/press-releases/ars-pharma-reports-business-highlights-and-third-quarter-2026-financial-results))
    2. **Ocenění peera:** SPRY má EV ~433 mil. USD, tedy ~3,7–3,9× TTM tržeb. AQST má EV ~430 mil. USD bez schváleného produktu. Po odečtení PharmFilm byznysu (~1,5× tržby ≈ 68 mil.) trh za Anaphylm platí ~360 mil. USD, tj. ~84 % EV firmy, která už neffy prodává. [Fakt/výpočet] ([StockAnalysis SPRY](https://stockanalysis.com/stocks/spry/statistics/))
    3. **Ekonomika launche:** 75 reps, ~8 000–8 500 cílových lékařů (30–35 % trhu), cena zatím neoznámená, plátci budou chtít zdůvodnit prémii proti generikům. Z tržeb odchází royalty RTW (tiered single-digit) a bývalým věřitelům. [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s52370292147050748450181), [Santelog/RTW PR](https://www.santelog.com/actualites-sante-nasdaq/aquestive-therapeutics-announces-75m-strategic-funding-agreement-rtw-support))
- **Teze v jedné větě:** _Anaphylm bude spíš schválen, ale druhý bezjehlový epinefrin na trhu, kde první po dvou letech drží 5 %, nevydělá na přecenění, které trh a sell-side čekají. Riziko/výnos k PDUFA je asymetrické dolů a 10,9 % portfolia je na binární událost moc._ [Názor]
- **Proč by se trh mohl mýlit:** sell-side modely stojí na peak sales ~500 mil.+ a diskontech kolem 10 %. Tržní cena SPRY ukazuje, že investoři reálnou adopci bezjehlového epinefrinu dnes oceňují mnohem střízlivěji. [Názor]

## Byznys model, pipeline a KPI (krok 3)

### Byznys model

- **PharmFilm (dnešní tržby):** exkluzivní výroba filmů pro partnery: Suboxone (Indivior), Sympazan (Cosette), Ondif (Hypera, Brazílie), Emylif (Zambon, EU). V Q3 vyrobili 26 mil. dávek (44 mil. y/y), za 9M 107 mil. (108 mil.). Tržby z výroby za 9M 27,4 mil., licence a royalty 7,5 mil. (z toho jednorázových 5 mil. od Zevry). [Fakt] ([8-K](https://web.quartr.com/m/sources/s61921036673), [Quartr Q3 call](https://web.quartr.com/m/sources/s48485844732543587712419))
- **Koncentrace:** Indivior ~67 % a Zevra ~14 % tržeb za 9M. Značkový Suboxone drží ~25 % trhu filmů a dlouhodobě ztrácí podíl ve prospěch generik. [Fakt] ([10-Q summary](https://web.quartr.com/m/events/731227))
- **Moat:** know-how a 100+ patentů v orálních filmech, americká výroba (necitlivá na cla), u Anaphylmu prodrug (dibutepinefrin), který obchází vazokonstrikci epinefrinu. Moat výroby je reálný, ale malý. Moat Anaphylmu stojí na patentech a na tom, jestli lékaři a plátci uznají klinickou výhodu. [Fakt/Názor] ([Quartr, Jefferies](https://web.quartr.com/m/sources/s79633192708809437160423))
- **Reporting:** jeden segment, tržby rozdělené na manufacture & supply, license & royalty a co-development. [Fakt] ([10-Q summary](https://web.quartr.com/m/events/731227))

### Pipeline s pravděpodobnostmi

| Program | Stav | Další milník | P(úspěch) | Zdroj stavu |
|---|---|---|---|---|
| Anaphylm (US) | NDA resubmise, Class 2 | PDUFA 16. 3. 2027 | ~75 % do PDUFA, ~85 % kdykoliv [Odhad] | [8-K](https://web.quartr.com/m/sources/s83226216108) |
| Anaphylm (Kanada / EU / UK) | příprava podání | Kanada Q4 2026, EU Q1 2027, UK Q2 2027, hledá se partner | ~60 % do 2028 [Odhad] | [Quartr, Jefferies](https://web.quartr.com/m/sources/s60118850234760706283285) |
| Libervant (licence Eton) | tentativní schválení | exkluzivita Valtoca končí 10. 1. 2027, PDUFA 23. 3. 2027 (12+ let) a 29. 3. 2027 (6–11 let) | ~90 % [Odhad] | [8-K](https://web.quartr.com/m/sources/s61921036673) |
| AQST-108 (atopická dermatitida, gel) | po fázi 1 | další klinika od Q1 2027 | ~5–10 % na schválení [Odhad] | [8-K](https://web.quartr.com/m/sources/s61921036673) |
| AdrenaVerse (~20 prodrugů) | preklinika | proof of concept v 2027 | opce [Názor] | [Quartr Q3 call](https://web.quartr.com/m/sources/s88528410791848278108356) |

- **Libervant ekonomika:** 10 mil. USD upfront (přišlo v říjnu), až 47,5 mil. v milnících, mid-teens royalty a 20letá dodavatelská smlouva. Pro hodnotu firmy je to spíš bonus. [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s87026518969032368401067))

### Cash runway

- Hotovost 90,3 mil. USD k 30. 9. Firma čeká na konci 2026 >70 mil. včetně 10 mil. od Etonu, bez RTW a Oaktree. [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s56917044335210341427340))
- Při schválení přijde 75 mil. od RTW (podmínka: schválení do 30. 6. 2027) a 20 mil. z Oaktree, celkem „necelých 200 mil.“ na launch. K tomu ATM ~73 mil. (nevyčerpané k 30. 9.). [Fakt] ([Quartr, Jefferies](https://web.quartr.com/m/sources/s75644056632894144972610), [10-Q summary](https://web.quartr.com/m/events/731227))
- **Můj odhad:** bez schválení dojde hotovost zhruba v Q1 2028 (burn ~45 mil./rok), takže by bylo nutné ředění. Se schválením a launchem je spotřeba v 2027 ~70 mil. Základní scénář je financovaný do 2028, pomalý launch by si vyžádal emisi kolem 75 mil. [Odhad, model]

### Produkt a ohlasy

- Silné stránky: odolnost (nezmrzne, snese >65 °C, voda), nosí se v peněžence, rychlá absorpce, FDA podle firmy nevidí vyšší kardiovaskulární riziko než u autoinjektoru. Povědomí mezi alergology je ~85 %. [Fakt podle firmy] ([Quartr, Jefferies](https://web.quartr.com/m/sources/s63986934051172610781010), [Quartr](https://web.quartr.com/m/sources/s75342688067079890556864))
- Slabiny: na jazyku (místo pod jazykem) je PK nižší, i když nad terapeutickým prahem. Analytici se ptají, jestli výrazný nárůst tlaku není „přestřelený“. Chybí klinické endpointy, je to PK/PD registrace, stejně jako u neffy. [Fakt] ([Quartr](https://web.quartr.com/m/sources/s50427613174466203192176), [Quartr Q&A](https://web.quartr.com/m/sources/s70711130681419315509612))

### KPI (podle sektoru)

- Rozhodnutí FDA a label (sublinguálně / na jazyk, váha ≥30 kg) · % pokrytých životů a kvalita pokrytí · TRx Anaphylmu v targetovaných ordinacích · tržby za Anaphylm vs. křivka neffy · cash a burn · čerpání ATM · tržby PharmFilm (Suboxone) · neffy jako benchmark trhu. Management sám slíbil reportovat plátce, uptake u navštívených lékařů a efektivitu výdajů. [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s71980410968107514022687))

## Finance, cash runway, rozvaha a governance (kroky 4–7)

### Krok 4 – finance

| Rok | Tržby (mil. USD) | Hrubý zisk | EBIT | Čistý zisk | Provozní CF |
|---|---|---|---|---|---|
| 2022 | 47,7 | 28,3 | −42,1 | −54,4 | −9,8 |
| 2023 | 50,6 | 29,8 | −15,1 | −7,9 | −6,4 |
| 2024 | 57,6 | 39,7 | −30,8 | −44,1 | −35,8 |
| 2025 | 44,5 | 26,0 | −71,1 | −83,8 | −52,4 |
| 9M 2026 | 35,8 | 24,7 | −26,9 | −47,4 | −31,3 |

Zdroj: [Quartr financials FY](https://web.quartr.com/m/documents/2993053), [FY24](https://web.quartr.com/m/documents/1863213), [8-K Q3](https://web.quartr.com/m/sources/s61701945476). [Fakt]

- **Tržby Q3 2026: 7,557 mil. USD.** Ověřeno v 8-K (dokument 4002761). Číslo 13,0 mil., které se objevilo v jiném zdroji, jsou ve skutečnosti tržby **Q4 2025** (13,015 mil.), tedy záměna období. [Fakt] ([8-K](https://web.quartr.com/m/sources/s61701945476), [Quartr Q4 25](https://web.quartr.com/m/documents/2992997))
- **Kvalita čísel:** tržby jsou 15 let ploché (45–58 mil.) a kolísají podle objednávek Suboxone. 9M 2026 obsahuje jednorázových 5 mil. od Zevry. Bez nich by 9M tržby byly ~30,8 mil., tedy −2 % y/y. Guidance 2026 je 46–50 mil., takže Q4 by měl mít ~10–14 mil. [Fakt/výpočet] ([Quartr Q3 call](https://web.quartr.com/m/sources/s48485844732543587712419))
- **Přechodné vs. strukturální:** propad Q3 je načasování (Suboxone 9M y/y nahoru). Strukturální je pomalá eroze Suboxone a SG&A, které po launchi vyskočí (Q4 2025 mělo SG&A 32,8 mil. při přípravě na původní PDUFA). [Fakt/Názor] ([Quartr](https://web.quartr.com/m/sources/s87068116563601921889728), [Quartr Q4 25](https://web.quartr.com/m/documents/2992997))
- **Jednorázové položky:** ztráta 11,7 mil. ze splacení 13,5% notes (9M 2026). Bez ní by čistá ztráta 9M byla 35,7 mil. Adj. EBITDA 9M −19,2 mil. vs. −35,5 mil. [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s54039807717723903320630))

### Krok 5 – alokace kapitálu

- Žádné dividendy ani buybacky. Kapitál jde do launche Anaphylmu, ex-US regulace a selektivně do AdrenaVerse. Libervant se místo vlastního launche vylicencoval, což je kapitálově rozumné. [Fakt/Názor] ([Quartr Q3 call](https://web.quartr.com/m/sources/s81639522740211058600543))
- Historicky se financovali drahým dluhem (13,5% notes s royalty), monetizací royalty a emisemi. Počet akcií vzrostl z 91 mil. (Q4 2024) na 125,7 mil. (Q3 2026), tj. **+37 % za necelé dva roky**. V 9M 2026 přes ATM jen 4,7 mil. USD. [Fakt] ([Quartr financials](https://web.quartr.com/m/documents/4002760), [10-Q summary](https://web.quartr.com/m/events/731227))

### Krok 6 – rozvaha

- **Dluh:** Oaktree term loan **55 mil. USD** (květen 2026), splatnost 12. 5. 2031, bez splátek jistiny. Celý rámec je až 150 mil., z toho 95 mil. delayed draw za podmínek (20 mil. po schválení). Úrok z výkazu vychází ~13 % p. a. (1,85 mil. za Q3). [Fakt; sazba: Odhad] ([10-Q summary](https://web.quartr.com/m/events/731227), [8-K](https://web.quartr.com/m/sources/s61701945476))
- **Royalty závazky:** 28,9 mil. (royalty z Anaphylmu a Libervantu bývalým věřitelům, trvají i po splacení notes, platby až do 2035) a 62,2 mil. závazek z dřívějšího prodeje budoucích tržeb. Většinou jde o účetní/nevratné položky, ale snižují budoucí cash flow. [Fakt] ([8-K rozvaha](https://web.quartr.com/m/sources/s51258862134), [10-Q summary](https://web.quartr.com/m/events/731227))
- **RTW (75 mil.):** nejde o equity, ale o royalty financování. RTW dostane tiered single-digit % z US tržeb Anaphylmu, s capem. Peníze přijdou jen při schválení. [Fakt] ([Santelog/PR 14. 8. 2025](https://www.santelog.com/actualites-sante-nasdaq/aquestive-therapeutics-announces-75m-strategic-funding-agreement-rtw-support))
- Vlastní kapitál −70,8 mil. USD, akumulovaná ztráta 494 mil. (velké NOL, daně dlouho nulové). Net debt / EBITDA n/a (čistá hotovost ~35 mil. k 30. 9.). [Fakt] ([8-K](https://web.quartr.com/m/sources/s51258862134))
- **Ředění:** 250 mil. autorizovaných akcií, ATM ~73 mil. USD. Při 3,70 USD by plné čerpání ATM znamenalo ~20 mil. akcií (+16 %). [Fakt/výpočet]

### Krok 7 – vlastnictví a governance

- Žádný kontrolující akcionář, instituce ~51 %, insideři ~4 %. [Fakt] ([StockAnalysis](https://stockanalysis.com/stocks/aqst/statistics/))
- **Insider trading:** CEO Barber prodal 16. 9. 2026 25 000 ks (~120 tis. USD) a další prodeje proběhly 16. 10. Uplatnění opcí s ponecháním akcií (CEO 9. 9., CPO 10. 9.). Ředitel nakoupil 12. 11. (objem skrytý). Čisté informativní prodeje za 3 měsíce ~164 tis. USD, skóre neutrální. Malé částky, žádný silný signál. [Fakt] ([TipRanks](https://www.tipranks.com/stocks/aqst/insider-trading))
- **Spory:** probíhají žaloby kolem Suboxone (product liability) a hromadná žaloba akcionářů. [Fakt] ([10-Q summary](https://web.quartr.com/m/events/731227))
- **Track record managementu:** v 2026 splnili, co slíbili (resubmise do Q3, licence Libervantu, refinancování, hotovost >70 mil.). [Fakt] ([Quartr Q3 call](https://web.quartr.com/m/sources/s72514221010221301637236)) Historicky ale opakovaná zdržení: Libervant roky blokovaný exkluzivitou Valtoca a CRL Anaphylmu kvůli balení, tedy chyba v human factors, které se dalo předejít. [Názor]
- Nový člen boardu Rich Daly (od 14. 10. 2026), změna auditora nezjištěna. [Fakt] ([StockAnalysis news](https://stockanalysis.com/stocks/aqst/))

## Požadovaný výnos a valuace (kroky 8–9)

### Krok 8 – požadovaný výnos

- **Baseline:** pasivní alternativa (S&P 500 / ACWI) ~8–9 % p. a. [Odhad]
- **Rizikové faktory AQST:**
    1. **Binární PDUFA 16. 3. 2027** (zvyšuje, výrazně): druhé CRL by znamenalo nejen zpoždění, ale i ztrátu 75 mil. od RTW (deadline 30. 6. 2027) a nutnou emisi za nízkou cenu.
    2. **Komerční adopce vs. neffy** (zvyšuje): přímý precedent ukazuje pomalou adopci a drahý launch. Aquestive má menší sílu (75 reps) a vstupuje jako druhá. Plusem je CCO s historií EpiPenu.
    3. **Financování, ředění a royalty stack** (zvyšuje): Oaktree ~13 %, royalty RTW i bývalým věřitelům, ATM 73 mil., záporný vlastní kapitál, počet akcií +37 % za 2 roky.
    4. **Koncentrace dnešních tržeb** (zvyšuje mírně): Indivior 67 %, Suboxone dlouhodobě klesá.
    5. **Likvidita a struktura** (snižuje mírně): vysoká likvidita a PharmFilm byznys, který dává částečnou podlahu. Short interest 26 % floatu zvyšuje volatilitu oběma směry.
- **Závěr:** u pre-commercial biotechu s jedním aktivem a binární událostí do 4 měsíců, navíc s nutností financovat launch, je rozumná požadovaná návratnost **25–35 % p. a.** Spodní hranice platí, pokud by schválení bylo jisté a šlo jen o launch, horní pro dnešní stav s regulatorním i komerčním rizikem. [Názor]
- **Horizont:** ~15 měsíců. PDUFA 16. 3. 2027, pak 2–3 čtvrtletí launch dat (plátci, TRx). Teze se potvrdí nebo vyvrátí s výsledky Q4 2027 (~únor/březen 2028). [Odhad]

### Krok 9 – valuace

**Metoda:** cílová cena k horizontu = 50 % DCF (diskont 12,5 %, FCF 2028–2045, LOE Anaphylmu ~2038, pak −30 %/rok) + 50 % EV/sales na tržby 2028E (peer SPRY 3,7–3,9× TTM). Model: COGS Anaphylmu 12 %, royalty stack 7 %, centrální náklady 32 mil./rok, PharmFilm příspěvek 25 mil./rok (−3 %/rok), NOL 480 mil. Hotovost na konci 2027 = 70 (YE26) + RTW 75 + Oaktree 20 + FCF 2027 (+ případná emise). [Odhad, Python]

**Launch křivka podle neffy** (US net sales, mil. USD): neffy rok 1 = 72,2, rok 2 ≈ 110–115 ([ARS FY25](https://www.biospace.com/press-releases/ars-pharmaceuticals-reports-fourth-quarter-and-full-year-2025-financial-results-and-updates-on-neffy-epinephrine-nasal-spray-commercialization), [ARS Q3](https://www.biospace.com/press-releases/ars-pharma-reports-business-highlights-and-third-quarter-2026-financial-results)).

| Anaphylm | 2027 | 2028 | 2029 | 2030 | 2031 | Peak | vs. neffy rok 2 |
|---|---|---|---|---|---|---|---|
| Pomalý launch | 15 | 55 | 100 | 135 | 155 | 170 | ~50 % |
| Dobrá adopce | 35 | 125 | 230 | 320 | 380 | 400 | ~110 % |

**Tři scénáře (cíl k ~2/2028):**

| Scénář | P | Cíl | Klíčové předpoklady |
|---|---|---|---|
| CRL znovu | 25 % | **1,00 USD** | RTW i Oaktree draw padají, emise 60 mil. @1,20 (+50 mil. ks), PharmFilm 1,5× tržby, Anaphylm jako opce (45 % pozdějšího schválení, silný diskont) |
| Schválení, pomalý launch | 50 % | **2,15 USD** | peak 170 mil. (~6 % trhu), DCF 1,82 / EV/sales 3,0× → 2,46, emise 75 mil. @2,50 (+30 mil. ks) |
| Schválení, dobrá adopce | 25 % | **6,45 USD** | peak 400 mil. (~12–15 % trhu, víc než neffy), DCF 6,84 / EV/sales 4,5× → 6,02, bez emise |
| **Vážená cena** | | **2,93 USD** | **−21 % celkem, −17 % p. a.** |

[Odhad, výpočet v Pythonu]

- **rNPV dnes:** vážená cena diskontovaná požadovanými 25–35 % p. a. dává **~2,0–2,2 USD na akcii** proti ceně 3,70. Trh tedy implicitně počítá s vyšší pravděpodobností dobré adopce nebo s nižším diskontem. [Odhad]
- **Citlivost (vážená cena):**

| P(schválení) \ podíl dobré adopce | 25 % | 33 % | 50 % |
|---|---|---|---|
| 65 % | 2,44 (−34 %) | 2,66 (−28 %) | 3,14 (−15 %) |
| 75 % | 2,66 (−28 %) | 2,92 (−21 %) | 3,47 (−6 %) |
| 85 % | 2,88 (−22 %) | 3,17 (−14 %) | 3,79 (+3 %) |

- **Reverse pohled:** aby dnešní cena dávala požadovaných 25 % p. a., musela by vážená cena být ~4,9 USD. To by vyžadovalo, aby dobrá adopce (víc než neffy) byla základní scénář s pravděpodobností >60 %. Nebo peak sales ~500 mil.+, se kterými pracuje sell-side (cíl 9,33). [Odhad]
- **EV/sales vs. peers:** AQST 8,8× TTM tržeb (EV 430 / 48,8) vs. SPRY 3,7–3,9×. Na peak sales: 3,7× (pomalý) / 1,1× (dobrý). [Fakt/výpočet] ([StockAnalysis SPRY](https://stockanalysis.com/stocks/spry/statistics/))
- **Ředění je v cílech započtené:** +5 mil. opcí/RSU ve všech scénářích, plus emise v CRL a pomalém scénáři. [Odhad]
- **Upside mimo model:** převzetí (big pharma by mohla platit 4–6× peak sales) nebo ex-US partnerství s velkým upfrontem. To je hlavní důvod, proč nedoporučuju vystoupit úplně. [Názor]
- **Vážený vs. požadovaný:** −17 % p. a. vs. 25–35 % p. a. → **nesplňuje** požadovaný výnos ani definici Buy. [Odhad]

## Base rate, rizika a protiargument (kroky 10–11)

### Krok 10 – base rate

- **Neffy:** CRL v září 2023 (FDA chtěla studii s opakovanou dávkou), schválení v srpnu 2024 po resubmisi. Po schválení ale neffy rostla pomaleji, než trh čekal: 5 % podílu po dvou letech a akcie SPRY je dnes ~4 USD. To je nejbližší precedent pro obě fáze, regulatorní i komerční. [Fakt] ([Healio](https://cm.healio.com/news/allergy-asthma/20230920/fda-asks-ars-pharma-for-more-testing-in-epinephrine-nasal-spray-approval-process), [Drug Topics](https://www.drugtopics.com/view/fda-approves-first-needle-free-epinephrine-nasal-spray), [StockAnalysis SPRY](https://stockanalysis.com/stocks/spry/statistics/))
- **CRL kvůli human factors / balení bez otázek k účinnosti:** takové CRL bývají řešitelné a resubmise mají obvykle vyšší šanci než CRL kvůli účinnosti. Přesto počítám 75 %, ne 90 %: FDA v 2026 bývá nevyzpytatelná a placement „na jazyk“ je skutečné riziko pro bezpečnost v nouzi. [Odhad/Názor]
- **Malé firmy s jedním produktem, které launchují samy do trhu s generiky** (Aquestive sama s Libervantem a Sympazanem, řada specialty pharma): typicky pomalý ramp, ředění a často prodej nebo licence. Base rate pro „dobrou adopci“ je pod 30 %. [Názor]

### Krok 11 – rizika (podle závažnosti)

1. **Druhé CRL nebo zpoždění** (25 %): pád k ~1 USD, ztráta RTW, emise. Dopad −70 %.
2. **Pomalý launch / slabé pokrytí plátci:** neffy ukazuje, že i s lepší formou to trvá roky. Pomalý launch skončí emisí kolem 2,5 USD.
3. **Ředění a drahé financování:** ATM 73 mil., Oaktree ~13 %, royalty stack 7 % tržeb. [Odhad]
4. **Konkurence:** neffy (náskok 2,5 roku, 44 000+ předepisujících), levná generika, EpiPen, Auvi-Q a další bezjehlové formy ve vývoji. [Fakt: neffy čísla] ([ARS Q3](https://www.biospace.com/press-releases/ars-pharma-reports-business-highlights-and-third-quarter-2026-financial-results))
5. **Eroze Suboxone a koncentrace na Indivior** (67 % tržeb).
6. **Label:** omezení (např. jen ≥30 kg, bez dětí) nebo varování by zmenšilo trh. Pediatrie je klíčová část receptů. [Názor]
7. **Soudní spory** (Suboxone, akcionáři).

**Nejsilnější protiargument proti mému (medvědímu) pohledu:** Anaphylm může být reálně lepší produkt než neffy: pohodlnější nošení, silnější PD a jasná preference pacientů. Trh epinefrinu je navíc výrazně nedopenetrovaný (5 mil. receptů vs. 30–40 mil. ohrožených). Pokud plátci přijmou HEOR argument (méně ER návštěv), může Anaphylm překonat neffy a s 26% short interestem by squeeze po schválení vystřelil akcii nad 6 USD rychle. K tomu opcionalita převzetí a ex-US partnerství. Proto redukovat, ne vystoupit. [Názor]

## Conviction, pozice, katalyzátory a monitoring (kroky 12–13)

### Krok 12 – conviction a velikost pozice

- **Conviction: střední** (v medvědím pohledu). Edge z kroku 2 je jasná a podložená tržními daty (SPRY, neffy), ale rozptyl scénářů je extrémní: 1,00 až 6,45 USD, tedy −73 % až +74 %. [Názor]
- **Rámec:** binární biotech s váženým výnosem pod požadovaným patří maximálně do **3–4 % portfolia** jako opce na pozitivní překvapení. [Názor]
- **Současná váha u Tomáše: 10,9 %** (15 722 CZK, 3. největší pozice; `tools/portfolio.py` k 17. 11. 2026). → **Výrazně převážená**, zhruba 3× rámec. Při druhém CRL by sama tahle pozice vzala portfoliu ~8 %. [Fakt/výpočet]
- **Ke zvážení:** snížit k ~3–4 % před PDUFA (prodat zhruba 60–70 % pozice; u T212 jsou kusy s nákupkou 3,13 USD v zisku, eToro 4,12 USD ve ztrátě). Zbytek držet přes PDUFA. Při ceně ~2,0–2,2 USD a nezměněných fundamentech by se poměr výnos/riziko vyrovnal a dalo by se přikoupit. [Názor]
- Farmacie & biotech tvoří u Tomáše 19 % portfolia (AQST + IOVA + NOVO + PFE + GUTS), takže koncentrace binárních biotech rizik je vysoká. [Fakt] (`tools/portfolio.py`)
- **Michal:** nedrží, beze změny. [Fakt]

### Krok 13 – katalyzátory a monitoring

| Datum | Událost | Proč na tom záleží |
|---|---|---|
| do 31. 12. 2026 | podání v Kanadě (Health Canada) | první ex-US krok, předpoklad partnerství |
| 10. 1. 2027 | konec exkluzivity Valtoca | otevírá finální schválení Libervantu |
| ~březen 2027 | výsledky Q4 2026 | cash >70 mil.? čerpání ATM? |
| Q1 2027 | podání v EU, start kliniky AQST-108 | ex-US hodnota, pipeline |
| **16. 3. 2027** | **PDUFA Anaphylm** | **binární událost, podmínka RTW 75 mil.** |
| 23. 3. a 29. 3. 2027 | PDUFA Libervant (12+ / 6–11 let) | milníky od Etonu |
| Q2 2027 | podání v UK, US launch (při schválení) | start křivky |
| 30. 6. 2027 | deadline schválení pro RTW | při skluzu ztráta financování |
| Q2–Q4 2027 | čtvrtletní data: pokrytí plátci, TRx, tržby | test proti křivce neffy |
| čtvrtletně | výsledky ARS Pharma (neffy) | benchmark trhu |

- **Potvrdí (bull):** schválení s čistým labelem; ≥50 % komerčních životů do 6 měsíců; Anaphylm ≥25 mil. USD za první dvě celá čtvrtletí; ex-US partner s upfrontem ≥50 mil.; launch bez emise.
- **Vyvrátí (bull) / potvrdí můj medvědí pohled:** druhé CRL nebo požadavek na studii; restriktivní label; pokrytí <30 % po 6 měsících; tržby <10 mil. za první dvě čtvrtletí; emise pod 3 USD; neffy stagnuje.
- **KPI do dossieru:** stav review FDA, label, % pokrytých životů, TRx/tržby Anaphylmu vs. neffy, hotovost a burn, čerpání ATM, tržby PharmFilm a Suboxone, short interest.

## Zdroje (krok 14)

- Quartr: [profil firmy](https://web.quartr.com/m/companies/12753) · [8-K Q3 2026 (4002761)](https://web.quartr.com/m/documents/4002761) · [10-Q Q3 2026 (4002760)](https://web.quartr.com/m/documents/4002760) · [Q3 2026 event a summary](https://web.quartr.com/m/events/731227) · [Q3 2026 transcript](https://web.quartr.com/m/documents/4448935) · [Jefferies Healthcare Conference 16. 11. 2026, transcript](https://web.quartr.com/m/documents/4637196) · [Quartr financials FY2025](https://web.quartr.com/m/documents/2993053) · [FY2024](https://web.quartr.com/m/documents/1863213) · [Q4 2025](https://web.quartr.com/m/documents/2992997)
- ARS Pharma (neffy): [Q3 2026 výsledky](https://www.biospace.com/press-releases/ars-pharma-reports-business-highlights-and-third-quarter-2026-financial-results) · [FY2025 výsledky](https://www.biospace.com/press-releases/ars-pharmaceuticals-reports-fourth-quarter-and-full-year-2025-financial-results-and-updates-on-neffy-epinephrine-nasal-spray-commercialization) · [SPRY statistiky](https://stockanalysis.com/stocks/spry/statistics/) · [CRL neffy 9/2023 (Healio)](https://cm.healio.com/news/allergy-asthma/20230920/fda-asks-ars-pharma-for-more-testing-in-epinephrine-nasal-spray-approval-process) · [schválení 8/2024 (Drug Topics)](https://www.drugtopics.com/view/fda-approves-first-needle-free-epinephrine-nasal-spray)
- Tržní data AQST: [StockAnalysis přehled](https://stockanalysis.com/stocks/aqst/) · [statistiky](https://stockanalysis.com/stocks/aqst/statistics/) · [historie cen](https://stockanalysis.com/stocks/aqst/history/) · [Equibles short interest](https://equibles.com/stocks/aqst/shortinterest) · [TipRanks insider trading](https://www.tipranks.com/stocks/aqst/insider-trading)
- CRL Anaphylm: [Benzinga 2/2026](https://www.benzinga.com/news/fda/26/02/50309975/whats-going-on-with-aquestive-therapeutics-stock-after-fda-update-for-lead-allergic-treatment) · [Parameter 2/2026](https://parameter.io/aquestive-therapeutics-aqst-stock-fda-rejects-allergy-treatment-over-packaging-concerns)
- Financování: [RTW 75 mil., PR 14. 8. 2025 (Santelog)](https://www.santelog.com/actualites-sante-nasdaq/aquestive-therapeutics-announces-75m-strategic-funding-agreement-rtw-support)
- Ceny konkurence: [Medfinder, ceny neffy/EpiPen/Auvi-Q](https://www.medfinder.com/blog/how-to-help-patients-save-money-on-neffy-providers-guide)
- Interní: `config/portfolio.yaml`, `tools/portfolio.py` (17. 11. 2026), `state/prices.json`, `state/calendar.md` (Jefferies 16. 11. 2026)
- Výpočty: Python skript aqst_valuation.py (scratchpad běhu, mimo repo)
