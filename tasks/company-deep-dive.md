# Úloha: Analýza firmy (Onboarding a Deep dive)

Dvě úrovně:
- **Onboarding**: rychlé založení dossieru u nové firmy (watchlist, nová pozice). Cca 20 %
  práce deep dive.
- **Deep dive**: plná analýza podle 15krokového frameworku níže. Spouští se z fronty
  (`state.json → deep_dive_queue`), na povel („analyzuj X“, „deep dive X“) nebo když
  Tomáš pošle odkaz, screenshot či popis firmy.

Framework převzatý od kamaráda a upravený pro tohle repo. **Sekvence kroků je fixní.**
Metriky, násobky, peers a požadovaný výnos uvnitř každého kroku odvozuj vždy znovu
z konkrétního byznysu, nikdy z předem daných čísel nebo kategorií.

Každé tvrzení ve financích a valuaci označ **[Fakt]**, **[Odhad]** nebo **[Názor]**.
**Buy** = očekávaný výnos +50 % až +100 % a víc v horizontu 1–3 let.

Zdroje dat v tomto pořadí: Quartr (dokumenty, transcripty, finance), research log
v repu (broker pohledy), web (ceny, tržní data, recenze, zprávy).

---

## Onboarding (rychlý dossier)

1. Zkopíruj `templates/dossier.md` do `companies/<TICKER>/dossier.md`.
2. Vyplň:
   - **Pozice** z `portfolio.yaml` (všechny účty, oba vlastníci),
   - **Snapshot** (krok 0 níže, s tím, co jde rychle dohledat),
   - **Byznys v kostce** (3–5 vět),
   - **KPI ke sledování**: 4–6 metrik specifických pro sektor (viz krok 3),
   - **Katalyzátory**: nejbližší události z Quartr `list_events` nebo z webu,
   - **Broker views**: zmínky z `research/log/` a ze `state.json → pending_mentions`,
   - **Investiční teze**: nech prázdné místo „Tomášova teze (doplnit)“ a pod ním
     navrhni pracovní variantu označenou [Názor].
3. Signál nastav 🟡 Sledovat, dokud není hotový deep dive.
4. Doplň `quartr_id` do `universe.yaml` (přes `search_companies`), pokud chybí.
5. Firmu přidej do `deep_dive_queue`.

---

## Deep dive (15 kroků)

Výstup: `companies/<TICKER>/deep-dive-vN.md` (N = další číslo verze) + Claude Doc
s názvem `Deep dive: <Název> (<TICKER>) – <D. M. YYYY>`. Poté aktualizuj dossier: tezi,
KPI, scénáře, katalyzátory, signál a odkaz na verzi.

Při aktualizaci existující analýzy začni rozdílem oproti předchozí verzi: co se změnilo
a proč.

### Krok 0 – snapshot firmy
Tabulka: sektor a subsektor, země HQ, listingy, ticker, market cap, EV, cena akcie, 52W
low–high, % free float, % insider ownership, gross / EBIT / FCF / net margin, total revenues,
net debt / EBITDA, CEO, odkaz na investor relations, analytický konsenzus, denní likvidita
a její kategorizace (podprůměrná / průměrná / nadprůměrná vzhledem k velikosti firmy), RSI 14.

### Krok 1 – zdroj a kontext idey
Jednou větou: odkud idea přišla a kdy (u stávajících pozic z `portfolio.yaml` nebo
z dossieru). Proč je dnes cena tam, kde je. Jak vypadá trh firmy dnes a stručný výhled
na další roky.

### Krok 2 – teze v jedné větě (variant perception)
Co si myslí trh, co si myslíš ty a proč je trh podle tebe vedle. Jádro celé analýzy.
**Bez variant perception analýza nepokračuje.** Pokud ji nenajdeš, napiš to otevřeně
a analýzu ukonči krokem 11 (rizika) a krokem 13 (monitoring).

### Krok 3 – byznys model
Komplexně: co firma dělá, jak vydělává peníze, kde je moat nebo jeho absence. Jak reportuje
a jaké má segmenty. Metriky zvol podle sektoru: u banky NIM a CET1, u SaaS NRR a CAC
payback, u výrobní firmy replacement cost kapacity a utilizaci, u biotechu cash runway
a pipeline s pravděpodobnostmi, u obrany backlog a book-to-bill. Přidej produkt a recenze
(zákazníci, uživatelé, odborný tisk).

