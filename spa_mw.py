"""
spa_mw.py: script to calc. mw u test for drought extent.

SHSH <herho@terpmail.umd.edu>
12/16/22
"""

import numpy as np
import pandas as pd
import xarray as xr
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt

plt.style.use("seaborn")
plt.rcParams['figure.dpi'] = 300


# open netcdf
ds = xr.open_dataset("https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/steiger2018/da_hydro_JunAug_r.1-2000_d.05-Jan-2018.nc")


# data preprocessing
pdsi = ds["pdsi_mn"].sel(lat=slice(-20, 20),lon=slice(90, 160), time=slice(1293, 1527))

ref = (pdsi.mean(dim="time"))
ref = ref.to_numpy().flatten()

jaya = pdsi.sel(time=slice(1309, 1328)).mean(dim="time")
jaya = jaya.to_numpy().flatten()

heyday = pdsi.sel(time=slice(1350, 1389)).mean(dim="time")
heyday = heyday.to_numpy().flatten()

famine = pdsi.sel(time=1426)
famine = famine.to_numpy().flatten()

candra = pdsi.sel(time=1478)
candra = candra.to_numpy().flatten()

data = {"(1293 - 1527 CE)":ref,
        "(1309 - 1328 CE)":jaya, 
        "(1350 - 1389 CE)":heyday,
df = df.dropna()

ax = df.boxplot(figsize=(20,8));
ax.set_ylabel("PDSI");


# mw test
## jayanegara
jaya_mw = mannwhitneyu(x=df[df.columns[1]], y=df[df.columns[0]], alternative = 'two-sided')
print("U = ", round(jaya_mw.statistic, 3))
print("p-value = ", round(jaya_mw.pvalue, 3))

## hayam wuruk
heyday_mw = mannwhitneyu(x=df[df.columns[2]], y=df[df.columns[0]], alternative = 'two-sided')
print("U = ", round(heyday_mw.statistic, 3))
print("p-value = ", round(heyday_mw.pvalue, 3))

## famine
fam_mw = mannwhitneyu(x=df[df.columns[3]], y=df[df.columns[0]], alternative = 'two-sided')
print("U = ", round(fam_mw.statistic, 3))
print("p-value = ", round(fam_mw.pvalue, 3))


## candrasengkala
cs_mw = mannwhitneyu(x=df[df.columns[4]], y=df[df.columns[0]], alternative = 'two-sided')
print("U = ", round(cs_mw.statistic, 3))
print("p-value = ", round(cs_mw.pvalue, 3))
