# Data Directory

Suggested local structure:

```text
data/
├── raw/
│   ├── pantheon_plus/
│   ├── sdss_rm/
│   ├── sdss_agn/
│   └── desi_bao/
└── teaching/
```

`raw/` is ignored by Git.

Small instructor-created derivative tables may be committed under `teaching/` only if:
- every row comes from real observations;
- provenance is documented;
- no synthetic values are inserted.
