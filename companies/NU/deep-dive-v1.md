# Deep dive: Nu Holdings (NU) – v1 – 26. 11. 2026

_Spuštěno z fronty (NU předběhl IOVA podle vah 25. 11.). Verze v1, předchozí verze neexistuje. Cena pro výpočty 12,36 USD (close 25. 11. 2026, +4,2 %, Yahoo). Váhy `tools/portfolio.py` k 25. 11. (kurzy ČNB 25. 11.). Výpočty v `companies/NU/valuation-v1.py`._

## Verdikt

- **Signál:** 🟡 **Sledovat: držet, přikupovat až pod ~11,4 USD** nebo po potvrzení teze na Investor Day a ve Q4 (beze změny od onboardingu, sklon mírně pozitivní). [Názor]
- **Teze v jedné větě:** Trh oceňuje Nu jako brazilskou banku před úvěrovým cyklem (10,5× konsenzu zisku 2027, P/TBV ~4,5×, nejníž za 3 roky). I když zisk poroste jen ~20 % ročně, tedy o ~15–20 % pod konsenzem, a násobek se nezvedne, vychází výnos kolem požadované laťky. Na Buy je ale potřeba buď nižší cena, nebo důkaz, že růst NPL je mix, ne cyklus. [Názor]
- **Scénáře (horizont 2 roky, cíl k 11/2028 na forward zisk 2029E):** bear 7,96 USD (−36 %, 25 %) · base 17,10 USD (+38 %, 50 %) · bull 26,26 USD (+112 %, 25 %). **Vážený cíl 17,10 USD = +38 % za 2 roky, ~17,6 % p. a.** [Odhad, Python]
- **Požadovaný výnos 14–18 % p. a.** Vážený výnos je v horní části pásma, ale pod hranicí Buy (+50 %). Buy vychází pod **~11,4 USD** (52W minimum je 11,20). [Odhad]
- **Velikost pozice:** Tomáš rámec 4–6 % (střední conviction), dnes **5,7 %**, tedy v rámci, horní hrana. Michal rámec 2–3 %, dnes **3,6 %**, tedy mírně převážený. [Názor]
- **Co rozhodne:** Investor Day 8. 12. 2026 (cíle ROE a alokace kapitálu), Q4 2026 24. 2. 2027 (NPL a výhled 2027), Q1 2027 (sezónně nejhorší kvartál pro úvěry) a cesta Selic a BRL v 2027.

## Krok 0 – snapshot

