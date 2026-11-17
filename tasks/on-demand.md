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
| „co říkají banky o <téma>“ | Hledej v `research/log/`, `house-views.md`, `themes.md` → shrnutí v chatu se zdroji. |
| „týdenní souhrn“ | `tasks/portfolio-weekly.md`. |
| „přeplánuj brief na pátek“, „chci denní brief“, „vypni alerty“ | Najdi naplánovanou úlohu (`list_triggers`) a uprav ji (`update_trigger`). Aktualizuj `config/schedule.md`. |
| „signály“, „co bych měl řešit“ | Přehled všech signálů z dossierů seřazený podle naléhavosti (⚡, 🔴, 🟡, 🟢). |

Odpovědi na krátké povely piš přímo do chatu. Dokument vytvářej jen u briefu, souhrnu,
deep dive, nebo když o něj Tomáš požádá.
