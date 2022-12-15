"""
temporal.py

temporal drought analysis
during the Majapahit era

12/15/22
SHSH <herho@terpmail.umd.edu>
"""

# import libs & plot styling
import xarray as xr
import pyleoclim as pyleo
import matplotlib.pyplot as plt

plt.style.use("ggplot")
plt.rcParams['figure.dpi'] = 300


# open netcdf
jja = xr.open_dataset("https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/steiger2018/da_hydro_JunAug_r.1-2000_d.05-Jan-2018.nc")

# data preprocessing
glob_pdsi = jja["pdsi_mn"] # pdsi recon. mean
nino34 = jja["Nino_3.4_mn"] # nino34 sst recon. mean

def nino_avg(index):
    """
    returns annual avg.
    index : nino34 idx
    """
    arr = index.to_numpy()
    return np.mean(arr.reshape(-1, 12), axis=1)[1292:1527]

avgNino34 = nino_avg(nino34) # annual mean nino34

maja_pdsi = glob_pdsi.sel(lat=slice(-20, 20),lon=slice(90, 160), time=slice(1293, 1527))
wp_itcz = jja["WPac_mn"].sel(time=slice(1293, 1527)).to_numpy()
t = maja_pdsi.time.to_numpy()
maja_spei_ts = maja_spei.mean(dim=("lat", "lon")).to_numpy()

ts_nino34 = pyleo.Series(time=t, value=avgNino34,
                         time_name="Year", value_name="Niño 3.4",
                         time_unit="CE", value_unit="$^{\circ}$C")

ts_pdsi = pyleo.Series(time=t, value=maja_pdsi_ts, time_name="Year",
                      value_name="PDSI",time_unit="CE")

ts_itcz = pyleo.Series(time=t, value= wp_itcz, time_name="Year", value_unit="$^{\circ}$ lat",
                      value_name="WP ITCZ", time_unit="CE")

# stackplot
ms = pyleo.MultipleSeries([ts_itcz, ts_nino34, ts_spei])
ms.stackplot()

# wavelets
## itcz vs pdsi
coh = ts_itcz.wavelet_coherence(ts_pdsi,method='wwz')
coh_sig = coh.signif_test(number=500)
coh_sig.plot()

## enso vs pdsi
coh = ts_nino34.wavelet_coherence(ts_pdsi,method='wwz')
coh_sig = coh.signif_test(number=100)
coh_sig.plot()

## itcz vs enso
coh = ts_itcz.wavelet_coherence(ts_nino34,method='wwz')
coh_sig = coh.signif_test(number=100)
coh_sig.plot()