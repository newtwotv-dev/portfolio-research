# Povely z chatu

Tomáš může kdykoliv napsat povel v chatu nad tímto repem (nová session v Claude Code
s repem `portfolio-research`, nebo pokračování v kterémkoliv naplánovaném běhu).
Rozpoznávej i volné formulace. Vždy dodrž začátek a konec běhu z `CLAUDE.md`
(stáhni repo, nakonec commit a push).

| Povel (příklady) | Co udělat |
|---|---|
| „pošli mi brief“, „co se děje na trzích“, „brief za poslední 3 dny“ | `tasks/market-brief.md` s požadovaným obdobím (výchozí: od posledního briefu). Pokud Inbox dnes neběžel, spusť ho nejdřív. |
| „co je nového u Micronu“, „update SOFI“ | Tracker jen pro danou firmu (`tasks/portfolio-tracker.md`, kroky 2–3) a krátká odpověď v chatu. Claude Doc jen když o něj požádá. |
| „analyzuj X“, „deep dive X“, odkaz nebo screenshot firmy | `tasks/company-deep-dive.md` (plná analýza). |
| „přidej X na watchlist“ | Přidej do `universe.yaml` (tier B) a proveď onboarding. Zeptej se, jestli ji má přidat i na Quartr watchlist, a teprve po souhlasu zavolej `add_to_watchlist`. |
| „odeber X“ | `status: archived` v `universe.yaml`, dossier do `_archive/`. Quartr watchlist jen se souhlasem. |
| „koupil jsem 10 SOFI za 15 na T212“, „prodal jsem…“ | Uprav `config/portfolio.yaml` (množství a vážená průměrná cena). Nová firma → universe + onboarding. Potvrď změnu jedním řádkem. |
| nový výpis od brokera (PDF, screenshot) | Porovnej s `portfolio.yaml`, ukaž rozdíly a po potvrzení přepiš. Osobní údaje z výpisu (rodné číslo, ID zákazníka) **nikdy** neukládej. |
| „stav portfolia“, „kolik mám“ | Aktualizuj ceny → `tools/portfolio.py` → odpověď v chatu (tabulka a 3 věty komentáře). |
| „co říkají banky o <téma>“, „co píšou analytici o ropě / Fedu / AI / firmě X“ | Viz sekce **Dotaz na téma** níže. |
| „týdenní souhrn“ | `tasks/portfolio-weekly.md`. |
| „přeplánuj brief na pátek“, „chci denní brief“, „vypni alerty“ | Najdi naplánovanou úlohu (`list_triggers`) a uprav ji (`update_trigger`). Aktualizuj `config/schedule.md`. |
| „signály“, „co bych měl řešit“ | Přehled všech signálů z dossierů seřazený podle naléhavosti (⚡, 🔴, 🟡, 🟢). |

Odpovědi na krátké povely piš přímo do chatu. Dokument vytvářej jen u briefu, souhrnu,
deep dive, nebo když o něj Tomáš požádá.


## Dotaz na téma (co píšou analytici)

Tomáš se může kdykoliv zeptat na téma, region, aktivum nebo firmu (pokyn 20. 11. 2026).
1. Najdi všechno relevantní: štítek v `research/themes.md` (všechny datované odrážky),
   řádky v `research/house-views.md` (tabulky i log změn) a `grep -n -i` přes všechny
   `research/log/*.md` (štítek, klíčová slova, tickery, synonyma). U firmy i její dossier.
2. Odpověď v chatu (dokument jen na požádání nebo když je to dlouhé):
   - **Shrnutí v 2–3 větách:** kam se banky kloní a jak se to vyvíjí v čase.
   - **Kdo co říká:** tabulka Instituce | Pohled / outlook (čísla, cíle) | Datum, nejnovější nahoře.
   - **Rozpory** jmenovitě (kdo proti komu a proč).
   - **Vysvětlení** jednoduchými slovy, co to znamená a proč na tom záleží (mechanismus).
   - **Dopad na portfolio:** které pozice se tématu týkají a jakým směrem [Názor].
   - **Zdroje** ve tvaru „log 2026-11 · GS 13. 11.“; z grafů jen, co je v řádcích „Z grafů“.
3. Pokud jsou data stará (poslední zmínka > 14 dní), řekni to a nabídni kontrolu novějších zdrojů.
