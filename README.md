# MSc Astrostatistics for Observational Cosmology

## Real survey data, AGN variability, Bayesian inference and multi-probe cosmology

**Duration:** 11 weeks  
**Weekly contact:** 3 h lecture + 4 h hands-on  
**Total contact:** 77 h  
**Scientific-data rule:** assessed analyses use **real observational data**.

> **How do real astronomical measurements become constraints on the Universe?**

\[
\text{observations}
\rightarrow
\text{measurement uncertainty}
\rightarrow
\text{statistical model}
\rightarrow
\text{distance/time scale}
\rightarrow
p(\theta_{\rm cosmo}\mid D).
\]

## Hands-on design

There are **11 weekly lab notebooks**. Six are **graded labs** and replace separate homework assignments.

- Every week: in-class checkpoint, contributing to the 20% practical grade.
- Six weeks: the same notebook contains an **Extended Analysis** section completed after class and submitted for 5%.
- Students therefore maintain one notebook per week, not a lab plus a separate homework.

### Assessment

| Component | Weight |
|---|---:|
| Weekly lab checkpoints | 20% |
| Six graded lab extensions | 30% |
| Final real-data project | 40% |
| Oral scientific defence | 10% |

## Real data

- Pantheon+ / SH0ES
- SDSS Reverberation Mapping light-curve products
- Real SDSS AGN/quasar data used to study the statistical-selection framework of arXiv:2608.23579
- DESI BAO public cosmology products

See `docs/DATA_SOURCES.md`.

## Weekly learning structure

Each week has three linked components:

1. **Lecture** — cosmology-focused theory and derivation in `lectures/`.
2. **Learning Notebook** — selected material from the [2025 Astrostatistics Summer School](https://github.com/lionandjelka/2025_summer_school).
3. **Hands-on Lab** — real observational data in `labs/`.

See [`docs/LECTURES_AND_CRETE.md`](docs/LECTURES_AND_CRETE.md) for the exact week-by-week map.

### Example

**Week 3**

- Lecture: `lectures/W03_OPTIMIZATION_LIKELIHOOD_AND_MLE.ipynb`
- Learning notebooks:
  - [Crete Optimization](https://github.com/lionandjelka/2025_summer_school/blob/main/03_Optimization/Optimization.ipynb)
  - [Crete MLE](https://github.com/lionandjelka/2025_summer_school/blob/main/04_MLE/MLE.ipynb)
- Lab: `labs/L03_COSMOLOGICAL_LIKELIHOOD.ipynb`

The Crete notebooks teach the **general statistical method**; the course lab applies it to **real cosmological observations**.


## Weekly labs

| Week | Lab | Status |
|---:|---|---|
| 1 | Data anatomy: Pantheon+ and SDSS-RM | Formative |
| 2 | Real Hubble diagram: residuals, bootstrap and tests | **Graded Lab 1** |
| 3 | Build a cosmological likelihood | Formative |
| 4 | Bayesian Hubble diagram | Formative |
| 5 | MCMC, covariance and nuisance parameters | **Graded Lab 2** |
| 6 | Robustness to real sample definition | **Graded Lab 3** |
| 7 | Measure a real SDSS-RM reverberation lag | **Graded Lab 4** |
| 8 | Critical reconstruction of the SN Ia–QSO paper | Formative |
| 9 | Multivariate SDSS AGN selection | **Graded Lab 5** |
| 10 | Gaussian-process cosmological reconstruction | Formative |
| 11 | Real multi-probe cosmology | **Graded Lab 6** |

## Student workflow

For every lab:

1. Read the scientific question.
2. Complete the five-line statistical statement before coding.
3. Audit the real data.
4. Complete the required analysis.
5. Run the diagnostic/failure test.
6. Write the scientific conclusion.
7. On graded weeks, finish the **Extended Analysis** and submit the same notebook.
