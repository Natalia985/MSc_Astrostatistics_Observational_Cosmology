# Instructor Guide

## Hands-on course design

Separate homework notebooks are intentionally removed.

Six weekly lab notebooks are marked **Graded Lab**. Their **Extended Analysis** sections are the homework equivalents.

### Graded weeks

- L02 → Graded Lab 1
- L05 → Graded Lab 2
- L06 → Graded Lab 3
- L07 → Graded Lab 4
- L09 → Graded Lab 5
- L11 → Graded Lab 6

## Suggested 4-hour lab pacing

- 0:00–0:20 — scientific question + five-line statement
- 0:20–1:20 — guided implementation
- 1:20–1:30 — break
- 1:30–2:30 — independent analysis
- 2:30–2:40 — break
- 2:40–3:25 — diagnostic / failure test
- 3:25–3:50 — checkpoint
- 3:50–4:00 — explain Extended Analysis on graded weeks

## Instructor preparation before semester

1. Download Pantheon+ high-level table and covariance.
2. Verify `scripts/fetch_sdss_rm.py` works, or cache the public VizieR tables.
3. Select three SDSS-RM objects for L07: easy/intermediate/difficult.
4. Prepare a machine-readable Appendix-B table from arXiv:2608.23579 with provenance notes.
5. Build the real SDSS parent pool for L09 and commit the exact query in `scripts/sdss_parent_pool_query.sql`.
6. Choose and document the DESI BAO product used in L11.
7. Add local deadlines and Faculty academic-integrity rules.

## Data-integrity rule

Do not fabricate missing measurements to make an assignment easier.

If a public source cannot supply a needed variable, redesign the task or state the limitation.

## Grading efficiency

Use the same six-part rubric for all graded labs.

The scientific conclusion and diagnostic/failure sections should carry enough weight that code-only submissions cannot earn high marks.
