# Úloha: Research Inbox

**Cíl:** Zpracovat nové reporty v Gmailu jednou a uložit z nich strukturované extrakty,
ze kterých čtou všechny ostatní úlohy. Tomášovi nic neposílá.

## 1. Najdi nové maily

- Okno: od `state.json → research_inbox.last_processed_at` do teď. Při prvním běhu
  (hodnota je `null`) vezmi posledních 14 dní.
- Gmail dotaz: `after:YYYY/MM/DD -in:sent` (datum o den dřív než `last_processed_at`,
  kvůli překryvu). Stránkuj, dokud nejsou všechny výsledky.
- Přeskoč vlákna, jejichž id je v `state.json → research_inbox.processed_thread_ids`.

## 2. Roztřiď

Pro každý mail urči původního autora. U FW mailů od `martinec@jtfg.com` je v těle řádek
`From:`. Pak mail zařaď podle `config/sources.yaml`:

| Kategorie | Co s tím |
|---|---|
| high / medium priorita | plný extrakt (krok 3) |
| company_alerts (Simply Wall St) | extrakt jen pro firmy z `universe.yaml`, ostatní zahoď |
| newsletters_low | extrakt jen když zmiňují firmu z `universe.yaml` nebo silné makro téma, jinak jen řádek v logu |
| ignore (webcasty, registrace) | jen řádek v logu („Ostatní“) |

**Limit na běh:** plný extrakt nejvýš u 20 reportů. Přednost má vysoká priorita, zmínka
firmy z portfolia a outlooky. Zbytek zapiš jako „Nezpracováno – jen titulek“ a nech
vlákno mimo `processed_thread_ids`, aby ho další běh dokončil.

## 3. Přečti obsah

1. `get_thread` a přečti text mailu. U krátkých notes (Gavekal Daily, Albert Edwards
   apod.) často stačí tělo mailu.
2. Pokud je obsah v PDF příloze: `download_gmail_attachment` → ulož do `/tmp/reports/`
   (mimo repo) → `pdftotext -layout`.
3. U dlouhých PDF (víc než 15 stran) čti:
   - titulní stranu, executive summary a key takeaways (obvykle strany 1–4),
   - tabulky doporučení a alokací,
   - všechny pasáže, kde se vyskytuje ticker nebo název firmy z `universe.yaml`
     (`grep -n -i` přes text).
4. PDF ani jejich text **necommituj** do repa.

## 4. Zapiš extrakt

Do `research/log/YYYY-MM.md` (měsíc podle data reportu, soubor vytvoř, pokud neexistuje)
přidej záznam podle `templates/research-entry.md`. Nejnovější záznamy jdou nahoru pod
nadpis dne.

Pravidla extraktu:
- Parafrázuj vlastními slovy, žádné dlouhé citace.
- **Hlavní teze** max. 3 odrážky, **klíčová čísla** jen ta, která jsou v reportu.
- **Změny doporučení** uváděj vždy explicitně (z čeho na co), i u alokací regionů a sektorů.
- **Relevance pro portfolio:** přímá (firma zmíněná jménem), nepřímá (sektor nebo téma
  z pole `themes` v `universe.yaml`), nebo žádná.
- Štítky témat používej konzistentně se seznamem v `research/themes.md`. Nové téma přidej
  i tam.

## 5. Aktualizuj souhrnné soubory

**`research/house-views.md`:**
- U každé změny doporučení nebo výrazného pohledu (region, sektor, aktivum, firma)
  aktualizuj řádek v tabulce aktuálních pohledů (Téma | Instituce | Pohled | Od | Zdroj).
- Změnu zapiš i do sekce „Log změn“ (datum, instituce, z → na, odkaz na záznam v logu).

**`research/themes.md`:**
- K tématům, kterých se nové reporty týkají, přidej datovanou odrážku: co je nového
  a kdo to říká.
- Když se téma objeví ve 3 a víc reportech za týden, označ ho 🔥 (žhavé téma týdne).

**Zmínky firem:** pokud report zmiňuje firmu z `universe.yaml`, přidej do jejího dossieru
(sekce „Broker views a zmínky“) jeden řádek: datum, instituce, co říká, odkaz na záznam v logu.
Pokud dossier ještě neexistuje, zapiš zmínku do `state.json → pending_mentions` a Tracker
ji použije při onboardingu.

## 6. Stav

- `research_inbox.last_processed_at` = čas nejnovějšího zpracovaného mailu.
- Přidej id zpracovaných vláken do `processed_thread_ids` a smaž z tohoto seznamu id starší
  než 21 dní (podle data).
- `research_inbox.last_run` = teď a `research_inbox.last_run_stats` = počty
  (plné extrakty / jen titulek / zahozené).
