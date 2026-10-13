# GitHub Setup

## Recommended repository name

`MSc_Astrostatistics_Observational_Cosmology`

This should be a separate repository from the older binary-SMBH course because the scientific spine, data sources and assessment structure are now substantially different.

## Create the repository

On GitHub:

1. New repository
2. Name: `MSc_Astrostatistics_Observational_Cosmology`
3. Choose Public or Private
4. Do not initialise with a README if uploading this prepared package
5. Create repository

## Terminal upload

After unzipping the prepared package:

```bash
cd MSc_Astrostatistics_Observational_Cosmology
git init -b main
git add .
git commit -m "Initial real-data observational cosmology course"
git remote add origin https://github.com/lionandjelka/MSc_Astrostatistics_Observational_Cosmology.git
git push -u origin main
```

## Updating later

```bash
git status
git add -A
git commit -m "Update course materials"
git push origin main
```

## Never commit

- large public survey releases;
- private student submissions;
- API tokens;
- local cache files;
- raw FITS archives.

The `.gitignore` in this package already excludes `data/raw/`.
