# Rozvrh naplánovaných úloh

Časy jsou Europe/Prague. Úlohy běží v cloudu jako naplánované úlohy v Claude. Každý
běh si stáhne toto repo, provede úlohu a změny pushne zpět.

| Úloha | Kdy | Co dělá | Výstup pro Tomáše |
|---|---|---|---|
| Portfolio – denní běh | každý den 6:17 | `tasks/research-inbox.md` → `tasks/portfolio-tracker.md` | alert jen při události, jinak nic |
| Portfolio – Market Brief | pondělí 7:13 | `tasks/market-brief.md` | dokument „Market Brief – datum“ |
| Portfolio – týdenní souhrn | pondělí 7:47 | `tasks/portfolio-weekly.md` | dokument „Portfolio – týdenní souhrn – datum“ |

Změna rozvrhu: napiš v chatu třeba „přesuň brief na pátek 17:00“ (viz `tasks/on-demand.md`).

## Text promptů (pro případ ručního obnovení)

**Denní běh:**
> Připoj GitHub repo newtwotv-dev/portfolio-research s přístupem push (add_repo) a naklonuj ho do /home/claude/portfolio-research. Přečti CLAUDE.md a proveď v tomto pořadí tasks/research-inbox.md a tasks/portfolio-tracker.md. Dodrž začátek a konec běhu z CLAUDE.md (synchronizace watchlistu, commit a push). Výstupy česky.

**Market Brief:**
> Připoj GitHub repo newtwotv-dev/portfolio-research s přístupem push (add_repo) a naklonuj ho do /home/claude/portfolio-research. Přečti CLAUDE.md a proveď tasks/market-brief.md (pokud dnes neběžel Research Inbox, spusť nejdřív tasks/research-inbox.md). Výstup vytvoř jako Claude Doc a ulož do briefs/market/. Nakonec commit a push. Česky.

**Týdenní souhrn:**
> Připoj GitHub repo newtwotv-dev/portfolio-research s přístupem push (add_repo) a naklonuj ho do /home/claude/portfolio-research. Přečti CLAUDE.md a proveď tasks/portfolio-weekly.md. Výstup vytvoř jako Claude Doc a ulož do briefs/portfolio/. Nakonec commit a push. Česky.
