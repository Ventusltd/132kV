# 132kV
132kV Grid Connections Public Data

## Why

More people should be able to connect to the grid. The first thing anyone needs to know is where
capacity is, and where it is about to appear. At 132 kV that is public knowledge, scattered across
open data portals, planning records and streetworks notices. This repository gathers what is
public, says where each fact came from, and does the arithmetic in the open.

## What one circuit is worth

    power (MVA) = 1.732 x voltage (kV) x current (A) / 1000          1.732 is the square root of 3

| current in each phase | at 132 kV |
|---|---|
| 1000 A | 228.6 MVA |
| 1200 A | 274.4 MVA |
| 1312 A | 300.0 MVA |

A single circuit of large 132 kV cable is worth roughly a quarter of a gigawatt. The full table for
11 kV to 400 kV is `data/capacity.tsv`, made by `tools/capacity.py` and checked on every push. It
turns a current into a power. It is NOT a cable rating: what a buried cable carries continuously
depends on its size, how it is laid, how its screens are bonded, and the soil, and is a calculation
to IEC 60287 for the real route.

## What is watched

Once a day `tools/watch_catalogue.py` runs on GitHub's own machine and asks a network operator's
public open data catalogue which datasets mention 132 kV.

- **[NOW.md](NOW.md)** every such dataset, its record count, when it last changed, and its licence.
- **data/ledger.tsv** append only: one row each time a dataset's record count or date changes.

**Why a record count matters.** The 132 kV underground cable dataset has one record per mapped cable
section. When that number rises, cable has gone in the ground, and capacity has come with it. The
ledger is the dated record of that, kept from the day this was switched on.

## What this repository will not hold

- **No copied records from datasets that are not openly licensed.** Some datasets here are CC BY 4.0;
  the cable route datasets are under the operator's own shared data licence. For every dataset only
  the catalogue's own facts are kept: that it exists, how many records, when it changed. Follow the
  link and accept the operator's terms to see the data itself.
- No maker's tender reply, no guaranteed particulars supplied in confidence, no prices, no
  trademarks, nobody's proprietary data, no personal data.
- No figure without a public source or an open derivation. Anything else is left out or marked CANDIDATE.

## The licence question, answered

May a public map draw the 132 kV underground cable routes? **No.** The licence was read in full; see
[stones/STONE-20260919-may-a-public-map-draw-the-cable-routes.md](stones/STONE-20260919-may-a-public-map-draw-the-cable-routes.md)
for what it forbids, what may be done instead, and the attribution line for the datasets that are open.

## What it costs to run

Nothing that has to be paid for: a few seconds a day on a free runner, no key, no assistant. It
commits only when something changed.

## Next

1. Public planning and streetworks notices of new 132 kV routes, each with its source and date.
2. From the openly licensed 132 kV circuit flow data: how loaded each circuit is, with attribution.
3. Other network operators' public portals, the same way.
4. The cable section and an IEC 60287 rating for each route, drawn by the GlobalGrid2050 engine.

Source of the catalogue facts: UK Power Networks Open Data Portal, https://ukpowernetworks.opendatasoft.com.
This project is independent and is not affiliated with or endorsed by any network operator.
Provided as is, without warranty of any kind; a chart, not a design.

## Licence

The code is under the MIT licence (see LICENSE). The ledgers and tables this repository itself produces are under CC BY 4.0: use them, and say where they came from. Data belonging to others keeps its own licence, named beside it.
