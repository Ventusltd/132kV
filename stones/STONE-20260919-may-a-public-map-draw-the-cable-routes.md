# STONE: may a public map draw the 132 kV underground cable routes? No. Here is what may be done instead.

19 September 2026. The licence was obtained and read in full, and each finding below was checked by three
independent verifiers who were told to try to refute it. This is a record of what was found, not legal advice.

## The question

UK Power Networks publishes a dataset, "UK Power Networks Licence Area 132kV Underground Cables"
(2,437 records, last modified 2026-03-31), under the "UK Power Networks Shared Data Licence - Connections".
May an independent free public map draw it, or a public repository hold it or anything made from it?

## The answer: no

1. **The licence is not an open licence.** It is an Energy Networks Association shared data licence. It grants a
   non-exclusive, non-transferable, revocable right to access, view and store the data for the purposes stated in a
   data request form filled in on the portal. Initial term three months; copies are deleted on expiry. (Clauses 2.1, 13.1.2.)
2. **No redistribution, in whole or in part,** and no making the data available to third parties. A public map and
   a public repository are both that. (Clause 3.1.6; also 3.1.3, 3.1.5, 3.1.8.) There is no clause that allows
   reuse in return for attribution.
3. **No derived data.** On a reasonable reading that covers simplified lines, lengths or counts per area computed
   from the geometry, and capacity estimates computed from it. (Clause 3.1.4. The licence does not define
   "derived data", so this reading is an inference, and the cautious one.)
4. **No use for machine learning or artificial intelligence purposes.** The geometry must not be given to any
   model, local or hosted. (Clause 3.1.7.)
5. **Why.** The operator's own data triage treats cable pinch points and customer terminations as a security and
   commercial risk, to be shared with trusted parties for connections work. The geometry sits behind a login;
   anonymous requests are refused.
6. **Nobody else publishes it openly either.** No other distribution network operator in Great Britain was found
   publishing 132 kV underground routes under an open licence.

## What MAY be done, and is

- **Catalogue facts may be published**: that the dataset exists, its record count, its modified date, its licence
  name. The operator serves these to anonymous callers, and the regulator's data best practice guidance says the
  metadata of shared data should normally be open. That is exactly what this repository records, daily, and no more.
- **Link out.** Anyone who needs the routes for a connection asks the operator, on the operator's terms.
- **Draw the openly licensed datasets.** 132 kV overhead lines, poles and towers, and 132 kV circuit operational
  data (amps and MW) are CC BY 4.0. Attribution, in the operator's required form:
  `UK Power Networks, <dataset name>, <dataset URL>, <date of last update>`.
- **Use public notices of new routes** (planning, streetworks, consents), each with its own source and terms.

## Rules for this repository and for any engine that reads it

1. Never download, store, draw, simplify, aggregate or feed to a model the geometry of any dataset under a shared
   data licence. The watcher reads the catalogue only, and that is by design, not by accident.
2. Every dataset used carries its licence name beside it. No licence name, no use.
3. CC BY data is drawn only with the attribution line above, filled in.
4. A rising record count is the signal. It says cable went in. It does not say where, and we do not say where.

Licence file read: "UK Power Networks Shared Data Licence - 05.12.25 - Connections" (Energy Networks Association
template, September 2025), linked from the dataset's page on https://ukpowernetworks.opendatasoft.com.
This project is independent and is not affiliated with or endorsed by any network operator.
