"""
spatial_anal.py

Calculate pdsi spatial
anomaly during the Majapahit era

12/15/22
SHSH <herho@terpmail.umd.edu>
"""

# import libs & plot styling
import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

plt.style.use("bmh")
plt.rcParams['figure.dpi'] = 300


# open netcdf
ds = xr.open_dataset("https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/steiger2018/da_hydro_JunAug_r.1-2000_d.05-Jan-2018.nc")

# data preprocessing
pdsi = ds["pdsi_mn"].sel(lat=slice(-20, 20),lon=slice(90, 160), time=slice(1293, 1527))
ref = (pdsi.mean(dim="time")).rename("PDSI anomaly")
heyday = (pdsi.sel(time=slice(1350, 1389)).mean(dim="time") - ref).rename("PDSI anomaly")
candra = (pdsi.sel(time=1478) - ref).rename("PDSI anomaly")
famine = (pdsi.sel(time=1426) - ref).rename("PDSI anomaly")
jayanegara = (pdsi.sel(time=slice(1309, 1319)).mean(dim="time") - ref).rename("PDSI anomaly")


# plotting
fig = plt.figure(figsize=(12, 5));
ax = fig.add_subplot(111, projection=ccrs.PlateCarree());
jayanegara.plot(ax=ax, transform=ccrs.PlateCarree(), 
                x='lon', y='lat', cmap="bwr_r", levels=np.arange(-2, 2.5, .5));
ax.coastlines();
ax.gridlines();
ax.set_title("(a) 1309 - 1328 CE");

fig = plt.figure(figsize=(12, 5));
ax = fig.add_subplot(111, projection=ccrs.PlateCarree());
heyday.plot(ax=ax, transform=ccrs.PlateCarree(), 
            x='lon', y='lat', cmap="bwr_r", levels=np.arange(-2, 2.5, .5));
ax.coastlines();
ax.gridlines();
ax.set_title("(b) 1350 - 1389 CE");

fig = plt.figure(figsize=(12, 5));
ax = fig.add_subplot(111, projection=ccrs.PlateCarree());
famine.plot(ax=ax, transform=ccrs.PlateCarree(),
            x='lon', y='lat', cmap="bwr_r", levels=np.arange(-2, 2.5, .5));
ax.coastlines();
ax.gridlines();
ax.set_title("(c) 1426 CE");

fig = plt.figure(figsize=(12, 5));
ax = fig.add_subplot(111, projection=ccrs.PlateCarree());
candra.plot(ax=ax, transform=ccrs.PlateCarree(),
            x='lon', y='lat', cmap="bwr_r", levels=np.arange(-2, 2.5, .5));
ax.coastlines();
ax.gridlines();
ax.set_title("(d) 1478 CE");