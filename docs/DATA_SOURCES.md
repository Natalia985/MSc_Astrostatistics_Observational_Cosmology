# Real Data Sources

## Pantheon+ / SH0ES

Public repository:

https://github.com/PantheonPlusSH0ES/DataRelease

High-level course files are in:

`Pantheon+_Data/4_DISTANCES_AND_COVAR/`

including:

- `Pantheon+SH0ES.dat`
- `Pantheon+SH0ES_STAT+SYS.cov`

Store local copies under `data/raw/pantheon_plus/`. `data/raw/` is ignored by Git.

## SDSS Reverberation Mapping

VizieR catalogue:

`J/ApJ/851/21`

Important tables:

- `table1`: 222-object quasar sample information
- `table2`: 152,258 continuum/emission-line light-curve measurements

Students start from the published light-curve products, not raw spectra.

## Central SN Ia–QSO paper

https://arxiv.org/abs/2608.23579

The paper combines calibrated Type Ia SNe with SDSS DR14 quasars and reports a 255-object photometric AGN golden sample in Appendix B.

The course treats the sample as a **statistical-selection case study**, not as established physical AGN standardisation.

## SDSS parent pool for Lab 09

The instructor must provide either:

- a reproducible SDSS query and its real-data output; or
- an instructor-prepared CSV generated from that exact query.

The query must be committed to `scripts/`.

Do not create synthetic replacements for missing SDSS measurements.

## DESI BAO

DESI public documentation:

https://data.desi.lbl.gov/doc/

DR2 cosmology products:

https://data.desi.lbl.gov/doc/papers/dr2/

Convenient public teaching packaging:

https://github.com/CobayaSampler/bao_data

The course uses published BAO summary/cosmology products, not unreleased spectra.

## Real-data rule

Bootstrap, jackknife, permutation and posterior-predictive calculations are allowed statistical operations on real observations. They must not be described as additional observed objects.
