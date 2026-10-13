from pathlib import Path
from astroquery.vizier import Vizier

OUT = Path("data/raw/sdss_rm")
OUT.mkdir(parents=True, exist_ok=True)

Vizier.ROW_LIMIT = -1

sample = Vizier.get_catalogs("J/ApJ/851/21/table1")[0]
sample.write(OUT / "sdss_rm_table1.fits", overwrite=True)

lc = Vizier.get_catalogs("J/ApJ/851/21/table2")[0]
lc.write(OUT / "sdss_rm_table2.fits", overwrite=True)

print("Saved SDSS-RM tables to", OUT)
