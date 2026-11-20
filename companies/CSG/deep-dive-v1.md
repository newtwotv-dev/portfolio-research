# Deep dive: Czechoslovak Group (CSG) – 20. 11. 2026

_Claude Doc: https://claude.ai/artifact/BKYryLXPMitFSxrbgMBk3K · Verze v1 (první deep dive). Cena pro výpočty **9,32 EUR** (Euronext Amsterdam, close 19. 11. 2026 podle patria.cz, nepotvrzený close, `state/prices.json`). Close 20. 11. v době analýzy ještě nebyl: Börse Stuttgart 20. 11. ve 13:46 ukazovala **8,86 EUR (−4,9 %)** ([boerse.de](https://www.boerse.de/aktien/CSG-NV-Aktie/NL0015073TS8)). Váhy z `tools/portfolio.py` k 19. 11. Výpočty (multiples, reverse DCF, DCF, scénáře): `csg_valuation.py` ve scratchpadu běhu (`scratchpad/csg/`), výstup v `csg_valuation_output.txt`. Analýza je „před guidance 2027 a před lock-upem“._

## Verdikt

**Signál: 🟡 Sledovat (držet, nepřikupovat). Původní IPO teze (marže 26–28 %, růst „mid-teens“) je 🔴 oslabená, nová teze zní „levná, ale nedokázaná“.** [Názor]

- **Důvod:** Za 9,32 EUR trh platí ~7,8× upravené EV/EBIT 2026E a ~10× P/E 2026E (JPM EPS 0,92), tedy zhruba polovinu násobků evropských peers. Reverse DCF při rozumné cestě tržeb implikuje **trvalou EBIT marži ~18 %**, pod letošními ~21 % a hluboko pod cílem managementu 26–28 %. Cíl 26–28 % ale nevěřím ani já: Land Systems tvoří 57 % backlogu s marží 15–18 %, takže na 26 % by munice musela mít ~39 % (výpočet v kroku 2). Moje base je ~21 % v 2028. Cena je tedy pesimistická, jenže na hrozbu, kterou zatím nikdo nevyvrátil: Q3 book-to-bill 0,6, od dubna žádná velká objednávka M/L munice (JPM, 12. 11.) a Bernstein (19. 11.) čeká doplňování zásob NATO jen ~3 roky. [Odhad/Názor, výpočet v Pythonu]
- **Scénáře (horizont ~1,4 roku, do 31. 3. 2028 = po výsledcích FY2027):**
    - Bear 35 % → **5,43 EUR** (−42 %)
    - Base 45 % → **12,59 EUR** (+35 %, vč. dividendy 0,30)
    - Bull 20 % → **22,26 EUR** (+139 %)
    - vážená hodnota **12,02 EUR → +29 % za horizont, ~21 % p. a.** Směrodatná odchylka výnosu je 65 %. [Odhad]
- **Požadovaný výnos 14–18 % p. a.** Vážený výnos je těsně nad horní hranicí, ale jen při mých pravděpodobnostech: při 45/40/15 vychází 11,6 % p. a., tedy pod laťkou. **Buy podle definice (+50 až +100 % za 1–3 roky) to váženě není.** +50 % váženě by vycházelo při ceně ~8,0 EUR, laťku 14 % / 18 % p. a. splňuje cena pod ~10,1 / 9,6 EUR. [Odhad]
- **Pozice:** U Tomáše **10,8 %** (4. největší pozice). Rámec pro nízkou conviction je **6–8 %**, takže je **převážená ~1,4×** a obrana celkem dělá 26 % portfolia. U Michala **5,1 %** v konzervativním portfoliu, rámec **2–3 %**, převážená ~2×. Teď **nic nedělat**: vážený výnos laťku ještě splňuje a prodávat 4 týdny před guidance 2027 na 52W minimu by znamenalo vzdát se opce na Q4. O velikosti rozhodnout podle guidance 2027 (prosinec–leden). [Názor]
- **Proti sell-side:** Konsenzus z doby před výsledky (25,08 EUR, 11× Buy) je mrtvý. Nejnovější cíle jsou JPM 12, DB 14 a BofA 13. Můj base (12,6) je u nich, nikoli u Patrie (22,16) nebo u průměru Bloombergu (~20). [Fakt/Názor]
- **Co by signál zvrátilo:**
    - 🟢 **Teze posílena:** guidance 2027 s marží **≥21 %** a tržbami **≥8 mld. EUR**, net debt k 31. 12. 2026 **≤3,5 mld.** (reported pod 2,0×), NWC **≤35 %** tržeb, Q4 objednávky M/L munice s book-to-bill ≥1, potvrzená dividenda a konec lock-upu bez prodejů Strnada. Pak posunu pravděpodobnosti na 25/50/25 a vážený výnos vyjde ~29 % p. a.
    - 🔴 **Teze oslabena → ⚡ ke zvážení redukovat (Tomáš k ~6 %, Michal k 2–3 %):** guidance 2027 s marží pod 19 % nebo tržbami pod 7,5 mld., další revize FY2026, net debt ke konci roku nad 3,9 mld. (leverage nad 2,2×), Q4 book-to-bill pod 0,8 nebo backlog M/L munice pod 5 mld., zrušená dividenda, prodej či placement Strnada po lock-upu, schválená sektorová daň nebo eskalace kauz kolem prospektu. Při bear 45–50 % vychází vážený výnos jen 5–12 % p. a. [Názor]

## Snapshot a kontext (kroky 0–1)

### Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor / subsektor | Obrana: munice středních a velkých ráží (64 % tržeb 9M), pozemní systémy (Tatra, Excalibur, 14 %), Ammo+ (malorážová munice Sellier & Bellot, Federal/Remington z Kinetic Group, 20 %), aerospace a elektronika [Fakt] | [Quartr 9M call](https://web.quartr.com/m/sources/s56478557092376389809974) |
| HQ, listing, ticker | Praha, holding CSG N.V. (NL). Euronext Amsterdam (CSG), duální kotace v Praze. ISIN NL0015073TS8. IPO 23. 1. 2026 za **25 EUR** [Fakt] | [Euronext](https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/01/23/cpr01_notified_CZECHOSLOVAK%20GROUP%20Announces%20Admission%20to%20Trading%20on%20Euronext%20Amsterdam.pdf), dossier |
| Cena | 9,32 EUR (19. 11.), 20. 11. intraday 8,86 (−4,9 %). Od IPO **−63 %**, od maxima −74 % [Fakt, výpočet] | patria.cz, [boerse.de](https://www.boerse.de/aktien/CSG-NV-Aktie/NL0015073TS8) |
| 52W low–high | 8,92–35,50 EUR (Amsterdam). 20. 11. Stuttgart 8,85 = nové minimum [Fakt] | investing.com (dossier), boerse.de |
| Market cap / EV | 9,32 mld. EUR (1,00 mld. akcií). EV **13,64 mld.** (net debt 4,32). Bez strategických podílů (0,73) a půjček subdodavatelům (0,70) **12,21 mld.** [Fakt/výpočet] | [stockanalysis](https://stockanalysis.com/quote/ams/CSG/), [Quartr 9M](https://web.quartr.com/m/sources/s59505300070) |
| Tržby TTM | **7,02 mld. EUR**. FY2026 guidance 7,4–7,6 mld. [Fakt/výpočet] | [Quartr FY25](https://web.quartr.com/m/documents/3170114), [9M](https://web.quartr.com/m/documents/4227013) |
| Marže | hrubá (tržby − materiál) 9M 46,9 % · adj. op. EBIT LTM 22,8 % (9M 23,1 %, Q3 21,0 %) · čistá LTM 15,4 % · FCF 9M **−777 mil.** (−16 % tržeb), FY2025 −270 mil. [Fakt/výpočet] | [Quartr 9M P&L](https://web.quartr.com/m/sources/s71060228935), [CF](https://web.quartr.com/m/sources/s56005340727) |
| Valuace | EV/EBITDA LTM 7,6× (adj. 6,8×) · EV/EBIT LTM 8,5× · P/E LTM 8,6× · P/E 2026E 10,1× (JPM EPS 0,92) [Výpočet] | skript, [investing.com/JPM](https://de.investing.com/news/stock-market-news/jp-morgan-sieht-margen-von-csg-unter-druck-nachfrageverschiebung-bei-munition-belastet-3764380) |
| Net debt / EBITDA | **2,4×** reported (4,32 mld. / LTM 1,79 mld.), 1,6× adjusted. Cíl ke konci roku pod 2,0× / pod 1,5× [Fakt] | [Quartr 9M](https://web.quartr.com/m/sources/s59505300070) |
| Free float / insideři | Free float **15,2 %** (152 mil. akcií vč. greenshoe). Michal Strnad (přes CSG FIN) ~84,8 % [Fakt] | [Quartr H1](https://web.quartr.com/m/sources/s83684311121), [kurzy.cz](https://zpravy.kurzy.cz/868620-akcie-csg-ve-stredu-vzrostly-nejsilneji-od-ipo-zacne-short-squeeze/) |
| CEO / CFO | Michal Strnad (CEO a předseda boardu) / Zdeněk Jurák | [Quartr call](https://web.quartr.com/m/sources/s72946824361875464346215) |
| IR | [investors.csg.com](https://investors.csg.com/en) | |
| Konsenzus | Před výsledky 14 analytiků (11 Buy / 1 Hold / 2 Sell), průměrný cíl 25,08 EUR. Po výsledcích JPM Neutral 12, DB Hold 14, BofA Underperform 13. Průměr Bloombergu „mírně nad 20“ (E15, 18. 11.) [Fakt] | [investing.com](https://uk.investing.com/equities/csg-nv), [ad-hoc-news 19. 11.](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/csg-aktie-erholung-nach-rekordtief/70536004) |
| Denní likvidita | ~1,1–1,2 mil. akcií (3M), tedy ~11 mil. EUR denně a ~0,8 % free floatu. **Průměrná** vzhledem k free floatu, podprůměrná vzhledem k market capu [Fakt/Odhad] | investing.com, skript |
| RSI 14 | Neověřeno (denní řadu nemám). Po −31 % za týden a −37 % za měsíc odhaduji **pod 30**, tedy přeprodáno [Odhad] | [ls-tc](https://www.ls-tc.de/de/aktie/4347672) (výkonnost) |

### Krok 1 – zdroj a kontext idey

- **Zdroj:** Stávající pozice z IPO roku. Tomáš drží xtb + t212 s váženou nákupkou 14,42 EUR, Michal t212 s nákupkou 14,91 (`config/portfolio.yaml`). Data nákupů v repu nejsou. Dossier vznikl při onboardingu 18. 11. 2026.
- **Proč je cena tam, kde je:**
    - **IPO (leden):** ocenění 25 mld. EUR, 3,8 mld. hrubě, z toho jen 0,75 mld. nové akcie a ~2,55 mld. prodal Strnad ([Euronext](https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/01/23/cpr01_notified_CZECHOSLOVAK%20GROUP%20Announces%20Admission%20to%20Trading%20on%20Euronext%20Amsterdam.pdf)). Maximum 35,50 EUR. [Fakt]
    - **Květen–červen:** Short report Hunterbrook (4. 5.) a short Qube (až 0,8 % akcií 9. 7.). Akcie spadla až na 12,20 EUR ([kurzy.cz](https://zpravy.kurzy.cz/868620-akcie-csg-ve-stredu-vzrostly-nejsilneji-od-ipo-zacne-short-squeeze/)). [Fakt]
    - **Srpen:** Silné H1 vyneslo akcii vnitrodenně nad 20 EUR, Qube short stáhl na 0,17 % ([kurzy.cz](https://zpravy.kurzy.cz/870928-qube-utika-z-shortu-csg-zmizelo-6-3-milionu-akcii-jenze-kde-je-vzala/)). [Fakt]
    - **11. 11.:** Výhled marže snížen z 24–25 % na ~21 %, NWC z pod 20 % na pod 35 %, bez předchozího profit warningu. Za den −20,6 %, pak downgrady JPM a DB a 17. 11. dalších −8,7 %. [Fakt, dossier]
- **Trh a výhled:**
    - Poptávku po munici táhnou výdaje NATO (cíl 3,5 % HDP na core obranu do 2035, [ITF](https://czechoslovakgroup.com/itf/CZECHOSLOVAK_GROUP_ITF_FINAL.pdf)) a evropský program SAFE.
    - Mix se rychle posouvá od standardní 155mm munice k extended-range, a ceny standardu proto padají ([Quartr call](https://web.quartr.com/m/sources/s65745047351769352711517)).
    - Kapacity v Evropě rostou (CSG 0,85 → 1,1 mil. ks, RHM a další) a drony berou část role dělostřelectva (Bernstein 19. 11., JPM 12. 11.).
    - Výhled na 2027–2030: objemy nejspíš vysoké, ale s tlakem na ceny. Délka cyklu je hlavní spor (krok 9b). [Fakt/Názor]

## Teze a variant perception (krok 2)

**Teze v jedné větě:** Trh oceňuje CSG, jako by letošní ~21% marže byla strop a muniční cyklus měl vrchol za sebou. Při base cestě (marže ~21 % v 2028, uvolnění části NWC) je akcie ~30–35 % pod hodnotou. Edge je ale slabý: cíl managementu 26–28 % je podle mě nereálný, a pokud vyjde Bernsteinův 3letý cyklus, dnešní cena levná není. [Názor]

- **Co si myslí trh (reverse DCF, WACC 10,5 %):** Upravené EV 12,2 mld. odpovídá jedné ze dvou interpretací. Při růstu tržeb 6 → 2 % ročně jde o **trvalou EBIT marži ~18,0 %**. Při nulovém růstu z 7,5 mld. jde o ~23,7 %. A při „Bernsteinově“ cestě (2027–28 růst, 2029–31 −10 % ročně) by dnešní cenu ospravedlnila až marže **~25,7 %**. [Výpočet]
- **Co si myslím já:**
    1. **26–28 % je nedosažitelných kvůli mixu.** Pokud Land Systems tvoří ~22 % tržeb při 17 %, Ammo+ ~22 % při 11 % a ostatní 4 % při 5 %, potřebuje M/L munice na skupinových 26 % marži ~39 %. Extended-range má podle CFO marži „blízko 30 %“ ([Quartr](https://web.quartr.com/m/sources/s53325195009424610662943)). Při 28–30 % vychází skupina na **20–21,5 %**. Land Systems přitom tvoří 57 % backlogu ([Quartr](https://web.quartr.com/m/sources/s63708768378855997450473)). [Odhad, výpočet]
    2. **Trvalých 18 % je zase příliš pesimistických**, pokud se ceny ER udrží. CFO je chce s vertikální integrací ochránit ([Quartr](https://web.quartr.com/m/sources/s91192704855371790775376)), Ammo+ se zotavuje (Q3 EBIT 2× r/r) a Land Systems mají backlog ~10 mld., tedy ~11 let současných tržeb segmentu. [Názor/výpočet]
    3. **Cash:** NWC 42 % LTM tržeb je extrém. CFO osobně čeká střednědobě ~20 % ([Quartr](https://web.quartr.com/m/sources/s76674208712649817145434)). Návrat jen k 30 % uvolní ~0,8 mld. EUR (~0,8 EUR na akcii). [Odhad]
- **Proč je trh podle mě vedle:** Diskont ~46–48 % k peers je firemní (governance, cash conversion, kvalita backlogu), ne sektorový (GS drží sektor OW). Uzavře se jen důkazy (Q4 cash, guidance 2027), ne narativem. [Názor]
- **Edge:** Interpretační a slabý. Míří **proti managementu** (marže) i **proti trhu** (trvalost marže a cash). Proto 🟡 a žádné přikoupení. [Názor]

## Byznys model, segmenty a KPI (krok 3)

### Co firma dělá a jak vydělává

CSG reportuje dva segmenty, Defence Systems a Ammo+, a v rámci Defence Systems čtyři subsegmenty. Vydělává hlavně na vládních zakázkách: 69 % tržeb jde do NATO, Evropa bez Ukrajiny 49,7 %, USA 18,9 %, Ukrajina 17,3 % (konec 2025: 27 %) ([Quartr](https://web.quartr.com/m/sources/s71060228935), [call](https://web.quartr.com/m/sources/s73654890687340568078628)). MO Ukrajiny a ČR daly v H1 26 % tržeb (H1 2025: 37 %) ([Quartr H1](https://web.quartr.com/m/sources/s55058562112)). [Fakt]

| Subsegment | Tržby 9M 2026 (r/r) | Op. EBIT / marže 9M | Podíl na backlogu | Zdroj |
|---|---|---|---|---|
| M/L Ammunition (155 mm, tankové, minomety) | 3 034 mil. (+10,3 %), Q3 913 (−7 %) | v Defence Systems, ER „blízko 30 %“ | 32 % (~5,8 mld.) | [Quartr](https://web.quartr.com/m/sources/s60707190796) |
| Land Systems (Tatra, Excalibur, MORANA, mostní vozidla) | 678 mil. (+15,8 %), Q3 233 (−35 %) | ~15,5 % | 57 % (~10,3 mld.) | [Quartr](https://web.quartr.com/m/sources/s73291146760) |
| Aerospace & Defence Electronics + Advanced | 81 mil. (−37 %) | – | 2,5 % | tamtéž |
| **Defence Systems celkem** | **3 793 mil. (+9,5 %)** | **1 056 mil. / 27,9 %** | | |
| **Ammo+** (S&B, Federal, Remington, CCI, Speer) | **971 mil. (−4,7 %)**, Q3 +11 % | **79 mil. / 8,1 %** | 8,5 % | [Quartr](https://web.quartr.com/m/sources/s60707190796) |

### Sektorové KPI (obrana: backlog, book-to-bill, kapacita)

| KPI | Hodnota | Zdroj |
|---|---|---|
| Backlog | **18 mld.** (konec 2025: 15). Fixed 7, frame 8, soft 3. Pipeline 29, celkem 47 mld. [Fakt] | [Quartr](https://web.quartr.com/m/sources/s69670198427) |
| Book-to-bill Q3 | **0,6** (objednávky ~0,9 mld. vs. tržby 1,5 mld.). JPM: od dubna 2026 žádná velká objednávka M/L munice [Fakt] | [Quartr](https://web.quartr.com/m/sources/s69670198427), [JPM přes investing.com](https://de.investing.com/news/stock-market-news/jp-morgan-sieht-margen-von-csg-unter-druck-nachfrageverschiebung-bei-munition-belastet-3764380) |
| **Rozpor v backlogu** | H1 17 mld. + Q3 objednávky 0,9 − tržby 1,5 ≈ 16,4 mld., firma přesto uvádí 18. Buď jde o zaokrouhlení, nebo o přesuny z pipeline či soft. Analytik Ross Law spočítal pokles backlogu munice o ~0,7 na ~5,8 mld., CFO pokles popřel ([Quartr](https://web.quartr.com/m/sources/s68486035339034298216576)) [Fakt/Názor] | [Quartr H1](https://web.quartr.com/m/sources/s83684311121) |
| Kapacita 155 mm | ~850 tis. ks (2026) → ~1,1 mil. do konce 2027. V Q3 prakticky 100 % ER [Fakt] | [Quartr](https://web.quartr.com/m/sources/s85647159102198059117813) |
| Vertikální integrace | Energetika in-house „do konce 2027 nebo začátku 2028“. Walsrode (NC) konec 2027, Gnaschwitz (NG, >100 mil.), Lavrio TNT konec 2027, **EURENCO JV bimodulární náplně až Q2 2028** [Fakt] | [Quartr](https://web.quartr.com/m/sources/s79807170153552959426090), [9M](https://web.quartr.com/m/sources/s73291146760) |
| Recommissioning (repasované zásoby) | Podíl klesá a střednědobě má být zanedbatelný. Střednědobé cíle na něm podle firmy nestojí [Fakt] | [Quartr](https://web.quartr.com/m/sources/s73291146760) |
| Land Systems | >1 500 vozidel ročně (polovina ambice 3 000 z IPO), backlog +77 % YTD [Fakt] | [Quartr](https://web.quartr.com/m/sources/s74302672330820995458808) |

### Moat

- **Munice: střední, ale časově omezený.** CSG je #2 v evropské M/L munici (~35 % trhu, [ITF](https://czechoslovakgroup.com/itf/CZECHOSLOVAK_GROUP_ITF_FINAL.pdf)). Výhodou je vlastní energetika v době, kdy jsou úzkým hrdlem prachy, TNT a bimodulární náplně. Jakmile kapacity energetik v Evropě (RHM, Nammo, EURENCO, PGZ) dorostou, prémie za nedostatek zmizí. [Názor]
- **Land Systems: střední.** Tatra podvozky, MORANA a mostní vozidla, silná pozice v CEE (PGZ, SAFE), ale konkurence KNDS, RHM, Hanwha a Patria. [Názor]
- **Ammo+: slabý až střední.** Největší výrobce malorážové munice na Západě, silné značky, ale komoditní vstupy (měď) a cyklus US civilní poptávky. [Fakt/Názor]

### Produkt a recenze

- **Zákazníci:** Polsko (PGZ, kontrakty >250 mil. v Q3), Lotyšsko (MORANA), US Army (rámec modernizace muničních závodů do 4,2 mld. USD, zatím jen kvalifikace), FBI a severské policie (Federal), nový JV v Ázerbájdžánu ([Quartr](https://web.quartr.com/m/sources/s84562418020)). [Fakt]
- **Negativní signály:**
    - NATO agentura NSPA suspendovala španělskou FMG.
    - Slovenský rámec za 58 mld. EUR nemá pevné účastníky.
    - Česká vláda podle zpráv zastavila financování muniční iniciativy. Hunterbrook uvádí přirážku ~28–30 % nad tureckou nabídkou ([Hunterbrook](https://hntrbrk.com/investigations/csg)). [Fakt podle Hunterbrook, CSG popírá]

## Finance, alokace kapitálu, rozvaha a governance (kroky 4–7)

### Krok 4 – finance

| FY | Tržby | Op. EBIT (Quartr std.) | Čistý zisk | CFO / FCF | Zdroj |
|---|---|---|---|---|---|
| 2021 | 14,4 mld. CZK | 1,30 mld. CZK | 1,32 mld. CZK | 3,29 mld. CZK / – | [Quartr](https://web.quartr.com/m/documents/2682398) |
| 2022 | 24,9 mld. CZK | 3,99 mld. CZK | 3,47 mld. CZK | 7,19 mld. CZK / – | [Quartr](https://web.quartr.com/m/documents/2682387) |
| 2023 | 1,73 mld. EUR | 378 mil. | 210 mil. | 252 / 178 mil. | [Quartr](https://web.quartr.com/m/documents/2682364) |
| 2024 | 4,01 mld. (+131 %, Kinetic od 11/2024) | 1 013 mil. | 633 mil. | 941 / 825 mil. | [Quartr](https://web.quartr.com/m/documents/2682264) |
| 2025 | 6,74 mld. (+72 %) | 1 593 mil. | 874 mil. | **−45 / −270 mil.** | [Quartr](https://web.quartr.com/m/documents/3170114) |
| 9M 2026 | 4,76 mld. (+6,1 %) | 1 102 mil. (23,1 %) | 721 mil. (+41 %) | −231 / **−777 mil.** | [Quartr](https://web.quartr.com/m/sources/s56005340727) |
| FY2026 guidance | 7,4–7,6 mld. | ~21 % (dřív 24–25 %) | – | NWC pod 35 %, capex ~8,5 % | [Quartr](https://web.quartr.com/m/sources/s68725230757) |

- **Kvalita zisku: slabá.** Druhý rok po sobě záporný FCF při EBIT 1,6 mld. Cash conversion (EBITDA − capex)/EBITDA spadla na 79 %. Pre-tax operating CF za 9M je −200 mil. ([Quartr](https://web.quartr.com/m/sources/s68725230757)). V Q3 vystřelily ostatní provozní výnosy na 100 mil. (Q3 2025: 13 mil.) a náklady na 132 mil. Netto je to podobné jako loni, struktura ale ukazuje na jednorázové položky, které firma nerozepisuje ([Quartr](https://web.quartr.com/m/sources/s71060228935)). [Fakt/Názor]
- **Přechodné vs. strukturální:**
    - Přechodné: posun ~300 mil. tržeb z Q3 do Q4 ([Quartr](https://web.quartr.com/m/sources/s90019239360283360599996)), výprodej zásob standardní munice (pokračuje do 2027) a předzásobení komponentami.
    - Strukturální: mix k Land Systems, tlak na ceny standardní munice, růst capexu (8,5 % v 2026) a závislost na subdodavatelích (půjčky 700 mil.). [Názor]
- **Implikovaný Q4:** Guidance ~21 % na 7,5 mld. znamená Q4 EBIT ~473 mil. na 2,74 mld., tedy **~17,3 %**. To je „mid-teens“, jak spočítal analytik na callu ([Quartr](https://web.quartr.com/m/sources/s90155175150176116775786)). Q4 musí přinést i ~1,0 mld. sezónního uvolnění NWC. CFO čeká hotovost ke konci roku ~1,5–1,6 mld. (30. 9.: 1,19 mld.) ([Quartr](https://web.quartr.com/m/sources/s68954133268001000895727)). [Výpočet/Fakt]
- **FCF 2026:** JPM snížil odhad z +860 mil. na **−695 mil.** (včetně půjček subdodavatelům ~700 mil.), tedy ~0 bez nich. Analytik David Perry připomněl dřívější komunikaci +0,8–0,9 mld. ([Quartr](https://web.quartr.com/m/sources/s67485258604558974299521)). [Fakt]

### Krok 5 – alokace kapitálu

- **M&A a podíly 2026:** 731 mil. do JV a strategických podílů: MDA Space 9,5 % (podle JPM ~400 mil.), Hirtenberger, 4iG, North Vector Dynamics, Alzchem, DOMAR, JV EURENCO/FNSS/Reunert, Řecko a Ázerbájdžán ([Quartr](https://web.quartr.com/m/sources/s84562418020)). K tomu **700 mil. půjček subdodavatelům** (do 9/2027, mimo NWC). Investice jdou do vesmíru, dronů a interceptorů, tedy mimo jádro, v roce, kdy firma pálí cash. [Fakt/Názor]
- **Kinetic Group (11/2024):** Akvizice za ~2,1 mld. EUR (Quartr cash acquisitions 2024). Celé Ammo+ (Kinetic + S&B) má dnes anualizovaný EBIT ~105 mil., implikovaný násobek je tedy **~20× dnešního EBIT** (horní mez). Při normalizované marži 12–14 % to dělá ~12–13,5×. EBIT samotné Kinetic jsem nedohledal. Synergie firma nekvantifikovala. [Odhad, výpočet]
- **Capex:** 2026 ~8,5 % tržeb (9M 5,3 %, Q4 zrychlí), střednědobě 4–5 %. Iowa Future Artillery Complex 2029. [Fakt]
- **Dividenda:** ITF slibovala výplatu **30–40 % čistého zisku od 2027** ([ITF](https://czechoslovakgroup.com/itf/CZECHOSLOVAK_GROUP_ITF_FINAL.pdf)), tedy z FY2026. CFO 11. 11. politiku nezměnil, ale rozhodne se až koncem roku ([Quartr](https://web.quartr.com/m/sources/s57495361429025895366437)). Buyback žádný. [Fakt]
- **Hodnocení:** Agresivní, růstově a strategicky orientovaná alokace. Track record cash conversion je zatím špatný. [Názor]

### Krok 6 – rozvaha

| 30. 9. 2026 | mld. EUR | Zdroj |
|---|---|---|
| Úvěry | 2,948 (31. 12. 2025: 1,824) | [Quartr](https://web.quartr.com/m/sources/s55008868789) |
| Dluhopisy | 2,474 (2,568) | tamtéž |
| Leasingy | 0,086 | tamtéž |
| Hotovost (výkaz CF) | 1,188 (1,505) | [Quartr](https://web.quartr.com/m/sources/s80666870329) |
| **Net debt** | **4,320** (3,004) · LTM EBITDA 1,788 → 2,4× | [Quartr](https://web.quartr.com/m/sources/s59505300070) |
| Vlastní kapitál (net assets) | 3,506 (2,079) · goodwill + nehmotná aktiva 2,10 | [Quartr](https://web.quartr.com/m/sources/s56005340727) |

- **Financování:** Senior facility refinancovaná v červenci na 3,06 mld. (čerpáno ~1,7 mld.), splatnost 6 let, marže −125 až −150 bp, podmínky se blíží nezajištěnému IG ([Quartr](https://web.quartr.com/m/sources/s55008868789)). Placené úroky za 9M 209 mil. Rating a splatnosti dluhopisů jsem neověřoval. [Fakt]
- **Pozor na data:** Quartr standardizace a tabulka dluhu uvádějí „cash (adjusted)“ 2,619 mld. Net debt 4,32 ale sedí na hotovost 1,188 z výkazu CF (5,508 − 1,188). Počítám s 4,32. [Fakt/výpočet]
- **Výhled:** Konec 2026 reported pod 2,0×, tedy net debt pod ~3,5 mld. při EBITDA ~1,74 mld. JPM odhaduje 3,6 mld. ([JPM](https://de.investing.com/news/stock-market-news/jp-morgan-sieht-margen-von-csg-unter-druck-nachfrageverschiebung-bei-munition-belastet-3764380)). Půjčky subdodavatelům (0,7) nesou úvěrové riziko slabších dodavatelů. [Fakt/Odhad]

### Krok 7 – vlastnictví a governance

- **Kontrolní akcionář:** Strnad drží ~84,8 % a je CEO i předseda boardu v jedné osobě. Minorita nemá protiváhu. Free float 15,2 %, anchor investoři BlackRock, Artisan a QIA (Al-Rayyan) se závazky 900 mil. ([Euronext](https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/01/23/cpr01_notified_CZECHOSLOVAK%20GROUP%20Announces%20Admission%20to%20Trading%20on%20Euronext%20Amsterdam.pdf)). [Fakt]
- **Lock-up:** 360 dní pro Strnada a velké akcionáře, tedy **~18. 1. 2027**. To je [Odhad] dopočtený od 23. 1. 2026 podle Seznam Zpráv, v release Euronextu ani v ITF lock-up uvedený není. Ověřit v prospektu. [Odhad]
- **Spřízněné strany (Hunterbrook, 4. 5.):** Před IPO přešlo 20–30 dceřinek na Strnadovu Ytaru a pohledávky ~275 mil. EUR zůstaly nesplacené. Excalibur Army měla pohledávky za CEO otcem, firma má nájem od bývalého místopředsedy a v představenstvu MSM sedí obviněný manažer. CSG vše odmítá. Hunterbrook drží short ([Hunterbrook](https://hntrbrk.com/investigations/csg)). [Fakt podle Hunterbrook / Názor]
- **Kratochvíl (10 % v CSG Land Systems, 8,9 % v MSM Group):** Uplatnil put opci, jeho ocenění je >34 mld. Kč, CSG počítá ~3,5 mld. Kč. Městský soud zamítl předběžné opatření (6/2026), odvolání čeká u Vrchního soudu. CSG tvrdí, že závazek by nesla skupina mimo CSG ([Ekonomický deník](https://ekonomickydenik.cz/boj-miliardy-podil-strnad-csg-soud-exmanazerovi-kratochvilovi-nevyhovel/)). Pro akcionáře je důležitý i fakt, že 10 % Land Systems patří minoritě. [Fakt]
- **Komunikace:** Firma před 11. 11. nevydala profit warning a analytik Growe to na callu otevřeně vytkl ([Quartr](https://web.quartr.com/m/sources/s86792162534392430511645)). [Fakt]
- **Insideři:** Nákupy managementu ani Strnada po IPO jsem nenašel. Auditora jsem neověřoval. [Fakt/neověřeno]

## Požadovaný výnos a valuace (kroky 8–9)

### Krok 8 – rizikový profil a požadovaný výnos

**Baseline:** 10Y Bund ~3,3 % plus prémie ~5 % dává **~8–8,5 % p. a.** GS čeká u STOXX 600 za 12 M ~9 % celkového výnosu (log 2026-11 · GS 13. 11.). [Odhad/Fakt]

**Rizikové faktory CSG:**

1. **Muniční cyklus a ceny (zvyšuje, +2,5 až +3 p. b.).** M/L munice dělá 64 % tržeb a většinu EBIT. Q3 book-to-bill 0,6, ceny standardu padají a Bernstein čeká ~3letý cyklus. Pro zisk z vrcholu cyklu nejde použít násobek stabilní firmy.
2. **Governance a kontrolní akcionář (zvyšuje, +2 až +2,5 p. b.).** ~85 % Strnad, CEO zároveň předseda, spřízněné transakce podle Hunterbrook, Kratochvíl, NSPA/FMG a výhled bez varování. Minorita nemá jak vynutit disciplínu.
3. **Páka a pracovní kapitál (zvyšuje, +1,5 až +2 p. b.).** Leverage 2,4×, NWC 42 % tržeb, FCF −777 mil. za 9M a 700 mil. půjček subdodavatelům. Dividenda není jistá.
4. **Overhang lock-upu a free float 15 % (zvyšuje, +0,5 až +1 p. b.).** Kolem 18. 1. 2027 může přijít nabídka, Strnad už jednou prodal ~2,55 mld. Jde spíš o riziko načasování než hodnoty.
5. **Politika: Ukrajina 17 % tržeb, česká sektorová daň (zvyšuje, +0,5 až +1 p. b.).** Příměří je v base scénáři BCA (18. 11.), SPD navrhuje daň ze zisku zbrojařů až 90 %.
6. **Startovní valuace a diverzifikace backlogu (snižuje, −1,5 až −2 p. b.).** ~10× P/E, backlog 18 mld. s rostoucím podílem Land Systems, USA 19 % tržeb a refinancovaný dluh se splatností 2032. Diskont už velkou část rizika nese.

**Závěr:** Čistá prémie +6 až +9,5 p. b. dává **požadovaný výnos 14–18 % p. a.** Spodní hranice platí, když Q4 a guidance 2027 potvrdí cash a marži a lock-up proběhne bez prodejů. Horní, dokud trvají pochybnosti o objednávkách munice a governance. U 4. největší pozice s 26% obrannou expozicí bych pod 14 % nešel. [Názor]

**Horizont ~1,4 roku (do 31. 3. 2028):** Mezikroky jsou guidance 2027 (prosinec–leden), lock-up (~18. 1. 2027) a FY2026 (25. 3. 2027). Teze se ale potvrdí až výsledky FY2027 (~březen 2028): ukážou, jestli vertikální integrace (konec 2027, EURENCO Q2 2028) drží marži a jestli se uvolnil NWC. [Odhad]

### Krok 9 – valuace

**Multiples vs. peers** [Fakt, StockAnalysis k uvedenému datu; RHM přepočten na 724,70 EUR (19. 11.), forward EPS z 26. 10.]

| Firma | Proč | EV/EBITDA TTM | fwd P/E | Datum |
|---|---|---|---|---|
| **CSG** | – | **7,6×** (adj. 6,8×) | **10,1×** (2026E, JPM) | 19. 11. |
| Rheinmetall | munice, vozidla (přímý konkurent) | 16,2× | 16,1× | 26. 10. / 19. 11. ([odkaz](https://stockanalysis.com/quote/etr/RHM/statistics/)) |
| Renk | pohony vozidel | 16,2× | 18,9× | 23. 10. ([odkaz](https://stockanalysis.com/quote/etr/R3NK/statistics/)) |
| Leonardo | diverzifikovaná obrana | 12,7× | 18,6× | 26. 10. ([odkaz](https://stockanalysis.com/quote/bit/LDO/statistics/)) |
| BAE Systems | munice (UK/US), vozidla | 14,8× | 22,4× | 26. 10. ([odkaz](https://stockanalysis.com/quote/lon/BA/statistics/)) |
| General Dynamics | OTS (munice US), Land Systems | 14,7× | 19,4× | 6. 11. ([odkaz](https://stockanalysis.com/stocks/gd/statistics/)) |
| Colt CZ | česká malorážová munice (S&B konkurence) | 11,6× | 12,1× | 20. 11. ([odkaz](https://stockanalysis.com/quote/pra/CZG/statistics/)) |
| Hensoldt / Saab / Kongsberg | elektronika, rakety (prémiové) | 28,6× / 28,0× / 32,6× | 39,8× / 37,0× / 32,4× | 10/2026 |

- **Čtení:** Medián „core“ peers (RHM, Renk, LDO, BAE, GD, Colt) vychází na EV/EBITDA **14,7×** a fwd P/E **18,8×**. CSG má diskont **~46–48 %**. Data peers jsou většinou z konce října a od té doby EU obrana klesla (RHM −30 %), skutečný diskont je tedy menší, spíš ~35–40 %. Při fwd P/E rovném mediánu s diskontem 30 / 40 / 50 % vychází CSG na **12,10 / 10,37 / 8,64 EUR**. Nammo a KNDS nejsou kotované. [Výpočet/Odhad]
- **Proč diskont ano:** Zisk z vrcholu muničního cyklu, záporný FCF, governance a 15% free float. Colt CZ (12× P/E) ukazuje, že česká munice s kontrolním akcionářem se na 20× neobchoduje. [Názor]

**Reverse DCF** (WACC 10,5 %, daň 23 %, upravené EV 12,2 mld.): Při růstu 6 → 2 % a terminálu 1,5 % implikuje trvalou marži **18,0 %**, při nulovém růstu **23,7 %**, při Bernsteinově cestě tržeb **25,7 %**. Cena je levná jen tehdy, když je cyklus delší než ~3 roky. [Výpočet]

**DCF (cross-check, net debt konec 2026E 3,6 mld., podíly 0,73):** bear (tržby −10 % ročně 2029–31, marže 15 %) **4,28 EUR** · base (19,5 → 21 → 21,5 %) **11,88 EUR** (při WACC 9,5 / 11,5 %: 13,77 / 10,37) · bull (22 → 25 %) **16,92 EUR**. [Výpočet]

**Tři scénáře** (horizont do 31. 3. 2028. Cíl = EV/EBIT fwd × EBIT 2028E − net debt 2027E + podíly, plus dividenda) [Odhad, výpočet v Pythonu]

| Scénář | p | Tržby / marže 2027 | Tržby / marže 2028 | FCF 2027 → ND 2027 | EV/EBIT | Cíl | Výnos (horizont / p. a.) |
|---|---|---|---|---|---|---|---|
| Bear | 35 % | 7,3 mld. / 17 % | 7,0 mld. / 15,5 % | 0,65 → 3,25 mld. | 7,5× | **5,43 EUR** | −42 % / −33 % |
| Base | 45 % | 7,95 mld. / 19,5 % | 8,45 mld. / 21 % | 0,96 → 2,64 mld. | 8,0× | **12,59 EUR** (12,29 + div 0,30) | +35 % / +25 % |
| Bull | 20 % | 8,4 mld. / 22 % | 9,2 mld. / 24 % | 1,23 → 2,17 mld. | 10,5× | **22,26 EUR** (21,91 + 0,35) | +139 % / +90 % |

- **Bear:** Guidance 2027 zklame, standard se doprodává levně a ceny ER začnou v 2027–28 klesat (kapacity, drony). Příměří utlumí Ukrajinu, NWC se neuvolní, dividenda se ruší, polovina půjček subdodavatelům se prodlouží a lock-up přinese nabídku. Implikované P/E 2028 je 8× při EPS 0,68.
- **Base:** Marže 2027 zůstane kolem 19,5 % (výprodej standardu, mix Land Systems), v 2028 je 21 % s integrovanou energetikou. NWC klesne k 30 %, půjčky se vrátí, dividenda je ~0,30 a násobek se nezmění (~8×, žádný re-rating). P/E 2028 je 10× při EPS 1,21.
- **Bull:** Q4 objednávky M/L a SAFE zakázky, ER ceny drží, marže 24 % v 2028 (stále pod 26–28 %), NWC 27 % a re-rating na 10,5× (P/E 14×, pořád pod peers).
- **Vážená hodnota 12,02 EUR → +29 % za 1,36 roku (~21 % p. a.) vs. požadovaných 14–18 % p. a. → těsně nad laťkou, bez rezervy.**
- **Citlivost:**
    - Pravděpodobnosti: při 45/40/15 vychází 10,82 EUR (+11,6 % p. a.), při 50/40/10 9,98 EUR (+5 % p. a.), při 25/50/25 13,22 EUR (+29 % p. a.).
    - Násobek base: 7× dává 10,82 EUR, 9× dává 14,36 EUR.
    - Při intraday ceně 8,86 je vážený výnos +36 % (+25 % p. a.). [Výpočet]
- **Rozpor se sell-side:** Můj base (12,6) sedí u JPM (12) a DB (14), Patria (22,16) a starý konsenzus (25) počítají s cílovou marží managementu. [Názor]

### Krok 9b – co píšou analytici (research reporty)

V `research/log/2026-11.md` není žádný broker report, který by CSG jmenoval přímo. CSG tam figuruje jen v řádcích „Relevance“ přes témata #eu-defense, #nato-spending a #ukraine. Přímé zmínky proto pocházejí z webu, z dossieru a z `house-views.md`.

**1. Přímé zmínky (nejnovější nahoře)**

| Datum | Instituce | Rating / cíl | Co říká |
|---|---|---|---|
| 19. 11. 2026 | Bernstein (A. Rabier) | bez ratingu k CSG | CSG a RHM počítají s doplňováním zásob NATO přes 10 let, Bernstein jen s ~3 lety. Drony (~80 % ztrát) tlačí ceny i objemy dělostřelecké munice po 2030. Míří přímo proti jádru teze (house-views · Bernstein 19. 11.; web aktiencheck, zprostředkovaně) |
| 18. 11. 2026 | E15 (souhrn) / Bloomberg, Patria | průměr Bloombergu mírně nad 20 EUR, Patria 22,16 | Cyrrus čeká snižování cílů, Direct Investments vidí slábnoucí prioritu zbrojení po midterms ([E15](https://www.e15.cz/byznys/burzy-a-trhy/strnadova-csg-za-tyden-ztratila-103-miliard-proc-analytici-stale-veri-ve-zdvojnasobeni-ceny-1437393)) |
| 18. 11. 2026 | FT (souhrn analytiků) | – | Odhady provozního zisku 2030 snížené za 6 měsíců u CSG o ~20 %, u RHM o ~25 % (themes #eu-defense · Tracker 18. 11.) |
| 13. 11. 2026 | Deutsche Bank | Buy → **Hold**, cíl 25 → **14 EUR** ⬇️ | po snížení výhledu ([ad-hoc-news](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/csg-aktie-erholung-nach-rekordtief/70536004)) |
| 12. 11. 2026 | JPMorgan (D. Perry) | OW → **Neutral**, cíl 27,50 → **12 EUR** ⬇️ | Q3 objednávky 0,9 mld. (B2B 0,6). Ukrajina podle Kiel Institute mezi únorem a srpnem munici skoro nekupovala, od dubna žádná velká M/L zakázka. EPS 2026 1,15 → 0,92, FCF +860 → −695 mil., net debt 2026 1,8 → 3,6 mld. Marže M/L v Q4 ~20 % vs. ~30 % za 9M ([investing.com](https://de.investing.com/news/stock-market-news/jp-morgan-sieht-margen-von-csg-unter-druck-nachfrageverschiebung-bei-munition-belastet-3764380)) |
| 11. 11. 2026 | J&T Banka | negativní | výsledky a výhled pod očekáváním, efekt může být jednorázový ([CC.cz](https://cc.cz/akcie-csg-po-vysledcich-spadly-o-petinu-na-nove-minimum-strnadova-zbrojovka-zhorsila-vyhled-marze/)) |
| 1. 10. 2026 | BofA | zahájení: **Underperform, 13 EUR** | ([investing.com](https://uk.investing.com/equities/csg-nv)) |
| 11.–12. 8. 2026 | JPM / Berenberg / RBC / Barclays | Buy 27,50 / Buy 25 / zahájení Hold 18 / zahájení Sell 19 (podle investing.com) | po H1 (investing.com) |
| 22. 5. 2026 | Jefferies | Buy, cíl 35 → 30 ⬇️ | ([boerse.de](https://www.boerse.de/aktien/CSG-NV-Aktie/NL0015073TS8)) |

**2. Sektor a témata (#eu-defense, #nato-spending, #ukraine)**

- **GS (13. 11.):** EU obrana **OW**, růst EPS ~19–20 %, fwd P/E ~20×, PEG pod 1, ~50% diskont vůči US obraně. Podporu vidí v německých výdajích a nižších cenách energií (log 2026-11 · GS 13. 11.).
- **MS (15.–16. 11.):** Obrana má nejsilnější konsenzuální růst zisků, ale v modelu MS na OW nedosáhla kvůli slabému momentu RHM. Německé výdaje zaostávají za plánem (log 2026-11 · MS 15. 11.).
- **SG (9. 11.):** Evropské obranné backlogy se spolehlivě nepřetavují do marží a cash, RHM podruhé letos snížil cíl tržeb (log 2026-11 · SG 9. 11.).
- **JPM (9. 11.):** U obrany opatrný od léta 2025, před dvěma měsíci se otočil pozitivněji s preferencí modernizačních titulů. Munice 155 mm mezi ně nepatří (log 2026-11 · JPM 9. 11.).
- **BCA Gertken (18. 11.):** Příměří na Ukrajině je pravděpodobné, nespolehlivost USA ale spustí novou vlnu evropských zbrojních výdajů. Ruská provokace by znamenala risk-off (log 2026-11 · BCA 18. 11.).
- **Rozpočty a Ukrajina:** ING (4. 11.) čeká, že část Evropy zpomalí obranné výdaje, Gavekal C. Gave (13. 11.) naopak prudké navýšení. MS (16. 11.) uvádí, že EU zvažuje ~45 mld. EUR pro Ukrajinu na 2027. Gavekal L. Gave (6. 11.) píše, že šance na mír vzrostly. MS Liwag (7. 11.) má US rozpočet FY27 na 1,1 bil. USD (log 2026-11).

**3. Konsenzus vs. rozpory a co z toho plyne**

- **Shoda:** Výdaje na obranu v Evropě porostou i při příměří (GS, BCA, Gave C., MS). To podporuje objemy, a tedy můj base.
- **Rozpor 1 – délka cyklu:** Bernstein (~3 roky, drony) stojí proti managementům CSG a RHM (10+ let) a proti BCA (nová vlna výdajů). **Zpochybňuje** tezi: reverse DCF ukazuje, že při Bernsteinově cestě dnešní cena levná není. Proto má bear 35 %.
- **Rozpor 2 – sektor vs. firma:** GS sektor OW, ale SG (konverze backlogu), MS (moment RHM) a JPM/DB/BofA u CSG konkrétně jsou opatrní. Plyne z toho **nový argument**: diskont CSG je firemní a sektorový OW ho sám nezavře. Re-rating v base proto nepředpokládám.
- **Rozpor 3 – cílové ceny:** JPM 12 / BofA 13 / DB 14 proti Patrii 22,16 a průměru Bloombergu ~20. Můj base je u spodní skupiny, a ta **potvrzuje** nastavení scénářů.
- **Rozpor 4 – rozpočty:** ING proti Gave C. jde hlavně o rozpočty mimo CEE. Pro CSG jsou důležitější Polsko, Pobaltí a SAFE, kde výdaje rostou.

**4. Z grafů:** K obraně nebo CSG neobsahuje žádná extrakce v logu řádek „Z grafů“. Nepřímo relevantní jsou dva:
- BCA 10. 11. (Papic/Gertken): emise akcií (IPO + SEO) rostou k ~300 mld. USD za 12 M a nejvyšší kvintil IPO historicky zvyšuje pravděpodobnost vrcholu trhu. Vypovídá to o nabídce akcií obecně, tedy i o overhangu po lock-upu. Fwd P/E eurozóny je ~14–15, CSG je s ~10× pod průměrem eurozóny (log 2026-11 · BCA 10. 11.).
- SG 10. 11.: průmyslové kovy jsou v neobvykle časté backwardaci. Pro Ammo+ to znamená riziko nákladů na měď, CSG volatilitu mědi zmiňuje jako tlak na marži (log 2026-11 · SG 10. 11.).

## Base rate, rizika a protiargument (kroky 10–11)

### Krok 10 – base rate check

- **IPO na vrcholu sektoru s velkým secondary podílem:** Akcie, kde zakladatel prodá většinu emise (tady ~80 % z 3,8 mld.) v době rekordních marží, mají historicky podprůměrné výnosy v dalších 3–5 letech. Rekordní ziskovost při IPO se málokdy zopakuje. [Názor, obecně známé]
- **Profit warning u nové akcie:** První snížení výhledu bývá často následováno dalším. Trh to ví, a proto nevěří ani nezměněné střednědobé guidance. Zlom obvykle přináší až 2–3 čisté kvartály. [Názor]
- **Muniční cykly:** Po konci studené války i po útlumu Iráku a Afghánistánu (US malorážová munice po 2013) objemy i marže výrobců munice spadly během pár let. Výrobci s diverzifikací do vozidel a systémů dopadli lépe. CSG se diverzifikuje (Land Systems 57 % backlogu), ale za nižší marži. [Názor, obecně známé]
- **Short reporty:** Výsledky jsou smíšené. Některé firmy se plně zotavily, jinde se potvrdily problémy s účetnictvím. U CSG zatím nic nevedlo k přepracování výkazů, firma ale potvrdila klesající roli recommissioningu. [Názor]
- **Závěr:** Base rate pro rychlý návrat k IPO tezi je nízký. Bear s 35 % je oprávněný a bull nad 20 % bych zvedl až po guidance 2027 a čistém Q4.

### Krok 11 – rizika podle závažnosti

1. **Objednávky a ceny munice.** B2B 0,6, od dubna žádná velká M/L zakázka, ceny standardu dolů a drony. Pokud začnou padat i ceny ER, marže M/L spadne z ~30 % k 20 % (JPM pro Q4) a s ní skupina k 15–17 %. [Fakt/Odhad]
2. **Cash a rozvaha.** NWC 42 %, FCF 9M −777 mil., net debt 4,32 mld., 700 mil. u subdodavatelů s riziky jejich likvidity a nejistá dividenda. Pokud Q4 neuvolní ~1 mld., leverage zůstane nad 2× a JPM odhad 3,6 mld. bude optimistický. [Fakt/Odhad]
3. **Governance a důvěryhodnost.** Kontrolní akcionář s ~85 %, Ytara a spřízněné strany, Kratochvíl (10 % Land Systems), NSPA/FMG, nedotažené rámcové smlouvy a výhled bez varování. [Fakt]
4. **Lock-up ~18. 1. 2027 [Odhad].** Při 15% free floatu stačí malý placement a cena spadne. Strnad už jednou prodal ~2,55 mld. [Fakt/Odhad]
5. **Mix a cíl 26–28 %.** Pokud management cíl nezmění, hrozí další zklamání. Pokud ho sníží, potvrdí strukturální pokles marže. [Názor]
6. **Exekuce vertikální integrace.** Walsrode, Gnaschwitz a Lavrio do konce 2027, EURENCO až Q2 2028, celé „do konce 2027 nebo začátku 2028“. Posun znamená, že marže 2028 přijde později. [Fakt]
7. **Politika.** Ukrajina 17 % tržeb (příměří), česká sektorová daň (SPD), US politika (Vance v minulosti označil CSG za „Kremlin-linked“, podle Hunterbrook). [Fakt]
8. **Korelace v portfoliu.** RHM, TKMS, SMSH a TKA (přes TKMS) reagují na stejné zprávy (11. 11.: CSG −20,6 %, RHM −6,9 %). [Fakt]

**Nejsilnější protiargument proti mé (neutrální) tezi:** Bernstein může mít pravdu. Pokud je doplňování zásob NATO ~3leté a drony od 2029 stahují objemy i ceny dělostřelecké munice, dnešní cena levná není: reverse DCF v té cestě potřebuje trvalou marži ~26 %. Pak je 9,32 EUR spíš férová cena firmy s vrcholem zisku v 2025–26, se záporným FCF a s kontrolním akcionářem, který může po lock-upu prodávat. Držet 10,8 % portfolia v takové akcii je chyba velikosti, ne valuace. [Názor]

Opačný argument (pro býky): Q4 sezónně uvolní ~1 mld. NWC, guidance 2027 může překvapit a backlog Land Systems ~10 mld. dává roky práce. Při ~8× EV/EBIT stačí, aby se zisk udržel, a akcie vzroste o desítky procent. [Názor]

## Conviction, pozice, katalyzátory a monitoring (kroky 12–13)

### Krok 12 – conviction a velikost pozice

- **Conviction: nízká.** Rozptyl je −42 % až +139 % (směrodatná odchylka 65 %), edge je interpretační a vážený výnos splní laťku jen při mých pravděpodobnostech. Klíčové proměnné (objednávky munice, ceny ER, rozhodnutí Strnada po lock-upu) nemám jak předpovědět. [Názor]
- **Tomáš:** rámcová velikost **6–8 %**, současná **10,8 %** (`tools/portfolio.py`, 19. 11.), tedy **převážená ~1,4×**.
    - Obrana celkem **26 %** (CSG 10,8 + RHM 9,3 + TKMS 3,5 + SMSH 2,0) plus TKMS přes TKA. Jedna korelovaná sázka na evropské zbrojení. [Výpočet]
    - Dopad bear scénáře: ~**−4,5 p. b.** na celém portfoliu při dnešní váze, ~−2,9 p. b. při 7 %. [Výpočet]
    - **Doporučení:** Nepřikupovat, protože obrana je už 26 % a přikoupení by dávalo smysl až pod ~8 EUR (+50 % váženě). Neprodávat teď na minimu před guidance 2027. **Rozhodnout po guidance 2027:** při 🔴 spouštěčích z Verdiktu redukovat k ~6 %, při 🟢 držet. [Názor]
    - Tomáš je v CSG ~−35 %. Pokud by redukoval, realizovaná ztráta se obvykle dá započíst proti zdanitelným ziskům z cenných papírů ve stejném roce. Ověř si s daňovým poradcem, jestli se to vyplatí ještě v prosinci. [Názor]
- **Michal (konzervativní portfolio, 63 % ETF):** rámec **2–3 %**, současná **5,1 %**, tedy **převážená ~2×**. Obrana u něj dělá 15 % (s RHM 9,5 %). Dopad bear ~−2,1 p. b., při 3 % −1,3 p. b. Platí stejné rozhodovací pravidlo po guidance 2027, u Michala ale s nižší tolerancí: při jakémkoli 🔴 spouštěči redukovat k 2–3 %. [Názor]
- Nejsem finanční poradce. Tohle je podklad pro Tomášovo rozhodnutí, ne pokyn.

### Krok 13 – katalyzátory a monitoring

| Datum | Událost | Co sledovat |
|---|---|---|
| průběžně do konce roku | Objednávky M/L munice, SAFE zakázky (PL, Pobaltí), Ukrajina | velké zakázky 155 mm, mírová jednání („koalice ochotných“, Witkoff), Kiel tracker |
| **prosinec 2026 – leden 2027** | **Guidance 2027** + rozhodnutí o dividendě ([Quartr](https://web.quartr.com/m/sources/s47284517696276799820086)) | marže 2027 (laťka 19 / 21 %), tržby (7,5 / 8,0 mld.), potvrzení nebo snížení 26–28 %, dividenda 30–40 % |
| **~18. 1. 2027** [Odhad] | Konec lock-upu Strnada a velkých akcionářů | placement, prodeje (AFM registr), ověřit datum v prospektu |
| **25. 3. 2027** | FY2026 ([Quartr](https://web.quartr.com/m/events/796107)) | Q4 marže vs. ~17 %, NWC ≤35 %, net debt ≤3,5 mld., FCF bez půjček ≥0, Q4 book-to-bill, backlog M/L, výrok auditora |
| ~květen 2027 [Odhad] | Q1 2027 a valná hromada | marže při doprodeji standardu, dividenda |
| ~srpen 2027 [Odhad] | H1 2027 | NWC trend, ER ceny, Walsrode |
| září 2027 | Splatnost půjček subdodavatelům (700 mil.) | vrácení vs. prodloužení nebo odpis |
| konec 2027 | 1,1 mil. ks 155 mm, energetika in-house (Walsrode, Gnaschwitz, Lavrio TNT) | skluz = posun marže |
| Q2 2028 | EURENCO JV (bimodulární náplně) | poslední díl integrace |
| ~březen 2028 | FY2027 (konec horizontu) | marže 2027 vs. 19,5 % base, NWC vs. 30 %, výhled 2028 |
| průběžně | Kratochvíl (Vrchní soud), Hunterbrook, NSPA/FMG, česká sektorová daň, short pozice (AFM), výsledky RHM | governance diskont, read-across na ceny munice |

**Potvrdí tezi:** guidance 2027 marže **≥21 %** a tržby **≥8,0 mld.** · FY2026 marže ≥21 % (Q4 ≥17 %) · NWC k 31. 12. **≤35 %** tržeb · net debt **≤3,5 mld.** (pod 2,0×) a hotovost ~1,5 mld. · FCF 2026 bez půjček subdodavatelům a podílů **≥0** · Q4 book-to-bill **≥1,0** a backlog M/L **≥6 mld.** · dividenda z FY2026 potvrzena · lock-up bez prodejů · ceny ER „stabilní“ i v 2027.

**Vyvrátí tezi (🔴):** guidance 2027 marže **<19 %** nebo tržby **<7,5 mld.** · další revize FY2026 · net debt **>3,9 mld.** / leverage >2,2× · NWC >35 % · Q4 book-to-bill **<0,8** nebo backlog M/L **<5 mld.** · zrušená dividenda · placement nebo prodej Strnada · snížení cen ER, nebo potvrzení střednědobé marže pod 22 % bez plánu na cash · schválená sektorová daň · nové právní kroky kolem prospektu nebo NSPA.

**KPI pro Tracker:** adj. op. EBIT marže (skupina, Defence Systems, Land Systems, Ammo+) · tržby a book-to-bill (skupina, M/L) · backlog (fixed/frame/soft, M/L vs. Land Systems) · NWC % LTM tržeb · net debt a leverage (reported, adjusted) · FCF · kapacita 155 mm a stav energetik · podíl Ukrajiny · ceny ER vs. standard · dividenda · Strnadův podíl, lock-up, short pozice · Kratochvíl.

## Zdroje (krok 14)

Odkazy na konkrétní pasáže (Quartr sources, web) jsou u čísel v textu. Hlavní zdroje:

- **Quartr – CSG:** [firma (21954)](https://web.quartr.com/m/companies/21954) · [9M/Q3 2026 event + transcript](https://web.quartr.com/m/events/729445) · [9M trading statement](https://web.quartr.com/m/documents/4227013) · [slides 9M](https://web.quartr.com/m/documents/4278908) · [H1 2026 interim report](https://web.quartr.com/m/documents/4213622) · [FY2025 annual report](https://web.quartr.com/m/documents/3170114) · roční data [FY24](https://web.quartr.com/m/documents/2682264), [FY23](https://web.quartr.com/m/documents/2682364), [FY22](https://web.quartr.com/m/documents/2682387), [FY21](https://web.quartr.com/m/documents/2682398) · [FY2026 event 25. 3. 2027](https://web.quartr.com/m/events/796107)
- **IPO:** [Euronext – admission 23. 1. 2026](https://live.euronext.com/sites/default/files/company_press_releases/attachments/2026/01/23/cpr01_notified_CZECHOSLOVAK%20GROUP%20Announces%20Admission%20to%20Trading%20on%20Euronext%20Amsterdam.pdf) · [ITF (dividendová politika)](https://czechoslovakgroup.com/itf/CZECHOSLOVAK_GROUP_ITF_FINAL.pdf) · [Seznam Zprávy – lock-up](https://seznamzpravy.cz/clanek/ekonomika-finance-akcie-fondy-csg-otazky-a-odpovedi-k-burzovnimu-debutu-297166)
- **Repo:** research/log/2026-11.md (GS 13. 11., MS 15. 11., SG 9. 11. a 10. 11., JPM 9. 11., BCA 10. 11. a 18. 11., ING 4. 11., Gavekal 6. a 13. 11.) · research/house-views.md (EU obrana, Bernstein 19. 11.) · research/themes.md (#eu-defense / #nato-spending / #ukraine) · companies/CSG/dossier.md · state/calendar.md · `tools/portfolio.py`, `state/prices.json` (19. 11.)
- **Sell-side (web):** [JPM 12. 11. (investing.com)](https://de.investing.com/news/stock-market-news/jp-morgan-sieht-margen-von-csg-unter-druck-nachfrageverschiebung-bei-munition-belastet-3764380) · [JPM, DB (ad-hoc-news 19. 11.)](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/csg-aktie-erholung-nach-rekordtief/70536004) · [investing.com (BofA, konsenzus, srpnové ratingy)](https://uk.investing.com/equities/csg-nv) · [E15 18. 11.](https://www.e15.cz/byznys/burzy-a-trhy/strnadova-csg-za-tyden-ztratila-103-miliard-proc-analytici-stale-veri-ve-zdvojnasobeni-ceny-1437393) · [CC.cz 11. 11.](https://cc.cz/akcie-csg-po-vysledcich-spadly-o-petinu-na-nove-minimum-strnadova-zbrojovka-zhorsila-vyhled-marze/) · Bernstein 19. 11. (aktiencheck / wallstreet-online, zprostředkovaně přes dossier)
- **Governance:** [Hunterbrook 4. 5. 2026](https://hntrbrk.com/investigations/csg) · [Ekonomický deník – Kratochvíl](https://ekonomickydenik.cz/boj-miliardy-podil-strnad-csg-soud-exmanazerovi-kratochvilovi-nevyhovel/) · [kurzy.cz – Qube short 7/2026](https://zpravy.kurzy.cz/868620-akcie-csg-ve-stredu-vzrostly-nejsilneji-od-ipo-zacne-short-squeeze/) · [kurzy.cz – Qube 8/2026](https://zpravy.kurzy.cz/870928-qube-utika-z-shortu-csg-zmizelo-6-3-milionu-akcii-jenze-kde-je-vzala/)
- **Ceny a peers:** [boerse.de 20. 11.](https://www.boerse.de/aktien/CSG-NV-Aktie/NL0015073TS8) · [ls-tc](https://www.ls-tc.de/de/aktie/4347672) · [fxstreet 19. 11. (Praha 231,20 Kč)](https://www.fxstreet.cz/prazska-burza-odepsala-vice-nez-procento-vyrazne-ztracely-akcie-csg-19112026.html) · [fxstreet 20. 11.](https://www.fxstreet.cz/zpravodajstvi-210883.html) · StockAnalysis: [CSG](https://stockanalysis.com/quote/ams/CSG/), [RHM](https://stockanalysis.com/quote/etr/RHM/statistics/), [Renk](https://stockanalysis.com/quote/etr/R3NK/statistics/), [Hensoldt](https://stockanalysis.com/quote/etr/HAG/statistics/), [Leonardo](https://stockanalysis.com/quote/bit/LDO/statistics/), [BAE](https://stockanalysis.com/quote/lon/BA/statistics/), [Saab](https://stockanalysis.com/quote/sto/SAAB.B/statistics/), [Kongsberg](https://stockanalysis.com/quote/osl/KOG/statistics/), [GD](https://stockanalysis.com/stocks/gd/statistics/), [Colt CZ](https://stockanalysis.com/quote/pra/CZG/statistics/)
- **Neověřeno:** oficiální close 19. a 20. 11. (9,32 je nepotvrzený close patria.cz) · přesné datum a rozsah lock-upu (prospekt) · RSI 14 · aktuální (listopadové) multiples peers kromě RHM a Colt CZ · EBIT Kinetic Group samotné a synergie · rating a splatnosti dluhopisů · auditor · podíl minorit (Kratochvíl) na zisku · rozpor v pohybu backlogu Q3 · obsah Bernsteinova reportu (jen zprostředkovaně) · dnešní příčina poklesu −4,9 % (20. 11. bez firemní zprávy).

## Uložení (krok 15) – co aktualizovat (udělá hlavní běh)

- **Dossier `companies/CSG/dossier.md`:** signál 🟡 Sledovat (držet, nepřikupovat; IPO teze 🔴) s „co by ho zvrátilo“ z Verdiktu, nový řádek historie signálu s odkazem na v1, pracovní teze z kroku 2, scénáře 35/45/20 → 5,43 / 12,59 / 22,26 EUR, vážený výnos ~21 % p. a. vs. 14–18 %, body Potvrdí/Vyvrátí z kroku 13, KPI (doplnit Q3 book-to-bill 0,6, fixed/frame/soft backlog, rozpor v backlogu, hotovost 1,188 mld.), broker views (JPM a DB se šipkami z → na, srpnové ratingy, Jefferies), deník změn, řádek „Poslední deep dive: v1, 20. 11. 2026“.
- **`config/universe.yaml`:** `last_deep_dive: 2026-11-20` u CSG. **`state/state.json`:** odebrat CSG z `deep_dive_queue`.
- **`state/calendar.md`:** doplnit 9/2027 splatnost půjček subdodavatelům, ~Q1 2027 výsledky [Odhad], ~3/2028 FY2027 (konec horizontu), Q2 2028 EURENCO JV.
- **Claude Doc** `Deep dive: CSG (Czechoslovak Group) (CSG) – 20. 11. 2026` + odkaz v hlavičce tohoto souboru.

[Analýza uložena: companies/CSG/deep-dive-v1.md]
