# Úloha: Portfolio Tracker (denní)

**Cíl:** Zjistit, co se od posledního běhu stalo u firem v `universe.yaml` (tier A a B),
aktualizovat jejich dossiery a **jen když se stalo něco podstatného**, poslat Tomášovi alert.

Předpoklad: dnešní Research Inbox už proběhl (`state.json → research_inbox.last_run` je dnes).
Pokud ne, spusť nejdřív `tasks/research-inbox.md`.

## 1. Onboarding nových firem

Firmy s tierem A nebo B, které nemají `companies/<TICKER>/dossier.md`: proveď onboarding
podle sekce „Onboarding“ v `tasks/company-deep-dive.md`. Pořadí podle
`state.json → onboarding_queue`, max. 6 firem za běh. Hotové z fronty odeber, zbytek
nech na další běh a zapiš do `state.json → onboarding_queue`.

## 2. Sběr novinek (okno: od `portfolio_tracker.last_run`)

Pro každou firmu tieru A (tier B jen v pondělí):

**Quartr** (pokud `quartr_id` není null):
- `list_events` → nové a nadcházející události (earnings, CMD, AGM). Nadcházející zapiš
  do `state/calendar.md`.
- `list_documents` → nové dokumenty od posledního běhu (výsledky, prezentace, 10-Q/10-K,
  6-K, tiskové zprávy).
- Pokud proběhly výsledky nebo earnings call: nejdřív `get_event_summary` /
  `get_document_summary`, a pokud jde o tier A, přečti i transcript (`read_transcript`).
  Zaměř se na guidance, KPI z dossieru, komentáře k poptávce, marže, alokaci kapitálu
  a otázky analytiků, na které management uhýbal.

**Research log:** nové záznamy v `research/log/` zmiňující firmu (už zapsané v dossieru
Inboxem) a `state.json → pending_mentions`.

**Web** (jen cíleně, ne plošně):
- firmy s `source: manual` (SMSH, TNEK): oznámení na burze a zprávy,
- biotech (IOVA, AQST, GUTS): FDA rozhodnutí, data z klinických studií, financování,
- firmy s výraznou zmínkou v reportech nebo s blížící se událostí,
- jedno hledání „big movers“ pro akcie z portfolia, aby se zachytily pohyby nad 8 %.

**Makro kontext:** podívej se do `research/themes.md` na témata z pole `themes` dané firmy
a nové poznámky stručně promítni do dossieru, když mění pohled na firmu.

## 3. Aktualizuj dossiery

Pro každou firmu s novinkou:
- uprav příslušné sekce (Poslední výsledky, Guidance, KPI, Katalyzátory, Rizika),
- přidej řádek do „Deníku změn“ (datum, co se změnilo, zdroj),
- přehodnoť **Signál** podle pravidel v `CLAUDE.md`. Změnu signálu zapiš do jeho historie.

Firmám bez novinek nic nepřepisuj.

## 3b. Zařazení na aktualizaci deep dive

Firma s hotovým deep dive (`last_deep_dive` v `universe.yaml`) jde do `state.json → refresh_queue`,
když nastane aspoň jedno:
- zveřejnila výsledky nebo změnila guidance,
- nastal některý bod z „Potvrdí“ nebo „Vyvrátí“ v dossieru,
- signál se změnil na 🔴 nebo ⚡ z jiného důvodu, než byl v posledním deep dive,
- cena se od data posledního deep dive pohnula o 25 % a víc.

Záznam: `{"ticker", "reason", "trigger_date", "since": "deep-dive-vN"}`. Plánované spouštěče
(např. výsledky v kalendáři) zapiš s `trigger_date` v budoucnu, aktivují se až po něm.
V alertu nebo týdenním souhrnu uveď „zařazeno na aktualizaci deep dive“.

## 4. Alert, jen když je důvod

Vytvoř alert (Claude Doc + `briefs/alerts/YYYY-MM-DD.md`, šablona `templates/alert.md`),
pokud nastala aspoň jedna z těchto věcí:
- firma z portfolia zveřejnila výsledky nebo změnila guidance,
- změna signálu na 🔴 nebo ⚡,
- pohyb ceny o 8 % a víc za den nebo 15 % a víc od posledního týdenního souhrnu,
- M&A, emise akcií nebo dluhu, změna CEO/CFO, výrazný insider nákup nebo prodej,
- regulatorní nebo klinická událost (FDA, výsledky studie, zakázka nebo kontrakt, který
  hýbe tezí),
- významná změna broker doporučení nebo cílové ceny u držené firmy.

Jinak žádný dokument nevytvářej. Novinky půjdou do týdenního souhrnu.

## 5. Stav

- `portfolio_tracker.last_run` = teď.
- `state/calendar.md`: smaž proběhlé události starší než 7 dní.
- Pokud jsi kvůli „big movers“ dohledával ceny, ulož je do `state/prices.json`
  (aktualizuj jen ty, které máš, a v klíči `as_of` uveď datum).

## 5b. Fronta deep dive

Pokud v tomto běhu nevznikl alert a zbývá kapacita, udělej **jeden** deep dive. Přednost má
aktivní položka z `state.json → refresh_queue` (trigger_date ≤ dnes, aktualizace vN+1 podle sekce
„Aktualizace“ v `tasks/company-deep-dive.md`), jinak první položka z
`state.json → deep_dive_queue` podle `tasks/company-deep-dive.md`
a vytvoř k němu Claude Doc. Frontu řaď podle váhy v portfoliu (výstup
`tools/portfolio.py`). Nové firmy z watchlistu se řadí podle váhy stejně jako ostatní (nedržené na konec).