### Krok 4 – finance
Historický vývoj tržeb, marží a cash flow. Kvalita zisku, jednorázové položky, konverze
na FCF. Poslední výsledky: co bylo přechodné a co strukturální. Data z Quartr `get_financials`
a z posledních reportů.

### Krok 5 – alokace kapitálu
Jak firma nakládá s cash flow: M&A, capex, dividendy, buybacky. U akvizic spočítej
implikovaný násobek s synergiemi i bez nich.

### Krok 6 – rozvaha
Zadlužení, splatnosti, likvidita, kdo drží dluh a za jakých podmínek. Net debt / EBITDA.

### Krok 7 – vlastnická struktura a governance
Free float, kontrolující akcionář, transakce se spřízněnými stranami, změny auditora,
insider trading. **Povinný krok u každé firmy.**

### Krok 8 – rizikový profil a požadovaný výnos
Nahrazuje pevné tiery. Postupuj jako analytik při odvozování diskontní sazby:
1. **Baseline**: výnos pasivní alternativy na daném horizontu (relevantní index nebo
   bezriziková sazba plus riziková prémie trhu).
2. Identifikuj **3–5 konkrétních rizikových faktorů této firmy**, ne obecné kategorie.
   Například úroveň páky, volatilita cash flow v cyklu, trvanlivost moatu, kvalita
   managementu a track record alokace kapitálu, likvidita akcie a free float, složitost
   struktury, koncentrace na jeden trh nebo zákazníka.
3. U každého faktoru napiš, zda požadovanou prémii nad baseline zvyšuje, nebo snižuje,
   a proč.
4. Z toho odvoď implikovaný požadovaný výnos jako **rozmezí**, ne jedno číslo. Zdůvodni ho
   textem, ne tabulkou.
5. Horizont analýzy odvoď z toho, kdy by se teze měla podle katalyzátorů potvrdit,
   ne z fixní délky.

### Krok 9 – valuace
Trading multiples proti peers, DCF nebo reverse DCF, transakční srovnání, pokud existuje
M&A. V reverse DCF ukaž, jaký růst a jakou marži musí trh věřit, aby ospravedlnil
dnešní cenu. **Tři scénáře** (bear, base, bull) s pravděpodobnostmi a cílovou cenou.
Pravděpodobnostně vážený výnos porovnej s požadovaným výnosem z kroku 8. Výpočty
(DCF, vážený výnos) dělej v Pythonu, ne z hlavy.

### Krok 10 – base rate check
Existují historické precedenty podobné situace u srovnatelných firem? Jaká byla jejich
úspěšnost?

### Krok 11 – rizika a nejsilnější protiargument
Rizika seřaď podle závažnosti. Na konci napiš nejsilnější argument proti tezi.

### Krok 12 – conviction a velikost pozice
Míra přesvědčení (nízká / střední / vysoká) podle šíře rozptylu scénářů z kroku 9 a síly
edge z kroku 2. Z toho rámcová velikost pozice v % portfolia, ne částka. Porovnej se
**současnou** váhou z `tools/portfolio.py` a napiš, jestli je pozice pod-, nebo
převážená. U pozic v bratrově portfoliu zvlášť.

### Krok 13 – katalyzátory a monitoring
Co sledovat, kdy přijdou další data a co by tezi potvrdilo nebo vyvrátilo. **Tohle se
přenáší do dossieru** jako KPI a katalyzátory, podle kterých pak běží denní Tracker.

### Krok 14 – zdroje
Seznam všech použitých zdrojů s odkazy (Quartr, broker reporty s datem, web).

### Krok 15 – uložení
- `companies/<TICKER>/deep-dive-vN.md` (v1, v2, v3 při dalších aktualizacích).
- Aktualizovaný dossier (teze, scénáře, signál, KPI, katalyzátory, odkaz na verzi).
- Claude Doc pro Tomáše.
- Odeber firmu z `deep_dive_queue` a zapiš `last_deep_dive` do `universe.yaml`.
- Na konci oznam: `[Analýza uložena: companies/<TICKER>/deep-dive-vN.md]`.