| Metrika | Hodnota | Zdroj |
|---|---|---|
| Sektor / subsektor | Diversified Banks (GICS). Digitální banka a finanční platforma: Brazílie, Mexiko (od 3Q26 banka), Kolumbie, nově Nu US a Nu Global [Fakt] | [Quartr](https://web.quartr.com/m/companies/11343), [Quartr release Q3](https://web.quartr.com/m/sources/s84692159050) |
| HQ, listing, ticker | Provoz São Paulo, holding Nu Holdings Ltd. (Kajmany). NYSE: NU, BDR ROXO34 v Brazílii [Fakt] | [Quartr release](https://web.quartr.com/m/sources/s74975985506), dossier |
| Cena, 52W | **12,36 USD** (25. 11., +4,2 %). 52W 11,20–18,98 USD. Close 20. 11. byl 11,27 USD, tedy jen 0,6 % nad minimem [Fakt] | Yahoo (zadání), [StockAnalysis](https://stockanalysis.com/stocks/nu/), [StockAnalysis historie](https://stockanalysis.com/stocks/nu/history/) |
| Akcie, market cap | 4,84 mld. akcií ([StockAnalysis](https://stockanalysis.com/stocks/nu/)); 20-F: 3 838,0 mil. třídy A + 1 022,6 mil. třídy B k 1. 3. 2026 ([Quartr 20-F](https://web.quartr.com/m/sources/s78165777277)). Market cap **59,8 mld. USD** [Fakt / výpočet] | výpočet |
| EV, net debt / EBITDA | U banky nedává smysl. Místo toho kapitál 9,9 mld. USD (regulované entity + holding), čisté úvěry / dostupný funding 57 % [Fakt] | [Quartr slide 25](https://web.quartr.com/m/sources/s64063137101) |
| Tržby | Manažerské hrubé tržby TTM 22,3 mld. USD (Q4 25–Q3 26: 4,86 + 5,32 + 5,88 + 6,26). IFRS tržby Q3 26 5,82 mld. (+39 % r/r v USD) [Fakt / výpočet] | [Quartr slide 20](https://web.quartr.com/m/sources/s53721092878), [Quartr IFRS P&L](https://web.quartr.com/m/sources/s77442654670) |
| Marže (banka) | ROE 32 %, efficiency ratio 19,3 %, NIM 22,5 %, risk-adjusted NIM 12,1 % (rekurentně 12,7 %), čistý zisk / manažerské tržby 17,4 % (Q3). Hrubá marže, EBIT a FCF u banky nemají smysl [Fakt / výpočet] | [Quartr release](https://web.quartr.com/m/sources/s85040634664) |
| Zisk, násobky | Čistý zisk TTM 3,92 mld. USD → **P/E TTM 15,3×**. P/E na konsenzus EPS: 13,3× 2026 (adj. 0,93), **10,5× 2027 (1,18)**, 8,2× 2028 (1,51). Vlastní kapitál 14,34 mld. → **P/B 4,2×**, P/TBV ~4,5× (goodwill + nehmotná aktiva ~1,0 mld. k YE25) [Fakt / Odhad, výpočet] | [Quartr slide 32](https://web.quartr.com/m/sources/s50729500569), [20-F rozvaha](https://web.quartr.com/m/sources/s67357405855), [StockAnalysis forecast](https://stockanalysis.com/stocks/nu/forecast/), [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nyse/nu/stock-forecast) |
| Free float / insideři | David Vélez ~18,6 % akcií, ale **74,4 % hlasů** (třída B má 20 hlasů). Cristina Junqueira ~2,7 % akcií, 9,9 % hlasů. Free float ~78 % [Fakt / Odhad, výpočet] | [Quartr 20-F](https://web.quartr.com/m/sources/s78165777277), [poznámky](https://web.quartr.com/m/sources/s43206451150) |
| CEO / CFO | David Vélez (zakladatel, CEO, předseda). CFO Rob Livingston od 13. 7. 2026 (dřív CFO Visa pro Severní Ameriku a Capital One), nahradil Guilherme Laga [Fakt] | [Quartr slide 3](https://web.quartr.com/m/sources/s49781664386), [Yahoo/GuruFocus](https://finance.yahoo.com/markets/stocks/articles/nu-holdings-shares-down-22-150833630.html) |
| IR | [investors.nu](https://www.investidores.nu/en/) | |
| Konsenzus | Buy: 23 analytiků (14 Strong Buy, 5 Buy, 3 Hold, 1 Sell), průměrný cíl 17,63 USD (medián 17,80, rozpětí 12–23) k 20. 11. Přehled k 24. 11. uvádí 17,41 USD [Fakt] | [StockAnalysis forecast](https://stockanalysis.com/stocks/nu/forecast/), [StockAnalysis](https://stockanalysis.com/stocks/nu/) |
| Likvidita | V listopadu typicky 38–90 mil. akcií denně, 13. 11. 153 mil. a 26. 10. 340 mil. → zhruba 0,5–1,1 mld. USD denně. Vzhledem k velikosti **nadprůměrná** [Fakt / Odhad] | [StockAnalysis historie](https://stockanalysis.com/stocks/nu/history/) |
| RSI 14 | **45,1** (Wilder, closy 15. 10.–25. 11., 24. 11. dopočten) → neutrální [Odhad, výpočet] | `valuation-v1.py` |
| Beta | 0,97 [Fakt] | [StockAnalysis](https://stockanalysis.com/stocks/nu/) |

## Krok 1 – zdroj a kontext idey

Stávající pozice: Tomáš na t212 (prům. nákupka 11,35 USD) a Michal na t212 (11,20 USD), dossier založen při onboardingu 19. 11. 2026. Datum nákupu v repu není. [Fakt, `config/portfolio.yaml`]

**Proč je cena tam, kde je (YTD −29 %, [log 2026-11 · GS 20. 11.]):** [Fakt, zdroje u bodů]
- **Červen 2026:** BofA snížil na Sell s cílem 10 USD (z 16) a Susquehanna na Neutral s cílem 13 USD ([Nasdaq/Fool 3. 6.](https://www.nasdaq.com/articles/it-too-soon-call-bottom-nu-holdings-stock)). Citi snížil na Neutral s cílem 13 USD (z 18), protože růst úvěrů a cost of risk spolu podle něj korelují na ~90 % a normalizované ROE vidí ~25 % ([Brasil247](https://www.brasil247.com/brazilstockguide/?p=5241), [NeoFeed](https://neofeed.com.br/negocios/apos-bofa-citi-rebaixa-nubank-por-risco-na-carteira-de-credito/en/)). Do toho přišla výměna CFO.
- **26. 10. 2026:** Lula vyhrál druhé kolo (51,8 %). NU zavřel na 12,59 USD z 15,16 (**−17 %**, vnitrodenně až −20 %, nejhorší den v historii akcie). EWZ ztratil ~21 %, INTR −36 %, STNE −29 % ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy), [TIKR](https://www.tikr.com/blog/stoneco-sinks-29-inter-co-down-36-pagseguro-down-25-on-lulas-unexpected-election-win), [StockAnalysis historie](https://stockanalysis.com/stocks/nu/history/)).
- **29. 10.:** Itaú BBA snížil cíl na 15 USD a varoval, že nejhorší může teprve přijít ([Seu Dinheiro](https://www.seudinheiro.com/2026/empresas/e-agora-nubank-itau-bba-corta-preco-alvo-e-alerta-o-pior-ainda-pode-estar-por-vir-miql/)).
- **13. 11.:** po Q3 akcie +11,75 % na 13,22 USD, pak během „dokonalé bouře“ v EM měnách (BRL ~−7,5 % od 4. 11.) spadla do 20. 11. na 11,27 USD ([log 2026-11 · GS 20. 11.], `research/themes.md` #usd/#em-fx).

**Trh a výhled:** Nu má v Brazílii 120 mil. klientů (65 % dospělých) a je č. 1 finanční aplikace s 86 mil. MAU ([Quartr slide 7](https://web.quartr.com/m/sources/s71315715920)). Růstový prostor je hlavně mimo Brazílii: penetrace kreditních karet je v Mexiku 12 % a v Kolumbii 14 % proti 75–80 % v Brazílii ([Quartr call](https://web.quartr.com/m/sources/s68401852961779112280434)). Vélez bere jako base case Mexiko ve velikosti ~70 % Brazílie, v upside variantě stejně velké ([Quartr call](https://web.quartr.com/m/sources/s55845031399732943749951)). Krátkodobě rozhoduje brazilské makro: HDP 2027 0,6–1,2 %, Selic 12,5–13,75 % ke konci 2027 (GS, SG, MS) a trh dokonce nacenil 15 % (ING). [Fakt, `research/themes.md` #latam] [Názor] V horizontu 2–3 let se Nu mění z „brazilské karty“ na regionální banku s druhým motorem v Mexiku a opcí na USA, a právě to je zdroj růstu i rizika.

## Krok 2 – teze (variant perception)

**Co si myslí trh:** Brazilská úvěrová páka na zadlužené domácnosti přichází na konec cyklu: NPL 90+ roste (7,3 %), náklady na riziko rostou rychleji než úvěry (+73 % r/r v USD) a nová Lulova vláda drží Selic vysoko a BRL slabý. Sell-side odhady jsou podle trhu příliš vysoko: Itaú BBA je pod konsenzem o 19 % (2027) a 22 % (2028). Dnešní cena odpovídá **10,5× konsenzu EPS 2027**. Reverse excess-return model ukazuje, že při nákladech vlastního kapitálu (ke) 13–14 % trh počítá s tím, že ROE během deseti let klesne z 30 % na **~24–27 %** při růstu knihy z 25 % na 5 %. To je zhruba normalizované ROE ~25 % podle Citi. [Fakt / Odhad, `valuation-v1.py`]

**Co si myslím já:**
1. **Růst NPL je z velké části mix, ne jen cyklus.** Podíl úročených zůstatků (IEP) v portfoliu vzrostl na 61 % z 59 %. Přepočteno na IEP se **rané delikvence 15–90 zlepšily z 8,2 na 8,0 %** a jen NPL 90+ vzrostlo na 12,1 % (z 11,6 %) ([Quartr release](https://web.quartr.com/m/sources/s44417884325)). Rané delikvence jsou předstihový ukazatel. Tvorba opravných položek kryje novou tvorbu NPL 15+ na 102 % a krytí 90+ je 234 % ([Quartr call](https://web.quartr.com/m/sources/s47546098355462028682805), [slide 18](https://web.quartr.com/m/sources/s68951139510)). [Fakt / Názor]
2. **ROE stojí na nákladech, ne jen na úvěrech.** Náklady na obsluhu klienta jsou 1,1 USD měsíčně při ARPAC 17,7 USD, efficiency ratio 19,3 % a vklady stojí 87 % CDI ([Quartr release](https://web.quartr.com/m/sources/s85040634664)). Hrubý zisk se dělí 34 % úvěry, 30 % poplatky a 36 % float ([slide 20](https://web.quartr.com/m/sources/s53721092878)), takže úvěrový cyklus zasáhne jen třetinu hrubého zisku. Vysoký Selic přitom float zvedá. [Fakt / Názor]
3. **I opatrný base dává výnos.** Můj base počítá se ziskem 2027 ~4,9 mld. USD (EPS ~1,00), tedy ~15 % pod konsenzem a blízko Itaú BBA, a s P/E 12× v cíli (dnes 12,2× na můj zisk 2027). Výnos pak tvoří čistě růst zisku ~20 % ročně, bez re-ratingu. [Odhad]

**Proč je trh vedle (a kde ne):** Trh oceňuje Nu s betou k Brazílii (−17 % proti EWZ −21 % v den voleb), přestože růst je z velké části přebírání podílu od velkých bank, ne růst trhu ([Quartr call](https://web.quartr.com/m/sources/s90273386508570035709413)). Variant perception je ale **mírná, ne silná**. Normalizované ROE ~25 % (Citi) není absurdní: base vychází v 2028–29 na ROE ~24–25 %, protože se hromadí kapitál bez výplat. Edge je hlavně ve čtení delikvencí přes IEP a v tom, že cena už nese škrt odhadů. Informační výhodu nemám. Analýza pokračuje. [Názor]

## Krok 3 – byznys model

- **Jak vydělává (manažerský P&L Q3 2026):** hrubé tržby 6,26 mld. USD = úvěry 3,80 + float 1,55 + poplatky 0,91. Přímé náklady 3,66 mld. (funding 1,47, náklady na úvěr 1,79, transakce 0,15, daně z tržeb 0,25) → hrubý zisk 2,60 mld. Opex 0,85 mld. → EBT 1,74 mld., čistý zisk 1,09 mld. [Fakt, [Quartr](https://web.quartr.com/m/sources/s49694977009)]
- **Portfolio:** 41,6 mld. USD (+33 % r/r FXN): karty 27,2 mld. (65 %), nezajištěné půjčky 11,0 mld. (+39 %), zajištěné (payroll, FGTS, INSS) 3,4 mld. (+23 %). Rekordní originace nezajištěných půjček v Brazílii 22,1 mld. BRL (+28 %). Soukromé payroll půjčky zrychlují [Fakt, [Quartr release](https://web.quartr.com/m/sources/s44417884325), [call](https://web.quartr.com/m/sources/s77344505393134188253724)]
- **Geografie:** Brazílie 120 mil. klientů a vklady 38,6 mld. USD. Mexiko 16,6 mil. (+27 %, 17 % dospělých, od 3Q26 bankovní licence, pojištění vkladů 16× vyšší) a vklady 5,3 mld. Kolumbie 6,1 mil. (+62 %), úvěry +80 %, č. 1 v počtu držitelů karet, vklady 3,5 mld. za 76 % benchmarku. Segmentový zisk po zemích release neuvádí [Fakt, [Quartr release](https://web.quartr.com/m/sources/s84692159050)]
- **Reporting:** od Q4 2025 manažerský P&L (reklasifikace a daňová ekvivalence, neutrální pro zisk) vedle IFRS. Růsty uvádí FX-neutrálně, což v době slábnoucího BRL přikrášluje dojem v USD [Fakt / Názor, [Quartr](https://web.quartr.com/m/sources/s45925344772)]

**Sektorové KPI (spotřebitelská banka):**

| KPI | Q3 2026 | Trend / komentář | Zdroj |
|---|---|---|---|
| NIM / risk-adj. NIM | 22,5 % / 12,1 % (rekurentně 12,7 %; jednorázově −63 bp za pohledávky od platebních institucí v likvidaci) | RA NIM 10,8 % v Q3 25, 12,4 % v Q2 26 | [Quartr](https://web.quartr.com/m/sources/s85040634664), [slide 15](https://web.quartr.com/m/sources/s68563540508) |
| NPL 15–90 / 90+ (portfolio) | 4,9 % / 7,3 % | +0,6 pb r/r obojí | [Quartr](https://web.quartr.com/m/sources/s85040634664) |
| NPL 15–90 / 90+ (na IEP) | 8,0 % / 12,1 % | 15–90 lepší (8,2 % v Q2), 90+ horší (11,6 %) | [Quartr](https://web.quartr.com/m/sources/s44417884325) |
| Náklady na úvěr (IFRS) / portfolio, anualizované | ~16,0 % (1 668,5 mil. × 4 / 41,6 mld.) vs. ~12,9 % v Q3 25 | IFRS 9 účtuje ztráty předem: růst portfolia přidal 332 mil. a záměrné rozšíření rizika 135 mil. do opravných položek | výpočet, [Quartr](https://web.quartr.com/m/sources/s77442654670), [call](https://web.quartr.com/m/sources/s47546098355462028682805) |
| Krytí 90+ | 234 % (opravné položky 7,1 mld. USD) | stabilní | [slide 18](https://web.quartr.com/m/sources/s68951139510) |
| Kapitál | 9,9 mld. USD: požadavek 4,2, přebytek v regulovaných entitách 2,1, holding 3,6. Regulovaný kapitál ~1,5× požadavku → implikovaný CAR ~15–16 % při minimu 10,5 % | konsolidované CET1 Nu neuvádí | [slide 25](https://web.quartr.com/m/sources/s64063137101), výpočet [Odhad] |
| ROE / efficiency | 32 % / 19,3 % | ROE 29–33 % pět kvartálů, efficiency 20,3 % před rokem | [slide 32](https://web.quartr.com/m/sources/s50729500569) |
| Cena vkladů | 87 % CDI (89 % před rokem), Kolumbie 76 % | ↓ lepší | [slide 13](https://web.quartr.com/m/sources/s73898879292) |
| ARPAC / cost to serve | 17,7 USD (+21 %) / 1,1 USD (+10 %) měsíčně | kohorty po 8 letech ~30 USD | [slide 26](https://web.quartr.com/m/sources/s76474748647) |

**Moat:** [Názor]
- **Pro:** nejnižší náklady v regionu (efficiency 19 % je podle CFO konkurenceschopná globálně, [call](https://web.quartr.com/m/sources/s80275670550225753982231)), škála dat (primární účet u největšího počtu klientů v Brazílii, tedy pozitivní selekce, [call](https://web.quartr.com/m/sources/s49092653295765291724004)), levné vklady a značka.
- **Proti:** produkt (karta, nezajištěná půjčka) je komoditní a konkurence (Itaú, Inter, Mercado Pago s úvěry +62 %) tlačí na cenu. Regulace (BCB proti předlužení, kolumbijský úrokový strop) může omezit nejvýnosnější segmenty. Moat je **silný v nákladech, střední v úvěrovém underwritingu**, který zatím neprošel brazilskou recesí v dnešní velikosti.

**Produkt a recenze:** Nu vyhrálo cenu Reclame Aqui v kategorii velkých bank po deváté v řadě (12/2025) ([Nubank](https://international.nubank.com.br/company/nubank-wins-the-reclame-aqui-award-for-the-9th-consecutive-time-and-is-elected-super-champion-for-the-third-year/)). V žebříčku stížností BCB za 3Q26 má Nu Pagamentos 10,68 oprávněných stížností na milion klientů proti 57,23 u Bradesca a 43,20 u Itaú ([Mercado & Consumo](https://mercadoeconsumo.com.br/22/10/2026/servicos/conglomerado-bradesco-lidera-ranking-de-reclamacoes-do-bc-do-3o-trimestre/amp/)). Nový tier Croma pro Super Core klienty má po třech měsících blízko 1 mil. klientů a věrnostní NuCoin 6,7 mil. registrací ([Quartr](https://web.quartr.com/m/sources/s71315715920)). Na Reclame Aqui se objevují stížnosti na snížení výnosu „Caixinha Turbo“ ([Reclame Aqui](https://www.reclameaqui.com.br/nubank/reducao-drastica-no-rendimento-da-caixinha-turbo-nubank-apos-atualizacao_DbYLtcpm1tUMJZEO/)), což je jednotlivý případ, ne trend. [Fakt / Názor]

## Krok 4 – finance

**Roky (IFRS, mld. USD):**

| | 2021 | 2022 | 2023 | 2024 | 2025 | TTM 3Q26 |
|---|---|---|---|---|---|---|
| Tržby | 1,70 | 4,79 | 8,03 | 11,52 | 15,77 | 22,3 (manažerské) |
| Růst | +130 % | +182 % | +68 % | +43 % | +37 % | – |
| Čistý zisk | −0,16 | −0,36 | 1,03 | 1,97 | 2,87 | 3,92 |
| Zředěné EPS (USD) | −0,10 | −0,08 | 0,21 | 0,40 | 0,58 | ~0,80 |

[Fakt, Quartr: [2021](https://web.quartr.com/m/documents/2177775), [2022](https://web.quartr.com/m/documents/2177777), [2023](https://web.quartr.com/m/documents/2177776), [2024](https://web.quartr.com/m/documents/2177778), [2025](https://web.quartr.com/m/documents/3232655); TTM výpočet]

**Kvartály (manažerské, mil. USD):**

| | Q2 25 | Q3 25 | Q4 25 | Q1 26 | Q2 26 | Q3 26 |
|---|---|---|---|---|---|---|
| Hrubé tržby | 3 772 | 4 317 | 4 857 | 5 315 | 5 876 | 6 259 |
| NII | 2 224 | 2 477 | 2 837 | 3 251 | 3 687 | 3 872 |
| Náklady na úvěr | 1 051 | 1 036 | 1 313 | 1 794 | 1 691 | 1 789 |
| Opex | 548 | 577 | 653 | 648 | 806 | 846 |
| Čistý zisk | 637 | 783 | 895 | 871 | 1 061 | 1 092 |
| ROE | 28 % | 31 % | 33 % | 29 % | 33 % | 32 % |

[Fakt, Quartr: [tržby](https://web.quartr.com/m/sources/s53721092878), [NII a náklady na úvěr](https://web.quartr.com/m/sources/s63969770518), [opex](https://web.quartr.com/m/sources/s75759326137), [zisk a ROE](https://web.quartr.com/m/sources/s50941951325), [ROE tabulka](https://web.quartr.com/m/sources/s50729500569)]

- **Kvalita zisku:** [Fakt / Názor]
  - NII roste rychleji než náklady na úvěr (Q3: NII +56 % r/r v USD, náklady na úvěr +73 %), takže NII po rizicích roste pomaleji než NII samotné. Tohle je jádro medvědího argumentu. [výpočet]
  - IFRS 9 účtuje ztráty při originaci: rychlý růst stlačuje dnešní zisk a zisk z dnešních úvěrů přijde později. Zpomalení růstu by krátkodobě zisk zvedlo.
  - Daně: efektivní sazba je v 2026 volatilní (Q3 IFRS 19,2 %), na 2027 CFO čeká „low-to-mid 20 %“ ([call](https://web.quartr.com/m/sources/s60719956775760815323824)). To je protivítr pro růst zisku v 2027. [Odhad]
  - Jednorázové položky v Q3 ubraly ~53 mil. USD čistého zisku (pohledávky od platebních institucí v mimosoudní likvidaci, [call](https://web.quartr.com/m/sources/s60719956775760815323824)).
  - SBC: konsenzus adj. EPS 2026 je 0,93, můj IFRS odhad 0,84 USD. Rozdíl ~0,4 mld. USD ročně je hlavně SBC po dani. [Odhad]
  - FCF u banky nedává smysl. Proxy je růst vlastního kapitálu: 10,55 → 14,34 mld. USD za rok (+3,79 mld.), tedy prakticky celý zisk TTM (3,92). Žádné výplaty, nízké přecenění. [Fakt / výpočet, [slide 32](https://web.quartr.com/m/sources/s50729500569)]
- **Přechodné vs. strukturální:** přechodné jsou jednorázový zásah RA NIM v Q3, odložené výdaje (efficiency v Q4 vzroste) a kurz (Q3 průměr 5,14 BRL/USD, listopad ~5,5–5,9, takže Q4 v USD ponese translační ztrátu ~8–10 %). Strukturální jsou rostoucí náklady na riziko při záměrném rozšiřování rizika, nižší výnos float při budoucím poklesu Selic a vyšší daň 2027. [Fakt / Odhad, `research/themes.md` #em-fx, [Quartr FX](https://web.quartr.com/m/sources/s63817275662)]
- **Guidance:** efficiency FY26 19–19,5 % (z ~20 %), Nu US + Nu Global max. 100 bp dopadu na efficiency v 2026 i 2027, RA NIM v Q4 silný, Q1 sezónně vyšší cost of risk. Na 2027 žádný výhled růstu úvěrů, management ale nevidí důvod k prudkému zpomalení [Fakt, [call](https://web.quartr.com/m/sources/s91095647497616590691356), [call](https://web.quartr.com/m/sources/s77344505393134188253724), [call](https://web.quartr.com/m/sources/s74295448828022269307161)]

## Krok 5 – alokace kapitálu

- **Dividendy a buybacky:** žádné. 20-F uvádí jen zákonnou možnost zpětného odkupu, program jsem nenašel. [Fakt, [Quartr 20-F](https://web.quartr.com/m/sources/s85519098136)]
- **Kapitál k nasazení:** přebytek 2,1 mld. USD v regulovaných entitách + 3,6 mld. hotovosti na holdingu ([slide 25](https://web.quartr.com/m/sources/s64063137101)). Holdingová hotovost odpovídá ~6 % market capu. [Fakt / výpočet] Vélez mluví o „významné kapitálové optionalitě“ ([call](https://web.quartr.com/m/sources/s86138507612747137431495)). Investor Day 8. 12. má přinést dlouhodobé cíle a hnací síly tvorby hodnoty ([call](https://web.quartr.com/m/sources/s60208510716790377194916)).
- **M&A:** menšinové podíly (Tyme v Jižní Africe a na Filipínách, podíl ~18 % podle 20-F, malá investice v Indii). Plná akvizice jen s „extrémně vysokou laťkou“, preferuje organický růst ([call](https://web.quartr.com/m/sources/s66597835916398150277002), [20-F](https://web.quartr.com/m/sources/s52270512614)). Implikovaný násobek akvizic spočítat nejde, protože nejsou zveřejněné hodnoty ani tržby cílů. [Fakt]
- **Organický růst a expanze:** Nu US (licence, účet 3,5 % APY, karta 1,5 % cashback) a Nu Global (multiměnový účet na stablecoinech, 37 zemí). Investice se mají škálovat jen po ověření product-market fit a jednotkové ekonomiky ([call](https://web.quartr.com/m/sources/s74295448828022269307161)). [Fakt]
- [Názor] Hlavní otázka pro hodnotu: pokud se zisk jen hromadí jako kapitál, ROE klesá (v base k ~24–25 % v 2028). Buyback nebo dividenda z přebytku by držely ROE kolem 28–30 % a podpořily bull scénář. Velká akvizice v USA by byla negativní signál.

## Krok 6 – rozvaha

- Aktiva 74,9 mld. USD (YE25), vlastní kapitál 11,3 mld. (YE25) → 14,3 mld. (Q3 26). Vklady 41,9 mld. (YE25) → 47,5 mld. (Q3 26, +19 % FXN). Závazky vůči kartovým sítím 13,6 mld., půjčky a financování 4,4 mld. (YE25, z 1,7 mld.) [Fakt, [20-F](https://web.quartr.com/m/sources/s67357405855), [20-F](https://web.quartr.com/m/sources/s80484106309), [Quartr Q3](https://web.quartr.com/m/sources/s303136289867126839765)]
- Likvidita: hotovost 15,0 mld. a cenné papíry FVOCI 12,2 mld. (YE25). Čisté úvěry 24,7 mld. vs. dostupný funding 43,7 mld. (57 %) [Fakt, [20-F](https://web.quartr.com/m/sources/s67357405855), [slide 25](https://web.quartr.com/m/sources/s64063137101)]
- Funding je retailový (vklady v BRL/MXN/COP), holding nemá významný dluh (v podkladech jsem nenašel). Vlastní kapitál / aktiva ~15 % (YE25). Net debt / EBITDA u banky nerelevantní. [Fakt / výpočet]
- [Názor] Rozvaha je **silná a nepákovaná** proti bankám. Riziko není likvidita, ale kvalita aktiv a kurz, protože kapitál je v BRL a reportuje se v USD.

## Krok 7 – vlastnická struktura a governance

- **Kontrolující akcionář:** Vélez (přes Rua California Ltd.) drží 903,1 mil. akcií třídy B = 88,3 % třídy B a **74,4 % hlasů** při ~18,6 % ekonomického podílu. Junqueira 9,9 % hlasů. BlackRock a Baillie Gifford po ~6,9 % třídy A (13G 11/2024, resp. 4/2025). Free float ~78 % [Fakt / Odhad, [20-F](https://web.quartr.com/m/sources/s78165777277), [20-F](https://web.quartr.com/m/sources/s43206451150)]
- **Controlled company:** Nu může čerpat výjimky NYSE (většina nezávislých v radě, nezávislý výbor pro odměny) ([20-F](https://web.quartr.com/m/sources/s57900822939)). Třída B má předkupní práva při emisích. [Fakt]
- **Auditor:** KPMG Auditores Independentes od 2018, výrok k 2025 i k vnitřním kontrolám (ICFR) bez výhrad podle souhlasu k S-8 ([20-F](https://web.quartr.com/m/sources/s74360394822), [20-F](https://web.quartr.com/m/sources/s82423858648)). Změnu auditora jsem nenašel. [Fakt]
- **Management:** výměna CFO (Lago → Livingston, 13. 7. 2026; Lago zůstal jako poradce vedení a auditnímu a rizikovému výboru) a odchod CTO Erica Younga (TIKR 3. 11.) ([Yahoo/GuruFocus](https://finance.yahoo.com/markets/stocks/articles/nu-holdings-shares-down-22-150833630.html), [TIKR](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up)). Nový CFO sedí v USA, což ukazuje váhu americké expanze. [Fakt / Názor]
- **Insider trading, spřízněné strany:** transakce insiderů za 2026 nenalezeny. Spřízněné strany: dohoda o registračních právech z 2021, nic materiálního ([20-F](https://web.quartr.com/m/sources/s84188009804)). [Fakt]
- **Crowding:** HF drží ~10 % kapitalizace, NU je na VIP listu GS (47 fondů, 21× v top 10) [Fakt, log 2026-11 · GS 20. 11. (HFTM)].
- [Názor] Governance je typická pro zakladatelskou firmu: sladění zájmů přes 18,6 % podílu CEO, ale minoritní akcionáři nemají žádnou kontrolu nad kapitálovými rozhodnutími (US expanze, M&A).

## Krok 8 – rizikový profil a požadovaný výnos

**Baseline:** 10Y UST ~4,85–4,9 % (`state/prices.json`, 24.–25. 11.) plus akciová prémie ~4,5–5 % → pasivní alternativa (široký US/globální index) zhruba **9–10 % p. a.** [Odhad]

**Rizikové faktory specifické pro Nu:**
1. **Koncentrace na Brazílii a politiku (zvyšuje výrazně, +3 až +4 pb).** ~80 % klientů a vkladů je v Brazílii. Lulovo 4. období s mírnou fiskální konsolidací (GS 10. 11.), Selic 12,5–15 % (GS, SG, MS, ING), HDP 2027 0,6–1,2 % a riziko US cel na Brazílii (BCA 18. 11.). Volby ukázaly, že akcie umí ztratit 17 % za den.
2. **Nezajištěný spotřebitelský úvěr v pozdní fázi cyklu (zvyšuje, +1,5 až +2,5 pb).** Karty a nezajištěné půjčky tvoří ~92 % portfolia, NPL 90+ roste a náklady na úvěr rostou o 73 % r/r. BCB zavádí pravidla proti předlužení, Citi i Itaú BBA vidí růst úvěrů a cost of risk jako spojené nádoby. Underwriting v dnešní velikosti neprošel brazilskou recesí.
3. **Dvojí kurzové riziko (zvyšuje, +0,5 až +1 pb).** Zisk v BRL/MXN/COP, akcie v USD, Tomáš a Michal v CZK. Volatilita USD/BRL je ~25, druhá nejvyšší po BTC (log 2026-11 · SG HFW 23. 11.).
4. **Governance a alokace kapitálu (zvyšuje mírně, +0,5 až +1 pb).** Controlled company, výměna CFO a CTO v jednom roce, nejistá návratnost US expanze a otevřená možnost M&A. K tomu crowding HF (10 % kapitalizace) jako zdroj nucených prodejů.
5. **Nákladová výhoda, kapitál a likvidita (snižuje, −1,5 až −2,5 pb).** Efficiency 19 %, vklady za 87 % CDI, kapitál 9,9 mld. USD s přebytkem, LDR 57 %, žádná páka na holdingu. ROE ~30 % dává velký polštář: i bear scénář je zisková banka s ROE ~18 %, ne ztrátová firma. Výborná likvidita akcie nevyžaduje prémii za nelikviditu. Diverzifikace do Mexika a Kolumbie riziko postupně ředí.

**Závěr:** Čistá prémie vychází na +4,5 až +8 pb, tedy **požadovaný výnos 14–18 % p. a.** Dolní hranice platí, pokud Investor Day přinese věrohodné cíle a návrat kapitálu a Q4/Q1 ukážou stabilní NPL. Horní hranice platí, dokud Brazílie nemá důvěryhodný fiskální plán a BRL je kolem 5,6–6,0. Je to o něco víc než u SOFI (14–17 %), protože k úvěrovému riziku přibývá země a měna. [Názor]

**Horizont:** ~2 roky (do 11/2028). Teze se potvrdí na Investor Day (12/2026), na Q1 2027 (sezónně nejhorší úvěrový kvartál), na celoročních výsledcích 2027 (2/2028) a na tom, zda Selic začne klesat (SG od 3Q27, MS až v 2028). [Odhad]

## Krok 9 – valuace

**Peers** [Fakt, zdroje u řádků; data k různým dnům]

| Firma | Proč srovnávat | Valuace | Profitabilita / růst | Zdroj |
|---|---|---|---|---|
| **NU** | – | P/E TTM 15,3×, 10,5× 2027E · P/B 4,2×, P/TBV ~4,5× (25. 11.) | ROE 32 %, zisk +31 % r/r FXN, kniha +36 % r/r | výpočet, [StockAnalysis](https://stockanalysis.com/stocks/nu/) |
| Itaú Unibanco | největší brazilská banka, hlavní incumbent | P/E 9,2×, P/B 1,9×, dividendový výnos ~8 % (panel bez data) | ROE 23,6 %, NPL 90+ 2,0 %, úvěry +10 % r/r (3Q26) | [Investidor10](https://investidor10.com.br/noticias/itau-itub4-supera-r-12-bi-em-lucro-no-3t26-veja-os-destaques-do-balanco-123668/) |
| Inter & Co (INTR) | brazilská digitální banka | P/E TTM 5,2×, fwd 4,6× (20. 11. při 3,60 USD) | ROE 15,8 %, efficiency 41,9 % (3Q26) | [StockAnalysis](https://stockanalysis.com/stocks/intr/), `companies/INTR/dossier.md` |
| MercadoLibre (Mercado Pago) | přímý konkurent v kartách a úvěrech | P/E TTM 42×, P/B 9,8× (5. 11.) | úvěry 17,9 mld. USD (+62 %), NIMAL 20,1 %, NPL 15–90 7,0 % | [sec-api](https://sec-api.io/insights/mercadolibre-meli-q3-2026-earnings-sec-filing-analysis-17-9bn-credit-book-up-62-as-operating-margin-falls-to-6-3) |
| StoneCo | brazilský fintech (platby, úvěry) | fwd P/E ~5,2× před volbami, po propadu blíž ~3× (26. 10.) | – | [TIKR](https://www.tikr.com/blog/stoneco-sinks-29-inter-co-down-36-pagseguro-down-25-on-lulas-unexpected-election-win) |
| PagSeguro | brazilský fintech | nenalezeno | – | – |
| SoFi | US digitální banka (Tomášova pozice) | fwd P/E 18,1×, P/TBV 1,91× (17. 11.) | ROTCE 9,9 % | `companies/SOFI/deep-dive-v1.md` |

Čtení [Názor]: Proti Itaú má Nu ~2,2× vyšší P/B při o ~8 pb vyšším ROE a ~3–4× rychlejším růstu knihy. V excess-return logice je to konzistentní, pokud Nu udrží ROE nad ~25 % ještě několik let. Proti INTR a StoneCo je Nu drahý, ale ty mají ROE 15 % a méně. MELI je jediný regionální fintech oceňovaný výš, protože trh ho bere jako e-commerce platformu. Na P/E 2027 (10,5×) je Nu levnější než SOFI při 3× vyšší ziskovosti.

**Reverse excess-return model (residual income)** [Odhad, Python]
- Předpoklady: kniha 14,34 mld. USD, ROE lineárně z 30 % na ROE_T během 10 let, růst knihy z 25 % na 5 %, terminální růst 5 %.
- Dnešní cena implikuje trvalé ROE_T **20,8 % při ke (náklady vlastního kapitálu) 12 %, 24,0 % při 13 %, 27,4 % při 14 %, 31,1 % při 15 %**. Když kniha zpomalí rychleji (18 % → 5 %), při ke 13 % je potřeba ROE_T 28,4 %.
- Ilustrace: ROE trvale 30 % a ke 14 % dává hodnotu 13,68 USD. Pád ROE na 22 % (úroveň Itaú) dává 9,55 USD.
- **Trh tedy počítá s ROE kolem 24–27 %**, což je pod dnešními 32 %, ale nad Itaú. Nejde o krizové ocenění, jde o ocenění „zestárnutí“.

**Reverse DCF na EPS** (bez dividend, EPS 2026E IFRS 0,84 USD) [Odhad, Python]
- Při ke 14 % a exit P/E 12× v 2031 potřebuje cena EPS 2031 ~1,98 USD, tedy **CAGR 18,7 %**. Při exit P/E 10× je potřeba 23,2 %, při 14× 15,1 %.
- Konsenzus (EPS 2027 1,18, 2028 1,51) implikuje ~27 % ročně do 2028. Trh tedy počítá zhruba s polovinou až dvěma třetinami konsenzuálního tempa.

**Tři scénáře** (cíl k 11/2028 = forward P/E × čistý zisk 2029E / 4,91 mld. akcií, ředění ~0,5 % ročně; zisk 2026E 4,07 mld. USD) [Odhad, Python]

| Scénář | P | Zisk 2027 / 28 / 29 (mld. USD) | CAGR 26–29 | P/E | EPS 2029 | Cíl | Výnos (2 r. / p. a.) | ROE 2028, P/B v cíli | Klíčový předpoklad |
|---|---|---|---|---|---|---|---|---|---|
| Bear | 25 % | 3,8 / 4,1 / 4,6 | 4 % | 8,5× | 0,94 | **7,96 USD** | −36 % / −20 % | 19 %, 1,7× | Brazilská recese a předlužení: náklady na riziko dál rostou rychleji než úvěry, růst portfolia pod 15 %, BCB omezí karty, USD/BRL ~6,0+, daň ~24 %, ocenění jako Itaú |
| Base | 50 % | 4,9 / 5,9 / 7,0 | 20 % | 12× | 1,42 | **17,10 USD** | +38 % / +18 % | 25 %, 3,2× | Zisk ~15–20 % pod konsenzem (blízko Itaú BBA), NPL 90+ kolem 7–7,5 %, Mexiko roste, BRL ~5,5, bez buybacku, násobek beze změny |
| Bull | 25 % | 5,4 / 6,9 / 8,6 | 28 % | 15× | 1,75 | **26,26 USD** | +112 % / +46 % | 28 %, 4,7× | Měkké přistání, Selic klesá od 2H27, BRL k 5,25 (GS/SG/MS), Investor Day s cíli a návratem kapitálu, Mexiko a Kolumbie ziskové, zisk blízko konsenzu (EPS 2028 ~1,41 vs. 1,51) |

- **Vážená cílová cena 17,10 USD → +38,4 % za 2 roky, ~17,6 % p. a.**
- **Požadovaný výnos 14–18 % p. a. → vážený výnos je v horní části pásma, ale pod hranicí Buy** (+50 % za 1–3 roky by vyžadovalo cenu ~11,40 USD).
- Citlivost na pravděpodobnosti: 30/50/20 → 16,19 USD (14,4 % p. a.), 20/50/30 → 18,02 USD (20,7 % p. a.), 35/45/20 → 15,73 USD (12,8 % p. a.).
- Cena, při které vážený výnos vychází 14 / 16 / 18 % p. a.: 13,16 / 12,71 / 12,28 USD.
- Citlivost na BRL (~80 % zisku z Brazílie): BRL −10 % proti USD ≈ −8 % zisku v USD, base cíl ~15,7 USD. BRL +5 % ≈ +4 %, base ~17,8 USD. [Odhad]
- Rozptyl scénářů je široký (−36 % až +112 %). Transakční srovnání pro celou firmu neexistuje.

## Krok 9b – co píšou analytici

**Přímé zmínky (nejnovější nahoře):**

| Datum | Instituce | Rating / cíl | Co říká |
|---|---|---|---|
| 20. 11. 2026 | GS (HFTM) | – | NU na VIP listu nejoblíbenějších HF longů (47 fondů, 21× v top 10), HF drží 10 % kapitalizace, YTD −29 % (log 2026-11 · GS 20. 11.) |
| 20. 11. 2026 | konsenzus | Buy, 23 analytiků (14 SB / 5 B / 3 H / 1 S), průměr 17,63 USD | rozpětí 12–23 USD ([StockAnalysis](https://stockanalysis.com/stocks/nu/forecast/)). V polovině října 22 analytiků, průměr 18,77 USD ([Investing](https://uk.investing.com/equities/nu-holdings-consensus-estimates)) → průměrný cíl ⬇️ |
| 3. 11. 2026 | konsenzus (TIKR) | průměr 18,80 USD | P/TBV 4,6× vs. 3letý průměr 8,3×, odchází CTO ([TIKR](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up)) |
| 29. 10. 2026 | Itaú BBA | Hold (od 16. 9.), cíl 18 → **15** USD ⬇️ (konec 2027) | Růst portfolia 2027 zpomalí z 37 na 26 %, Mexiko zatím výpadek nevyrovná. Zisk o 19 % pod konsenzem 2027 a 22 % pod 2028. 13,5× 2027 podle nich riziko nekompenzuje ([Seu Dinheiro](https://www.seudinheiro.com/2026/empresas/e-agora-nubank-itau-bba-corta-preco-alvo-e-alerta-o-pior-ainda-pode-estar-por-vir-miql/)) |
| 26. 10. 2026 | Monness Crespi | 🆕 Buy, 20 USD | dlouhodobý růst neobank a BNPL ([Stocktwits](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy)) |
| 20. 10. 2026 | UBS | Buy, 18,20 → **20,50** USD ⬆️ | – (dossier, [StockAlarm](https://pro.stockalarm.io/quote/NU/analysts)) |
| 1. 10. 2026 | GS (Labarta) | Hold, 23 USD | kombinace Hold a cíle 23 USD je neobvyklá, možná chyba ve zdroji ([StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 28. 9. 2026 | Needham | Buy, 19 USD | potvrzeno ([StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 16. 9. 2026 | Itaú BBA | Buy → **Hold** ⬇️, 20 → 18 USD | výhled Brazílie (dossier, [StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 25. 8. 2026 | Wolfe | Buy, 18 → **17** USD ⬇️ | – ([StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 17. 8. 2026 | MS (Kuri) | Buy, 21 USD | – ([StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 14. 8. 2026 | Susquehanna | Hold, 13 → **16** USD ⬆️ | – ([StockAnalysis](https://stockanalysis.com/stocks/nu/ratings/)) |
| 15. 6. 2026 | Citi | Buy → **Neutral** ⬇️, 18 → 13 USD | 14,4× P/E 2027, zisk 2026/27 −9 % / −15 % na 3,7 / 4,4 mld. USD, dlouhodobé ROE 30 → 25 %, kreditní karty a půjčky „podřízené“ payroll půjčkám ([NeoFeed](https://neofeed.com.br/negocios/apos-bofa-citi-rebaixa-nubank-por-risco-na-carteira-de-credito/en/)) |
| 2. 6. 2026 | BofA (Pierry) | Neutral → **Underperform** ⬇️, 16 → 10 USD | férový násobek 13× forward (z 18×) ([Nasdaq/Fool](https://www.nasdaq.com/articles/it-too-soon-call-bottom-nu-holdings-stock)). StockAnalysis 14. 8. potvrzuje Sell 10 USD, ale konsenzus 20. 11. má minimum 12 USD → **rozpor ve zdrojích** |

V broker reportech v research logu (GS, MS, SG, JPM, BCA, ING, UBP, Gavekal) se NU jménem objevuje jen v GS HFTM 20. 11. Jinak jde jen o témata. [Fakt]

**Témata #latam / #em-fx / #fintech:**
- **Brazílie – akcie:** GS snížil na MW (13. 11., HDP 2027 0,6 %, Selic 12,5 % konec 2027, IBOV EPS 2027 jen +1 %) a zvedl Mexiko na OW. EM banky drží OW. MS LatAm snížil Brazílii na UW (16. 11.). Alpine (19. 11.) naopak dává Brazílii nejvyšší 10letý očekávaný výnos akcií (10,3 %) (log 2026-11 · GS 13. 11., MS 15. 11., Alpine 19. 11.).
- **Selic:** GS 12,5 %, SG 12,75 % (snižování od 3Q27), MS 13,75 % po celý 2027 (11,75 % v 2028). ING uvádí, že trh nacenil růst na 15 % (log 2026-11 · GS 13. 11., SG 20. 11., MS 20. a 23. 11., ING 12. 11.).
- **BRL:** shoda na USD/BRL 5,25 koncem 2027 (GS, SG, MS), ING nejbýčejší 5,00. Krátkodobě MS varuje před 6,00 bez fiskálního plánu a GS (20. 11.) označil BRL za nejslabší EM měnu od 4. 11. (~−7,5 %) s odtoky z fondů. BCA (11. 11.) otevřela long BRL proti CHF (log 2026-11 · GS 13. a 20. 11., MS 9. a 20. 11., BCA 11. 11.).
- **Politika:** GS (10. 11.) čeká v Lulově 4. období jen mírnou fiskální konsolidaci. BCA (18. 11.) varuje před možnými US cly na Brazílii (log 2026-11 · GS 10. 11., BCA 18. 11.).
- **EM financials / fintech:** Gavekal L. Gave (6. 11.) má EM financials mezi favority při slabším USD. GS HFTM (20. 11.): HF v Q3 nejvíc navýšily Financials (+254 bp) (log 2026-11 · Gavekal 6. 11., GS 20. 11.).

**Konsenzus vs. rozpory:** Sell-side je k Nu pozitivní (19 z 23 Buy), ale průměrný cíl klesá (18,8 → 17,6 USD za měsíc) a skeptici mají konkrétní čísla. Itaú BBA a Citi se shodují na tom, že růst a cost of risk jsou spojené nádoby a že konsenzus zisku je příliš vysoko. Můj base je blízko jejich odhadů, takže tenhle argument v ceně vidím, ne proti tezi. Hlavní rozpor makro domů je Selic (12,5 % GS vs. 13,75 % MS vs. tržních 15 %). Pro Nu je to dvousečné: vysoký Selic drží výnos z floatu (36 % hrubého zisku), ale tlačí na schopnost domácností splácet. Shoda na BRL 5,25 koncem 2027 (z dnešních ~5,6–5,9) by znamenala +6–10 % translační vítr pro zisk v USD, což podporuje base a bull. Rozpor GS (Brazílie MW, Mexiko OW, EM banky OW) přesně odpovídá tezi: Brazílie je riziko, Mexiko druhý motor. [Názor]

**Z grafů:** GS HFTM (20. 11.): relativní propad VIP koše za 6 měsíců (−14 pb) je mezi extrémy XII/2008 a V/2022 a oba přišly blízko dna trhu. NU je člen koše, takže jde o kontrariánský signál, ale zároveň o riziko dalšího odbourávání crowdingu (log 2026-11 · GS 20. 11.). SG HFW (23. 11.): 30denní volatilita USD/BRL ~25 je druhá nejvyšší po BTC (log 2026-11 · SG 23. 11.).

## Krok 10 – base rate check

- **Brazilské banky v recesi 2015–2016 (Dilma):** velké soukromé banky (Itaú, Bradesco) prošly hlubokou recesí se zvýšeným cost of risk, ROE kleslo jen o několik bodů a ocenění se po 1–2 letech vrátilo. Úspěšnost „přežít cyklus bez ztráty franšízy“ byla u bank s nízkými náklady vysoká. [Názor, události obecně známé, bez ověřených čísel v tomto běhu]
- **Nu sám v 2022:** po IPO (12/2021) akcie v cyklu zvyšování Selic spadla hluboko pod emisní cenu a během dalších let se vrátila vysoko nad ni. Tehdy ale Nu byl ztrátový (zisk 2022 −0,36 mld. USD) a dnes vydělává ~4 mld. ročně. [Fakt: zisk [Quartr](https://web.quartr.com/m/documents/2177777); zbytek Názor]
- **Spotřebitelští věřitelé s rychlým růstem nezajištěných úvěrů do zpomalení:** typicky přišel nejdřív škrt odhadů a de-rating, teprve pak kapitulace ziskovosti (Upstart 2022 a 11/2026 podle `companies/SOFI/deep-dive-v1.md`). Rozdíl: Nu je financovaný vklady, ne prodejem úvěrů. [Názor]
- **Brazilské fintechy po volbách 2026:** INTR spadl na ~5× zisku, StoneCo na ~3× forward. Trh umí brazilské tituly držet na extrémně nízkých násobcích dlouho, takže bear s P/E 8,5× není okrajový. [Fakt / Názor, [TIKR](https://www.tikr.com/blog/stoneco-sinks-29-inter-co-down-36-pagseguro-down-25-on-lulas-unexpected-election-win)]
- **Závěr:** Base rate pro „nízkonákladová banka projde brazilskou recesí se ziskem“ je vysoký. Base rate pro „rychle rostoucí nezajištěný věřitel se vyhne škrtu odhadů“ je nízký. Proto bear 25 % a bull jen 25 %. [Názor]

## Krok 11 – rizika (podle závažnosti) a nejsilnější protiargument

1. **Brazilský úvěrový cyklus:** rekordní originace nezajištěných půjček (září nejsilnější měsíc v historii) těsně před zpomalením ekonomiky a s rostoucí zadlužeností domácností. Q1 2027 je sezónně nejhorší kvartál. [Fakt / Názor]
2. **Makro a politika Brazílie:** fiskál, Selic, BRL a možná US cla. Q4 ponese translační ztrátu ze slabšího BRL. [Fakt / Odhad]
3. **Regulace:** BCB opatření proti předlužení (management tvrdí, že s nimi je v souladu), případné stropy na úroky kreditních karet, kolumbijský úrokový strop. [Fakt, [call](https://web.quartr.com/m/sources/s86552330140042228240853)]
4. **Alokace kapitálu a US expanze:** hromadění kapitálu bez výplat ředí ROE. Nu US může spotřebovat víc než slíbených 100 bp efficiency, nebo může přijít drahá akvizice. [Názor]
5. **Konkurence:** Mercado Pago (úvěry +62 %), Itaú a soukromé payroll půjčky bank. Citi upozorňuje, že nezajištěné expozice jsou fakticky podřízené payroll půjčkám. [Fakt]
6. **Crowding a sentiment:** HF drží 10 % kapitalizace. Případné odbourávání VIP košů znamená prodeje bez ohledu na fundament. [Fakt]
7. **Management:** nový CFO a odchod CTO v jednom roce, kontrola zakladatele. [Fakt]

**Nejsilnější protiargument:** Růst Nu je z velké části úvěrová páka na nejzadluženější brazilské domácnosti v nejvyšších sazbách za desetiletí. Náklady na úvěr rostou o 73 % proti 33% růstu portfolia a IFRS 9 to zatím maskuje růstem (zisk z nových úvěrů přichází před ztrátami ze starších vintage). Až růst zpomalí na ~25 % (Itaú BBA), zisk se přiblíží Citi (4,4 mld. USD v 2027) a trh Nu přecení na brazilskou banku: ~2× knihy při ROE ~22 %, tedy ~9–10 USD (můj model při ROE 22 % dává 9,55 USD). Pokles NPL 15–90 na IEP může být jen efekt jmenovatele při rychlém růstu IEP. [Názor]

## Krok 12 – conviction a velikost pozice

- **Conviction: střední.** Edge je interpretační (čtení NPL přes IEP, nákladová výhoda, cena už nese škrt odhadů), rozptyl scénářů je široký (−36 % až +112 %) a klíčová data přijdou během 3–5 měsíců (Investor Day, Q4, Q1). [Názor]
- **Tomáš (koncentrované portfolio):** rámcová velikost **4–6 %**. Současná váha **5,7 %** (`tools/portfolio.py`, 25. 11.), tedy **v rámci, na horní hraně**. Pozor na korelaci: fintech blok (SOFI 13,8 % + NU 5,7 % + INTR 0,4 %) tvoří 20 % portfolia a NU s INTR jsou společně sázka na Brazílii a BRL. Bear scénář při současné váze ubere ~2,1 pb z celého portfolia. → **Držet, nepřikupovat při 12,36 USD.** Přikoupit (k ~6 %) má smysl pod ~11,4 USD, nebo po potvrzení na Investor Day a ve Q4, a to jen pokud se mezitím sníží SOFI (viz `companies/SOFI/deep-dive-v1.md`). Pozice je v zisku +8,9 %. [Fakt / Názor]
- **Michal (konzervativní, 63 % ETF):** rámcová velikost **2–3 %**. Současná váha **3,6 %**, tedy **mírně převážená**. Bear ubere ~1,3 pb z portfolia. → Nepřikupovat. Při růstu k base cíli (~17 USD) stáhnout na ~2,5 %. Prodávat teď u 52W minima nedává smysl, pozice je v zisku +10,4 %. [Fakt / Názor]
- Nejsem finanční poradce. Tohle je podklad pro Tomášovo rozhodnutí, ne pokyn.

## Krok 13 – katalyzátory a monitoring

| Datum | Událost | Potvrdí | Vyvrátí |
|---|---|---|---|
| 8. 12. 2026 | [Investor Day](https://web.quartr.com/m/events/744463) (první v historii) | dlouhodobý cíl ROE ≥ 28 %, rámec návratu kapitálu (buyback nebo dividenda z ~5,7 mld. přebytku a holdingové hotovosti), číselné cíle pro Mexiko | jen vize bez čísel, velké US ambice s vysokými ztrátami, signál M&A |
| prosinec 2026 – 1Q27 | COPOM (přesné datum nenalezeno), rozpočet 2027 a jmenování ministra financí, BCB pravidla proti předlužení | fiskální plán, BRL zpět pod ~5,5, Selic bez dalšího růstu | Selic nahoru k 15 %, USD/BRL nad 6,0, stropy na úroky karet |
| 24. 2. 2027 | [Výsledky Q4 2026](https://web.quartr.com/m/events/800028) | efficiency FY26 19–19,5 %, NPL 15–90 na IEP ≤ 8,0 %, NPL 90+ ≤ 7,5 %, růst portfolia ≥ 25 % FXN, RA NIM ≥ 12 % | NPL 90+ > 8 %, RA NIM rekurentně < 11 %, škrt tempa úvěrů pod 20 % |
| ~5/2027 | Q1 2027 (sezónně nejvyšší cost of risk) | ROE ≥ 27 % i v Q1, NPL 15–90 v pásmu loňska | ROE < 26 %, skok NPL 15–90 nad 5,3 % portfolia |
| 2027 | Mexiko (payroll účty, zákon o digitální ekonomice), Kolumbie (úrokový strop), Nu US | Mexiko viditelně ziskové, vklady rostou za nižší cenu, uvolnění stropu v Kolumbii | US dopad na efficiency nad 100 bp |
| 2H27 | Selic a BRL | začátek snižování Selic (SG od 3Q27), USD/BRL k 5,25 | Selic 13,75 % po celý rok (MS) a slabý BRL |

**Co by signál zvrátilo:** 🟢 / přikoupit: Investor Day s cílem ROE ≥ 28 % a návratem kapitálu plus Q4 s NPL 15–90 na IEP ≤ 8,0 % a NPL 90+ ≤ 7,5 % při růstu ≥ 25 %. Pak posunu pravděpodobnosti na 20/50/30 a vážený výnos vyjde ~21 % p. a. Druhá cesta je cena pod ~11,4 USD při nezměněných fundamentech. 🔴: NPL 90+ > 8 % nebo NPL 15–90 > 5,3 %, rekurentní RA NIM < 11 %, ROE < 26 % ve dvou kvartálech, regulační strop na úroky karet, USD/BRL dlouhodobě nad 6,2, velká akvizice. Definitivně by tezi rozbilo, kdyby náklady na úvěr dál rostly víc než dvojnásobným tempem proti portfoliu i po zpomalení růstu. [Názor]

**KPI pro Tracker:** NPL 15–90 a 90+ (na portfolio i na IEP) · náklady na úvěr vs. růst portfolia · RA NIM (vykázaný a rekurentní) · ROE · efficiency ratio · cena vkladů (% CDI) · kapitál a přebytek · klienti a aktivita po zemích · ARPAC · USD/BRL · Selic.

## Krok 14 – zdroje

- **Quartr – firma a eventy:** [Nu (11343)](https://web.quartr.com/m/companies/11343) · [Q3 2026 event + summary](https://web.quartr.com/m/events/695612) · [Investor Day 8. 12.](https://web.quartr.com/m/events/744463) · [Q4 2026 (24. 2. 2027)](https://web.quartr.com/m/events/800028)
- **Quartr – dokumenty:** [Earnings release Q3 2026](https://web.quartr.com/m/documents/3696872) · [Slidy Q3 2026](https://web.quartr.com/m/documents/4257984) · [Transcript Q3 2026](https://web.quartr.com/m/documents/4595512) · [20-F 2025](https://web.quartr.com/m/documents/3232655) · release [Q2 26](https://web.quartr.com/m/documents/3689651), [Q1 26](https://web.quartr.com/m/documents/3331488), [Q4 25](https://web.quartr.com/m/documents/2927750) · roční data [2021](https://web.quartr.com/m/documents/2177775), [2022](https://web.quartr.com/m/documents/2177777), [2023](https://web.quartr.com/m/documents/2177776), [2024](https://web.quartr.com/m/documents/2177778)
- **Quartr – klíčové pasáže:** [metriky Q3](https://web.quartr.com/m/sources/s85040634664) · [manažerský P&L](https://web.quartr.com/m/sources/s49694977009) · [IFRS P&L](https://web.quartr.com/m/sources/s77442654670) · [NPL na IEP](https://web.quartr.com/m/sources/s44417884325) · [NPL graf](https://web.quartr.com/m/sources/s71296141615) · [bridge opravných položek](https://web.quartr.com/m/sources/s53479729571) · [krytí](https://web.quartr.com/m/sources/s68951139510) · [kapitál](https://web.quartr.com/m/sources/s64063137101) · [vlastní kapitál a ROE](https://web.quartr.com/m/sources/s50729500569) · [vklady](https://web.quartr.com/m/sources/s73898879292) · [ARPAC](https://web.quartr.com/m/sources/s76474748647) · call: [opravné položky](https://web.quartr.com/m/sources/s47546098355462028682805), [jednorázovky a daň](https://web.quartr.com/m/sources/s60719956775760815323824), [RA NIM a Q1](https://web.quartr.com/m/sources/s91095647497616590691356), [růst úvěrů a payroll](https://web.quartr.com/m/sources/s77344505393134188253724), [M&A](https://web.quartr.com/m/sources/s66597835916398150277002), [kapitálová optionalita](https://web.quartr.com/m/sources/s86138507612747137431495), [Mexiko](https://web.quartr.com/m/sources/s55845031399732943749951), [Kolumbie](https://web.quartr.com/m/sources/s68401852961779112280434), [BCB opatření](https://web.quartr.com/m/sources/s86552330140042228240853), [US a Global 100 bp](https://web.quartr.com/m/sources/s74295448828022269307161) · 20-F: [vlastníci](https://web.quartr.com/m/sources/s78165777277), [poznámky k vlastníkům](https://web.quartr.com/m/sources/s43206451150), [controlled company](https://web.quartr.com/m/sources/s57900822939), [rozvaha](https://web.quartr.com/m/sources/s67357405855), [vlastní kapitál](https://web.quartr.com/m/sources/s80484106309), [auditor](https://web.quartr.com/m/sources/s74360394822)
- **Research log a repo:** log 2026-11 · GS 10., 13. a 20. 11. (EM Kickstart, HFTM, FX), MS 9., 15., 20. a 23. 11., SG 16., 20. a 23. 11., ING 12. 11., BCA 11. a 18. 11., Gavekal 6. 11., Alpine 19. 11. · `research/themes.md` (#latam, #usd/#em-fx, #fintech) · `research/house-views.md` (Brazílie, Selic, USD/BRL) · `companies/NU/dossier.md` · `companies/INTR/dossier.md` · `companies/SOFI/deep-dive-v1.md` · `tools/portfolio.py` (25. 11.)
- **Sell-side přes web:** [Seu Dinheiro – Itaú BBA 29. 10.](https://www.seudinheiro.com/2026/empresas/e-agora-nubank-itau-bba-corta-preco-alvo-e-alerta-o-pior-ainda-pode-estar-por-vir-miql/) · [NeoFeed – Citi a BofA 15. 6.](https://neofeed.com.br/negocios/apos-bofa-citi-rebaixa-nubank-por-risco-na-carteira-de-credito/en/) · [Brasil247 – Citi](https://www.brasil247.com/brazilstockguide/?p=5241) · [Nasdaq/Fool – BofA, Susquehanna 3. 6.](https://www.nasdaq.com/articles/it-too-soon-call-bottom-nu-holdings-stock) · [Stocktwits – Monness 26. 10.](https://stocktwits.com/news-articles/markets/equity/nu-stock-worst-day-on-record-in-brazil-market-rout-with-buy-rating/cZU34E4RByy) · [StockAnalysis – ratingy](https://stockanalysis.com/stocks/nu/ratings/) · [StockAlarm](https://pro.stockalarm.io/quote/NU/analysts)
- **Ceny a konsenzus:** [StockAnalysis](https://stockanalysis.com/stocks/nu/) · [StockAnalysis forecast](https://stockanalysis.com/stocks/nu/forecast/) · [StockAnalysis historie](https://stockanalysis.com/stocks/nu/history/) · [WallStreetZen – EPS 2027/28](https://www.wallstreetzen.com/stocks/us/nyse/nu/stock-forecast) · [Investing – konsenzus](https://uk.investing.com/equities/nu-holdings-consensus-estimates) · [TIKR 3. 11.](https://www.tikr.com/pt/blog/nu-holdings-just-dropped-14-in-a-month-is-it-time-to-sell-or-load-up) · close 25. 11. Yahoo (ze zadání a `state/prices.json`)
- **Peers:** [Investidor10 – Itaú 3Q26](https://investidor10.com.br/noticias/itau-itub4-supera-r-12-bi-em-lucro-no-3t26-veja-os-destaques-do-balanco-123668/) · [StockAnalysis – INTR](https://stockanalysis.com/stocks/intr/) · [sec-api – MELI 3Q26](https://sec-api.io/insights/mercadolibre-meli-q3-2026-earnings-sec-filing-analysis-17-9bn-credit-book-up-62-as-operating-margin-falls-to-6-3) · [TIKR – volby 26. 10.](https://www.tikr.com/blog/stoneco-sinks-29-inter-co-down-36-pagseguro-down-25-on-lulas-unexpected-election-win)
- **Management a produkt:** [Yahoo/GuruFocus – CFO](https://finance.yahoo.com/markets/stocks/articles/nu-holdings-shares-down-22-150833630.html) · [Business Wire – CFO](https://www.businesswire.com/news/home/20260601015786/en/Nubank-Appoints-Rob-Livingston-as-Chief-Financial-Officer) · [Nubank – Reclame Aqui](https://international.nubank.com.br/company/nubank-wins-the-reclame-aqui-award-for-the-9th-consecutive-time-and-is-elected-super-champion-for-the-third-year/) · [Mercado & Consumo – žebříček BCB 3Q26](https://mercadoeconsumo.com.br/22/10/2026/servicos/conglomerado-bradesco-lidera-ranking-de-reclamacoes-do-bc-do-3o-trimestre/amp/) · [Reclame Aqui – stížnost](https://www.reclameaqui.com.br/nubank/reducao-drastica-no-rendimento-da-caixinha-turbo-nubank-apos-atualizacao_DbYLtcpm1tUMJZEO/)
- **Výpočty:** `companies/NU/valuation-v1.py` (snapshot, RSI, reverse excess-return, reverse DCF, scénáře, citlivosti) · váhy `tools/portfolio.py`
- **Nedostupné v tomto běhu:** stránky StockAnalysis pro ITUB a MELI (oprávnění nepotvrzeno), Benzinga a Chartmill (chyba webu). Konsenzus EPS 2027/28 je jen z WallStreetZen bez data. PagSeguro bez dat. Close 24. 11. nedohledán (dopočten z +4,2 %).

## Krok 15 – uložení

- `companies/NU/deep-dive-v1.md` (tento soubor), `companies/NU/valuation-v1.py`
- Dossier aktualizován (signál, teze, KPI, scénáře, katalyzátory, odkaz na v1), `universe.yaml`: `last_deep_dive: 2026-11-26`
- NU odebrán z `deep_dive_queue` (state.json), Claude Doc „Deep dive: Nu Holdings (NU) – 26. 11. 2026“ vytvořen.

[Analýza uložena: companies/NU/deep-dive-v1.md]
