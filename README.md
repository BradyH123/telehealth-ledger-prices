# Telehealth Ledger published telehealth prices

Dated checks of the prices US telehealth programs publish on their own pages. This folder is a snapshot saved on 2026-11-12 from the data files listed at https://telehealthledger.com/press (https://telehealthledger.com/data/prices.csv, /data/price-changes.csv, /data/disclosure-census.csv). The live files are updated as prices are re-checked; use this snapshot when you need a fixed, citable copy.

## Files
| File | What | Rows |
|---|---|---|
| `data/prices.csv` | One row per published program price: provider, treatment, price and its basis, commitment, whether medication is included, the date checked (`verifiedAt`) and the page it was read from (`sourceUrl`) | 130 rows, 31 providers, checked 2026-10-25 to 2026-11-11 |
| `data/price-changes.csv` | Dated log of recorded changes, 2026-08-22 to 2026-11-11 | 180 entries: 73 are a provider's price re-verified at a new value; the rest are this site's own corrections, relabels or pulls |
| `data/disclosure-census.csv` | How many tracked providers publish each fact (a price, a continuing monthly price, and so on), with scope and date | 4 rows |
| `datapackage.json` | Frictionless Data Package descriptor with file hashes and column types (types inferred from the files) | |

Treatments in `prices.csv` on 2026-11-12: Compounded tirzepatide injection (34), Compounded semaglutide injection (31), Compounded NAD+ injection (14), Compounded oral semaglutide (10), Compounded Sermorelin injection (9), Compounded NAD+ nasal spray (5), Compounded glutathione injection (4), Compounded oral tirzepatide (4), Compounded oral Sermorelin (4), Wegovy injection (4), Zepbound injection (4), Compounded oral NAD+ (3), Ozempic injection (3), Mounjaro injection (1).

## What a row is, and is not
- A row is a dated reading of a page the provider publishes. It is not a quote, and a price may have changed since `verifiedAt`.
- Coverage is the providers listed on Telehealth Ledger, not a census of the market. Some providers show no price before a questionnaire, and some pages cannot be read.
- Compounded drugs are not FDA-approved. Nothing here is medical advice or a health claim.
- Column definitions and how prices are normalised: https://telehealthledger.com/methodology . Corrections: https://telehealthledger.com/corrections .

## Check the published figures yourself
`examples/reproduce_headline_figures.py` (Python standard library only) recomputes, from `data/prices.csv` alone, the figures published on https://telehealthledger.com/press for this snapshot: for example, 16 providers with a calendar-month continuing price for compounded semaglutide, from $99 to $299 a month, median $164. If your numbers differ from a published figure, that is a correction we want: https://telehealthledger.com/corrections .

## Who publishes this and how it is funded
Telehealth Ledger is edited by Brady Hanlon. The site earns a commission from most of the providers it lists when a reader signs up through its visit link. The data files carry no tracked links; `sourceUrl` is the provider's own page.

## Licence and credit
CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Credit: Telehealth Ledger, telehealthledger.com. How you link is up to you.

Suggested citation: Telehealth Ledger. (2026). Telehealth Ledger published telehealth prices (snapshot 2026-11-12) [Data set]. https://telehealthledger.com/press
