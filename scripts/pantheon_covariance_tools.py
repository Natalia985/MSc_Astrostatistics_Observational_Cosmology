"""Utilities for Pantheon+ teaching labs 03-05.

All astronomical measurements come from the public Pantheon+ / SH0ES release.
"""
from pathlib import Path
import requests
import numpy as np
import pandas as pd
from scipy.linalg import cho_factor, cho_solve
from astropy.cosmology import FlatLambdaCDM

BASE = (
    "https://raw.githubusercontent.com/PantheonPlusSH0ES/"
    "DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/"
)
URL_DATA = BASE + "Pantheon%2BSH0ES.dat"
URL_STAT = BASE + "Pantheon%2BSH0ES_STATONLY.cov"
URL_FULL = BASE + "Pantheon%2BSH0ES_STAT%2BSYS.cov"

def download(url, path):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists():
        r=requests.get(url,timeout=180)
        r.raise_for_status()
        path.write_bytes(r.content)
    return path

def read_cov(path):
    x=np.loadtxt(path)
    n=int(x[0])
    if x[1:].size != n*n:
        raise ValueError("Covariance size mismatch")
    return x[1:].reshape(n,n)
