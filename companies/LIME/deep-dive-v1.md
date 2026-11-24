# Deep dive: Neutron Holdings / Lime (LIME) – v1 – 24. 11. 2026

_Spuštěno na povel Tomáše (24. 11. 2026). Ve frontě byl první RHM, kvůli CMD 27. 11. je odložen (rozhodnutí Tomáše). Cena 19,69 USD (close 23. 11. 2026), kurzy ČNB 23. 11._

## Verdikt

- **Signál:** 🟡 **Sledovat: držet, nepřikupovat** (beze změny od onboardingu, sklon už ne negativní, ale neutrální). [Názor]
- **Scénáře (horizont ~1,5 roku, cíl k 12/2027 na forward 2028E):** bear 13,0 USD (−34 %, 30 %) · base 28,0 USD (+42 %, 50 %) · bull 48,2 USD (+145 %, 20 %). **Vážený cíl 27,5 USD = +40 %**, tj. ~25 % p. a. při 1,5 roku (18 % p. a. při 2 letech). [Odhad, Python]
- **Požadovaný výnos 16–22 % p. a.** Vážený výnos je nad ním, ale pod hranicí Buy (+50 %). Buy by vycházelo pod ~18,3 USD. [Odhad]
- **Velikost pozice:** rámec 4–6 % (nízká až střední conviction). Současná váha je **8,0 %**, tedy mírně převážená. Redukci teď nedoporučuju: lock-up končí 7.–9. 12. (uvolní se ~40 mil. akcií) a prodávat do převisu nabídky by bylo nevýhodné. Pokud cena před novými daty dojde k ~27 USD (vážený cíl), stáhnout na ~5 %. [Názor]
- **Co rozhodne:** přežití lock-upu bez propadu, guidance 2027 (23. 3. 2027) a letní sezóna 2027 (RVD na stejných trzích zpět do plusu).

## Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor | Sdílená mikromobilita (e-koloběžky ~2/3 flotily, e-kola ~1/3), Passenger Ground Transportation [Fakt] | [Quartr](https://web.quartr.com/m/companies/22606), [Quartr call](https://web.quartr.com/m/sources/s84334634395570170255971) |
| HQ, listing | San Francisco; Nasdaq LIME od 1. 7. 2026 (IPO 25 USD, 6,96 mil. akcií, GS a JPM leady) [Fakt] | [Business Wire](https://www.businesswire.com/news/home/20260630995454/en/Lime-Announces-Pricing-of-Initial-Public-Offering) |
| Cena, 52W | 19,69 USD (23. 11., +1,65 %); od IPO 17,51 (close 10. 11.) – 44,38 USD (27. 8.); −21 % pod IPO [Fakt] | [Trendlyne](https://us.trendlyne.com/us/equity/consensus-estimates/3569180/LIME/neutron-holdings-inc/), [quiverquant](https://www.quiverquant.com/stock/LIME/historical-prices/) |
| Akcie | 65,32 mil. v oběhu, opce 5,87 mil. (strike 9,28), RSU 3,51 mil.; zředěno (treasury) ~72,0 mil. [Fakt / výpočet] | [Quartr 10-Q](https://web.quartr.com/m/sources/s63883260915) |
| Market cap / EV | 1,29 mld. USD basic, 1,42 mld. zředěně; hotovost 417,7 mil. (+35,4 vázané), dluh 0 → **EV ~1,0 mld. USD** [Odhad, výpočet] | [Quartr rozvaha](https://web.quartr.com/m/sources/s55610614317) |
| Násobky | EV/adj. EBITDA 2026 (254) 3,9×; EV/(adj. EBITDA − SBC) 5,0×; P/E (GAAP, normalizovaný ~0,9–1,0 USD) ~20× [Odhad] | výpočet |
| Tržby TTM | 1,045 mld. USD (9M 835,0 + Q4 2025 210,1) [Fakt / výpočet] | [Quartr S-1/A](https://web.quartr.com/m/sources/s43591213088), [Q3 release](https://web.quartr.com/m/sources/s56735932526) |
| Marže 9M 2026 | adj. hrubá 51,2 % (GAAP 40,1 %), adj. EBITDA 25,2 %, EBIT 5,8 % (s jednorázovým SBC 35,8 mil.; bez něj 10,1 %), FCF 0,9 % [Fakt / výpočet] | [Quartr](https://web.quartr.com/m/sources/s52299237290) |
| Net debt / EBITDA | net cash ~418 mil. USD; revolver 200 mil. (JPM, do 2031) nečerpán [Fakt] | [Quartr](https://web.quartr.com/m/sources/s67995902145) |
| Free float / insideři | Uber 21,9 %, Sapphire (Lunate) 15,2 %, Fidelity 10,3 %, a16z 4,5 %, vedení 4,4 %; free float ~44 % [Odhad] | [Quartr S-1/A](https://web.quartr.com/m/sources/s74978584415) |
| CEO / CFO | Wayne Ting / Ann Gugino; předseda James Rowan (ex-CEO Volvo Cars) [Fakt] | [Quartr](https://web.quartr.com/m/sources/s52056267211) |
| Konsenzus | 8× Buy/OW, průměrný cíl 33,3 USD (27–37) [Fakt] | [TipRanks](https://www.tipranks.com/stocks/lime/forecast) |
| Likvidita | průměr ~380–400 tis. ks denně (~7,5–8 mil. USD), 23. 11. 318 tis. ks → **podprůměrná** vzhledem k velikosti [Fakt / Odhad] | [MarketBeat](https://www.marketbeat.com/instant-alerts/analyst-neutron-nasdaq-lime-given-new-3300-price-target-at-jpmorgan-chase-co-2026-11-04/) |
| RSI 14 | aktuální nenalezeno | – |

## Krok 1 – zdroj a kontext idey

Pozice Tomáše na Trading 212 (25 ks za 21,91 USD), nejspíš koupená kolem IPO. [Fakt, `config/portfolio.yaml`] Cena je pod IPO, protože hned první kvartál po IPO (3. 11.) přinesl EBITDA pod vlastní guidance a snížení výhledu FY26 z 265–285 na 253–255 mil. USD. Důvodem byl pokles RVD o 4,8 % (Austrálie ředí, LimePrime je levnější za jízdu, promo akce konkurence v Evropě). Akcie spadla 4. 11. o 27,8 %. [Fakt, [Quartr call](https://web.quartr.com/m/sources/s58480473875)] Mezitím firma ztratila Brusel (licence skončila 2. 7.), Denver (jediný operátor Veo) a Lisabon schválil zákaz koloběžek (do konce ledna 2027). [Fakt, [Belga](https://www.belganewsagency.eu/lime-withdraws-from-brussels-following-court-ruling-but-eyes-return), [CBS](https://www.cbsnews.com/colorado/news/veo-denver-scooters-contract-crashes-safety/), [DN](https://www.dn.pt/local-geral/cmara-de-lisboa-aprova-suspenso-das-trotinetas-partilhadas)]

Trh: Lime je největší operátor sdílené mikromobility (podíl 27 % globálně, 37 % v US podle S-1), víc než 3× větší než nejbližší konkurent. Odvětví se po krachu Birdu (2023) konsolidovalo a dnes je ziskové u tří hráčů (Lime, Voi, Dott). Lime podle Citizens jako jediný generuje kladný FCF v globálním měřítku. [Fakt, [Quartr S-1](https://web.quartr.com/m/sources/s50923324828), [Investing](https://www.investing.com/news/analyst-ratings/citizens-cuts-neutron-holdings-price-target-on-europe-competition-93CH-4998109)] Výhled: poptávka roste (MAU +16 %, nové megaměsta), ale přístup na trh určují města a tendry a regulace se v Evropě zpřísňuje (Paříž, Praha, Lisabon). [Názor]

## Krok 2 – teze (variant perception)

**Trh si myslí:** Lime je IPO, které hned v prvním kvartálu ukázalo, že jednotková ekonomika slábne (RVD dolů, konkurence, ztráty měst) a že adj. EBITDA přeceňuje skutečný zisk (FCF 9M jen 7 mil. USD). Proto ~4× EBITDA. [Názor]

**Já si myslím:** Na stejných trzích RVD dál roste o jednotky procent; pokles je z velké části mix (Austrálie, LimePrime s 8× vyšší frekvencí a 2× vyšším hrubým ziskem na jezdce). FCF 2026 stlačil růstový capex (flotila +26 %), ne zhoršení ekonomiky: vozidlo za ~1 300–1 500 USD se vrací za ~12 měsíců a odepisuje na 5 let. Dnešní cena implikuje, že „owner earnings“ po údržbovém capexu a SBC porostou jen ~2–3 % ročně (reverse DCF při 12 %). To je pro firmu s +20 % tržeb, net cash a dominantní škálou málo. [Názor, výpočet níže]

**Proč je trh vedle (a kde možná ne):** Trh extrapoluje jeden špatný kvartál a ztrátu několika měst. Skutečné riziko ale není marže, je to přístup na trh. Pokud by se zákazy koloběžek šířily jako v Paříži a Praze, část teze padá. Lime přitom umí přejít na e-kola (Paříž, Praha), takže zákaz koloběžek ≠ ztráta města. Variant perception je **mírná, ne silná**: edge je hlavně ve valuaci a v rozlišení mixu od ekonomiky, ne v informaci, kterou trh nemá. [Názor]

## Krok 3 – byznys model

- **Jak vydělává:** poplatky za jízdu (odemknutí + minuta) a předplatné (LimePass, nově LimePrime ~5,99 USD/měs., jízdy do 20 min za 2,50 USD). Prime: 8× víc jízd, 3× vyšší retence, ~2× vyšší adj. hrubý zisk na jezdce. ~12–13 % tržeb jde přes aplikaci Uber (exkluzivní integrace do 31. 12. 2028, Uber One). [Fakt, [Quartr](https://web.quartr.com/m/sources/s63103375622), [Quartr](https://web.quartr.com/m/sources/s67579856133)]
- **Geografie Q3 2026:** USA 114 mil. (+14 %), UK 76 (+18 %), Německo 38 (+33 %), ostatní 132 (+22 %); Austrálie přes +100 %. Reportuje jeden segment. [Fakt, [Quartr 10-Q](https://web.quartr.com/m/sources/s76726757489)]
- **Unit economics (klíčové metriky odvětví):** RVD (tržby na vozidlo a den) 8,77 USD v Q3 (−4,8 %), za 9M 7,77 USD (rovně r/r). Hotovostní marže ~50 % → ~4 USD/den/vozidlo, ~1 500 USD ročně na vozidlo za ~1 300–1 500 USD → návratnost ~12 měsíců. Účetní životnost 5 let (baterie 4). Údržbový capex ~5 % tržeb, zbytek capexu je růst. [Fakt, [Quartr S-1](https://web.quartr.com/m/sources/s47870864296), [Quartr GS konf.](https://web.quartr.com/m/sources/s86037737457140198964431), [Quartr CEO](https://web.quartr.com/m/sources/s61514193676987743863084)]
- **Nákladová struktura 2025 (% tržeb):** práce ~23, díly ~6, povolení ~3, provozovny ~3, ostatní ~12 → adj. hrubá marže ~53 %; D&A ~14 % → GAAP hrubá ~39 %. Marketing pod 2 % tržeb. [Fakt, [Quartr](https://web.quartr.com/m/sources/s46898374806)]
- **Moat:** škála (hustota flotily = dostupnost = poptávka), vlastní hardware a software, Uber jako akviziční kanál a licence (omezený počet operátorů). Slabiny: licence se obnovují v tendrech (Brusel prohrán), města mohou zakázat koloběžky, menší hráči s dluhovým financováním dělají promo. Moat je **střední a lokální**, ne globální. [Názor]
- **Produkt a recenze:** App Store 4,9★ (~35 tis. hodnocení), Trustpilot UK 1,2/5 (stížnosti na účtování, podporu, stav kol – typické pro odvětví). Nové e-kolo (menší kola, nižší rám, modulární díly) jezdí od 3/2026 v UK a v Paříži. Lisabon jako důvod zákazu uvádí 267 úrazů s převozem do nemocnice. [Fakt, [Apple](https://apps.apple.com/cz/app/lime-ridegreen/id1199780189), [Trustpilot](https://uk.trustpilot.com/review/limebike.com?page=6), [Dezeen](https://www.dezeen.com/2026/04/08/lime-bike/amp/), [DN](https://www.dn.pt/sociedade/trotinetas-267-acidentes-com-ida-ao-hospital-e-mais-de-oito-mil-retiradas-das-ruas)]

## Krok 4 – finance

| mil. USD | 2023 | 2024 | 2025 | 9M 2025 | 9M 2026 |
|---|---|---|---|---|---|
| Tržby | 522,0 | 686,6 | 886,7 | 676,7 | 835,0 (+23 %) |
| Adj. hrubá marže | 52,9 % | 53,7 % | 52,7 % | 54,3 % | 51,2 % |
| Adj. EBITDA | 99,8 | 153,4 | 218,1 | 185,0 | 210,1 |
| EBIT | −24,6 | 47,0 | 70,4 | 79,0 | 48,3 |
| SBC | 11,5 | 11,8 | 11,2 | 8,8 | 56,4 (35,8 jednoráz.) |
| Provozní CF | 81,2 | 169,0 | 214,8 | 179,1 | 163,9 |
| Capex (vozidla) | 80,1 (65,1) | 121,7 (104,5) | 111,1 (97,9) | 100,2 (90,5) | 156,6 (142,1) |
| FCF | 1,1 | 47,3 | 103,8 | 78,9 | 7,3 |
| Průměrná flotila (tis.) | 229 | 276 | 325 | 319 | 394 |
| RVD (USD) | 6,23 | 6,80 | 7,47 | 7,78 | 7,77 |

[Fakt, [Quartr S-1/A](https://web.quartr.com/m/sources/s53237902387), [non-GAAP](https://web.quartr.com/m/sources/s81411328462), [CF](https://web.quartr.com/m/sources/s58171005837), [10-Q KPI](https://web.quartr.com/m/sources/s69017858287)]

- **Kvalita zisku:** adj. EBITDA nezahrnuje SBC (normalizovaně ~55 mil./rok, nezaúčtovaných 85 mil. za RSU na 1,9 roku) ani odpisy vozidel (~14 % tržeb), které jsou skutečný náklad. Čistý zisk 9M 277,8 mil. je zkreslen rozpuštěním opravné položky k odloženým daním (289,1). Ztráty 2023–25 táhlo přecenění konvertibilek (77 / 41 / 125 mil.), ne provoz. [Fakt / Názor]
- **Přechodné vs. strukturální:** přechodné je ředění RVD Austrálií, jednorázové IPO SBC a vysoký růstový capex. Strukturální je tlak na ceny mimo velká města v západní Evropě a regulace. Sezónnost je silná: Q1 2026 adj. EBITDA jen 7,5 mil., Q3 118,4 mil. [Fakt / Názor]
- **FCF 2026:** 9M 7,3 mil. + Q4 (sezónně slabý) → FY ~20–40 mil. USD. [Odhad] Provozní CF FY ~200 mil., minus údržbový capex ~54 → „owner FCF“ ~145 mil., po SBC ~90 mil. [Odhad]

## Kroky 5–7 – alokace kapitálu, rozvaha, governance

- **Alokace kapitálu:** priority flotila, technologie, selektivní M&A, rezerva; buyback ani dividenda nejsou v plánu (revolver je navíc omezuje). Akvizice Neuron Mobility Canada za ~8,9 mil. USD. Capex FY26 172–177 mil. (sníženo z 180–185). [Fakt, [Quartr](https://web.quartr.com/m/sources/s81822417829)] [Názor] Bez číselného cíle na návratnost kapitálu; plus je, že capex se dá rychle zastavit (flotila je modulární).
- **Rozvaha:** hotovost 417,7 mil. USD (+35,4 vázané), žádný dluh, revolver 200 mil. (53 mil. akreditivy, volných 147), kovenanty čistá páka max. 3,25×. Operativní leasingy jen 52 mil. Pracovní kapitál ~391 mil. Odložená daňová pohledávka 293 mil. (limity §382 po změně vlastnictví). Rozvaha je **silná**. [Fakt, [Quartr](https://web.quartr.com/m/sources/s67995902145), [Quartr](https://web.quartr.com/m/sources/s49064013980)]
- **Vlastníci:** Uber 21,9 % (strategický; prodej nic do 7/2027, max. 50 % do 1/2028, max. 75 % do 7/2028; lock-up padá, pokud skončí integrační dohoda), Sapphire/Lunate 15,2 %, Fidelity 10,3 %, a16z 4,5 %, vedení 4,4 %. Jedna třída akcií, staggered board (3 třídy), 4 ze 7 nezávislí, v radě COO Uberu. [Fakt, [Quartr](https://web.quartr.com/m/sources/s74978584415), [Quartr](https://web.quartr.com/m/sources/s62852769257)]
- **Lock-up:** 160 dní od prospektu → **7.–9. 12. 2026**, ~40,1 mil. akcií (bez Uberu), tj. ~60 % akcií v oběhu; GS a JPM mohou uvolnit dřív. Dosavadní datum v repu (~27. 12.) bylo chybné. [Fakt, [S-1/A](https://www.sec.gov/Archives/edgar/data/0001699963/000162828026044471/neutronholdingsinc-sx1a1.htm), [Brimind](https://brimindinvest.com/lockup-radar/lime)]
- **Governance – negativa:** materiální slabina v kontrolách (málo účetních) za 2023–2025, trvá k 30. 9. 2026; going concern odstavec v auditu 2025 (KPMG) vyřešilo IPO; prezident Kraus odešel 22. 5. 2026; advokátní „vyšetřování“ (Levi & Korsinsky, BG&G), žaloba zatím nepodaná; spoluzakladatel Brad Bao osobně žalovaný v RICO sporech kolem Cere Network (Lime není strana). Odměny: výkonnostní opce CEO až při market capu 4 mld. USD po 90 dní (sladěno s akcionáři). [Fakt, [Quartr](https://web.quartr.com/m/sources/s66859069683), [Quartr](https://web.quartr.com/m/sources/s73970593512), [Quartr](https://web.quartr.com/m/sources/s44660700133), [IBTimes](https://www.ibtimes.co.uk/lime-chairman-brad-bao-faces-mounting-rico-fraud-claims-market-makers-tied-scheme-1794720)]

## Krok 8 – požadovaný výnos

Baseline: pasivní alternativa (S&P 500 / ACWI) ~8–9 % p. a. na horizontu 1–2 let. [Odhad] Faktory specifické pro Lime:
1. **Regulace měst (zvyšuje, výrazně):** binární ztráty trhů (Brusel, Denver, Lisabon, Praha pro koloběžky) mohou ubrat tržby skokově.
2. **Čerstvé IPO s materiální slabinou a snížením guidance (zvyšuje):** důvěryhodnost managementu zatím neprokázaná, lock-up 7.–9. 12. a podprůměrná likvidita.
3. **Sezónnost a konkurence v Evropě (zvyšuje mírně):** hráči s levným dluhem mohou promo držet déle.
4. **Net cash 418 mil. a kladné provozní CF (snižuje):** riziko ředění nebo bankrotu (Bird) je minimální, capex je flexibilní.
5. **Strategický akcionář Uber a exkluzivní integrace do 2028 (snižuje):** stabilní kanál ~13 % tržeb a možný kupec.

Požadovaný výnos odvozuji na **16–22 % p. a.**: rizika regulace a čerstvého IPO převažují nad polštářem z rozvahy. Horizont ~1–1,5 roku: lock-up (12/2026), guidance 2027 (3/2027) a letní sezóna 2027 (výsledky Q3 2027 v listopadu) tezi potvrdí nebo vyvrátí. [Názor]

## Krok 9 – valuace

**Peers (forward 2026E / 2027E EV/EBITDA):** Uber 11,7× / 9,2× (23. 11.), Lyft 7,1× / 4,9× (20. 10.); Voi a Dott soukromé (Voi TTM adj. EBITDA 54 mil. EUR, net leverage 0,94×); Bolt sekundárně 6,8–8,4 mld. USD. LIME 3,9× 2026E. [Fakt, [MarketScreener Uber](https://www.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/valuation/), [MarketScreener Lyft](https://in.marketscreener.com/quote/stock/LYFT-INC-56481539/valuation/), [MFN Voi](https://mfn.se/a/voitechnology/voi-technology-ab-publ-publishes-third-quarter-report-2026)] Proti Lyftu je Lime levnější, ale jeho EBITDA nese vyšší odpisy flotily, takže diskont je částečně oprávněný. [Názor]

**Reverse DCF:** EV ~1,0 mld. USD; owner FCF 2026 po údržbovém capexu a SBC ~90 mil. USD. Při diskontní sazbě 12 % cena implikuje trvalý růst jen **~2–3 % ročně**. [Odhad, výpočet] Tržby přitom rostou +20–23 % a flotila +26 %.

**Scénáře** (cíl k 12/2027 na forward 2028E; průměr metody EV/(adj. EBITDA − SBC) + čistá hotovost a metody P/E 2028E; 74 mil. akcií po ~3% ředění; [Odhad, Python]):

| Scénář | P | Tržby 2027 / 2028 | Adj. EBITDA 2028 (marže) | Násobek EV/(EBITDA−SBC) · P/E | EPS 2028 | Cíl | Výnos |
|---|---|---|---|---|---|---|---|
| Bear: konkurence a zákazy se šíří, RVD dál dolů, převis po lock-upu | 30 % | 1,15 / 1,21 mld. (+7 %, +6 %) | 255 mil. (21 %) | 4× · 10× | 0,83 | **13,0 USD** | −34 % |
| Base: RVD na stejných trzích stabilní, mix ředí, marže mírně roste (CFO: „normálnější expanze v 2027“) | 50 % | 1,21 / 1,35 mld. (+13 %, +12 %) | 339 mil. (25 %) | 6× · 16× | 1,59 | **28,0 USD** | +42 % |
| Bull: Evropa se zracionalizuje, Prime zvedá frekvenci, nové megaměsta | 20 % | 1,27 / 1,49 mld. (+19 %, +17 %) | 417 mil. (28 %) | 8× · 22× | 2,26 | **48,2 USD** | +145 % |

**Vážený cíl 27,5 USD (+40 %)** → ~25 % p. a. při 1,5 roku, 18 % p. a. při 2 letech, vs. požadovaných 16–22 % p. a. → **mírně nad požadavkem, pod hranicí Buy** (+50 % by vyžadovalo cenu ~18,3 USD). Rozptyl scénářů je široký (13–48 USD), což snižuje conviction. [Odhad / Názor]

Citlivost: P/E metoda (GAAP, daň 25 % po rozpuštění opravné položky) je v base o ~5 USD konzervativnější než EV metoda, protože odpisy flotily jsou vysoké. Pokud by trh dál oceňoval Lime na ~4× EBITDA i v 2027, base by vycházel kolem 22 USD (+12 %). [Odhad]

## Krok 9b – co píšou analytici

**Přímé zmínky (všichni upisovatelé IPO):**

| Datum | Instituce | Rating / cíl | Co říká |
|---|---|---|---|
| 9. 11. 2026 | Jefferies (Colantuoni) | Buy, 35 USD (potvrzeno) | – |
| 4. 11. 2026 | Goldman Sachs (Sheridan) | Buy, 40 → **37** USD | tlak na marže |
| 4. 11. 2026 | JPM (Anmuth) | Overweight, 38 → **33** USD | – |
| 4. 11. 2026 | Needham (McTernan) | Buy, 36 → **29** USD | jmenovitě promo akce **Voi** |
| 4. 11. 2026 | Citizens JMP (Boone) | Mkt Outperform, 33 → **27** USD | Lime jediný FCF-pozitivní operátor, konkurenti se k racionálním cenám vrátí časem |
| 3.–4. 11. 2026 | Evercore (Mahaney) | Outperform, 40 → **35** USD | – |
| 2. 11. 2026 | KeyBanc | Overweight, 37 USD | – |
| ~26. 10. 2026 | Citizens JMP | 45 → 33 USD | před výsledky |

[Fakt, [TipRanks](https://www.tipranks.com/stocks/lime/forecast), [Investing GS](https://www.investing.com/news/analyst-ratings/goldman-sachs-cuts-neutron-holdings-stock-price-target-on-margin-pressure-93CH-4997876), [Investing Needham](https://www.investing.com/news/analyst-ratings/needham-cuts-neutron-holdings-stock-price-target-on-competition-93CH-4998406), [Investing Citizens](https://www.investing.com/news/analyst-ratings/citizens-cuts-neutron-holdings-price-target-on-europe-competition-93CH-4998109)]

V broker reportech v research logu (GS, MS, JPM, SG, BCA aj.) Lime jménem nefiguruje, jen nepřímo přes témata. [Fakt]

**Témata #us-consumer / #eu-consumer:**
- MS Gapen (6. 11.): dvourychlostní spotřebitel, reálná spotřeba US 2027 zpomalí na 2,0 % (log 2026-11 · MS 6. 11.).
- MS Sunday Start (22. 11.): reálné výdaje za říjen jen +0,1 % m/m (log 2026-11 · MS 22. 11.).
- Gavekal: rozpor – C. Gave (13. 11.) vyhnout se US a EU spotřebitelským akciím vs. Tan (10. 11.) K-ekonomika se narovnává, US spotřebitel pozitivně (log 2026-11 · Gavekal 10. a 13. 11.).
- UBP (11. 11.): Consumer Discretionary UW, LIME mezi nepřímo dotčenými (log 2026-11 · UBP 11. 11.).
- SG MAP (20. 11.): long US Consumer Discretionary EW kvůli nižším cenám paliv a odolné zaměstnanosti (log 2026-11 · SG 20. 11.).

**Konsenzus vs. rozpory:** Sell-side se shoduje, že teze trvá (8× Buy), ale cíle se po Q3 rozestoupily na 27–37 USD; průměr 33 USD je nad mým váženým cílem 27,5 USD a blízko base/bull. Klíčový rozpor je délka cenové války: Citizens čeká racionalizaci, Needham vidí Voi jako trvalý tlak (Voi roste +53 % při RVD +10 %, tedy bere podíl). To potvrzuje můj bear scénář jako reálný (30 %), ne okrajový. Makro banky jsou ke spotřebiteli rozpolcené, pro Lime (nízká cena jízdy) je to druhořadé. [Názor]

**Z grafů:** k Lime ani mikromobilitě nic.

## Krok 10 – base rate

IPO, která v prvních výsledcích snížila výhled a spadla o 20–30 %: Eventbrite (−27 % v 5/2019, nakonec prodán za 4,50 USD vs. IPO 23), Oatly (−21 % v 11/2021, později reverse split), Allbirds (z 15 USD pod 2 USD, prodán za 39 mil.), Cerebras 2026 (−16 %, 45 % pod IPO). Protipříklad Stitch Fix (po propadu 3× IPO cena do 9 měsíců, pak zase dolů). Ve vzorku převažují špatné výsledky. [Fakt, [Fortune](https://fortune.com/2019/05/02/eventbrite-stock-plunges/), [Fool Oatly](https://www.fool.com/investing/2021/11/15/why-oatly-stock-plunged-today), [AOL Allbirds](https://www.aol.com/rise-fall-allbirds-silicon-valleys-132519824.html), [TechCrunch Stitch Fix](https://techcrunch.com/2017/12/19/stitch-fix-is-crashing-after-its-first-ever-earnings-report/?ncid=rss)]

Rozdíl: Eventbrite, Oatly a Allbirds byly ztrátové a pálily hotovost. Lime má kladné provozní CF, net cash a kladný EBIT. Bird zkrachoval s nulovou ekonomikou vozidla a dluhem; Lime je jeho opak. Base rate proto beru jako **varování pro sentiment** (nízké násobky mohou vydržet), ne jako precedens bankrotu. [Názor]

## Krok 11 – rizika (podle závažnosti) a nejsilnější protiargument

1. **Regulace a tendry:** Brusel, Denver, Lisabon (koloběžky), Praha (koloběžky), Řím (pokuta 2,675 mil. EUR všem operátorům, končí smlouva), tender TfL v Londýně 2027, Frankfurt a Berlín. UK je 21 % tržeb. [Fakt]
2. **Konkurence v Evropě:** Voi (RVD +10 %, levný revolver 150 mil. EUR), Dott, Bolt (příprava IPO) mohou držet promo dlouho. [Fakt / Názor]
3. **Lock-up 7.–9. 12. 2026:** ~40 mil. akcií vs. odhadem ~11–15 mil. akcií dnes volně obchodovatelných a obrat ~0,4 mil. denně. [Fakt / Odhad]
4. **Důvěryhodnost:** materiální slabina, guidance miss hned po IPO, advokátní vyšetřování (případná žaloba = overhang). [Fakt]
5. **Kvalita zisku:** SBC ~55 mil./rok, odpisy flotily ~14 % tržeb, FCF 2026 skoro nulový. [Fakt / Odhad]
6. **Závislost na Uberu:** ~13 % tržeb, dohoda do 2028, Uber ji může za určitých okolností ukončit. [Fakt]
7. **Makro a počasí:** sezónnost, FX (~70 % tržeb mimo US), cla na vozidla. [Fakt / Názor]

**Nejsilnější protiargument:** Mikromobilita je komodita, kde ceny určuje nejagresivnější hráč s levným kapitálem a přístup na trh určují politici. Lime nemá cenovou sílu (proto nenásleduje promo a ztrácí RVD) a každá ztráta města je trvalá. Pak je 4× EBITDA fér a FCF zůstane skoro nulový, protože růst flotily jen nahrazuje ztracené trhy. [Názor]

## Krok 12 – conviction a velikost pozice

Conviction **nízká až střední**: variant perception je mírná (valuační, ne informační), rozptyl scénářů velký (13–48 USD) a klíčová data přijdou až v 3/2027 a v létě 2027. Rámcová velikost **4–6 %**. Současná váha Tomáše **8,0 %** (11 009 CZK z 138 306 CZK, `tools/portfolio.py`, kurzy ČNB 23. 11.) → **mírně převážená**. Michal LIME nedrží. [Fakt / Názor]

Doporučení: neprodávat do lock-upu; nepřikupovat (Buy až pod ~18,3 USD a i tak by pozice vyšla nad rámec). Při růstu k ~27 USD bez nových dat stáhnout na ~5 %. [Názor] Nejsem finanční poradce.

## Krok 13 – katalyzátory a monitoring

| Datum | Událost | Potvrdí | Vyvrátí |
|---|---|---|---|
| 7.–9. 12. 2026 | Konec lock-upu (~40 mil. akcií) | absorpce bez propadu pod ~17,5 USD, nákupy insiderů | blokové prodeje Sapphire/Fidelity s diskontem, propad pod 15 USD |
| 12/2026 – 1/2027 | Lisabon stažení koloběžek; tendry Frankfurt, Berlín; soud o Brusel | přechod na e-kola v Lisabonu, výhra tendrů | další zákaz ve velkém městě (Londýn, Berlín, Madrid) |
| 23. 3. 2027 | Výsledky Q4/FY26 + guidance 2027 | Q4 tržby 240–250, EBITDA 43–45; guidance 2027 s tržbami +12 % a víc a marží EBITDA ≥ 24 %; plán na odstranění materiální slabiny | další škrt, guidance 2027 bez expanze marže, FCF FY26 záporné |
| 5/2027, 8/2027 | Q1 a Q2 2027 | RVD na stejných trzích kladné, celkové RVD zpět k 0 % r/r, Prime roste | RVD dál −3 % a hůř, ztráta podílu ve UK/DE |
| 7/2027 | Konec 12M lock-upu Uberu | Uber drží nebo přikupuje | Uber prodává / vypovídá integraci |

KPI pro Tracker: RVD (celkové a na stejných trzích), flotila, MAU, adj. EBITDA marže, FCF a capex, podíl tržeb přes Uber, licence a tendry. [Názor]

## Krok 14 – zdroje

- **Quartr:** [firma](https://web.quartr.com/m/companies/22606) · [Q3 2026 event](https://web.quartr.com/m/events/724023) · [10-Q Q3](https://web.quartr.com/m/documents/3955555) · [release Q3](https://web.quartr.com/m/documents/3955556) · [slidy Q3](https://web.quartr.com/m/documents/4279953) · [prepared remarks](https://web.quartr.com/m/documents/4036763) · S-1/A: [shrnutí](https://web.quartr.com/m/sources/s53237902387), [akcionáři](https://web.quartr.com/m/sources/s74978584415), [unit economics](https://web.quartr.com/m/sources/s47870864296), [Uber smlouva](https://web.quartr.com/m/sources/s60834738760), [lock-up Uberu](https://web.quartr.com/m/sources/s62852769257) · call Q3: [RVD](https://web.quartr.com/m/sources/s58480473875), [konkurence](https://web.quartr.com/m/sources/s60874715090315120202345), [alokace kapitálu](https://web.quartr.com/m/sources/s81822417829)
- **SEC:** [S-1/A](https://www.sec.gov/Archives/edgar/data/0001699963/000162828026044471/neutronholdingsinc-sx1a1.htm) · [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0001699963/000162828026073057/lime-20260930.htm)
- **Research log:** log 2026-11 · MS 6. 11., MS 22. 11., Gavekal 10. a 13. 11., UBP 11. 11., SG 20. 11.; `research/themes.md` (#us-consumer)
- **Web:** [Business Wire – IPO](https://www.businesswire.com/news/home/20260630995454/en/Lime-Announces-Pricing-of-Initial-Public-Offering) · [Trendlyne – cena 23. 11.](https://us.trendlyne.com/us/equity/consensus-estimates/3569180/LIME/neutron-holdings-inc/) · [quiverquant – historie cen](https://www.quiverquant.com/stock/LIME/historical-prices/) · [TipRanks – analytici](https://www.tipranks.com/stocks/lime/forecast) · [MarketBeat JPM](https://www.marketbeat.com/instant-alerts/analyst-neutron-nasdaq-lime-given-new-3300-price-target-at-jpmorgan-chase-co-2026-11-04/) · [Finviz – Q3](https://finviz.com/news/415050/lime-tops-q3-estimates-but-falling-revenue-per-vehicle-and-an-ebitda-guidance-cut-mark-its-first-real-soft-spot-since-the-ipo) · [Belga – Brusel](https://www.belganewsagency.eu/lime-withdraws-from-brussels-following-court-ruling-but-eyes-return) · [DN – Lisabon](https://www.dn.pt/local-geral/cmara-de-lisboa-aprova-suspenso-das-trotinetas-partilhadas) · [TravelDailyNews – Lisabon](https://www.traveldailynews.com/destinations/lisbon-shared-electric-scooter-suspension-2027/) · [CBS – Denver](https://www.cbsnews.com/colorado/news/veo-denver-scooters-contract-crashes-safety/) · [expats.cz – Praha](https://www.expats.cz/czech-news/article/prague-to-ban-shared-e-scooters-from-january-over-safety-concerns) · [Il Sole 24 Ore – Řím](https://en.ilsole24ore.com/art/27-million-fine-for-bird-dott-and-lime-over-free-micromobility-passes-in-rome-AJ8riQg) · [MFN – Voi Q3](https://mfn.se/a/voitechnology/voi-technology-ab-publ-publishes-third-quarter-report-2026) · [micromobility.io – Dott](https://micromobility.io/news/45k-new-vehicles-22-margins-the-shift-in-dotts-q2-2026) · [Sacra – Bolt](https://sacra.com/c/bolt-technology/) · [TechCrunch – Bird](https://techcrunch.com/2023/12/20/bird-bankruptcy) · [MarketScreener – Uber](https://www.marketscreener.com/quote/stock/UBER-TECHNOLOGIES-INC-57860975/valuation/), [Lyft](https://in.marketscreener.com/quote/stock/LYFT-INC-56481539/valuation/) · [Brimind – lock-up](https://brimindinvest.com/lockup-radar/lime) · [Stockhouse – BG&G](https://stockhouse.com/news/press-releases/2026/11/20/bronstein-gewirtz-grossman-llc-initiates-an-investigation-into-allegation2) · [Apple App Store](https://apps.apple.com/cz/app/lime-ridegreen/id1199780189) · [Trustpilot](https://uk.trustpilot.com/review/limebike.com?page=6) · base rate: [Fortune](https://fortune.com/2019/05/02/eventbrite-stock-plunges/), [Fool Oatly](https://www.fool.com/investing/2021/11/15/why-oatly-stock-plunged-today), [AOL Allbirds](https://www.aol.com/rise-fall-allbirds-silicon-valleys-132519824.html), [TechCrunch Stitch Fix](https://techcrunch.com/2017/12/19/stitch-fix-is-crashing-after-its-first-ever-earnings-report/?ncid=rss)
- **Výpočty:** valuace v Pythonu (`companies/LIME/valuation-v1.py`), reverse DCF ručně ověřený výpočtem, váhy `tools/portfolio.py`.

[Analýza uložena: companies/LIME/deep-dive-v1.md]
