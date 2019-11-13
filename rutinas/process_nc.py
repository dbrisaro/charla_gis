"""
En esta rutina exploramos un archivo .nc proveniente del
sensor MODIS a bordo del satelite Aqua

Dani Risaro
Noviembre 2019
"""


import xarray as xr                                     # importo libreria xarray
import matplotlib.pyplot as plt                         # importo para graficar
import numpy as np

dire = '/home/daniu/Documentos/charla_GIS/'             # directorio/ruta
filename = 'A20022132002243.L3m_MO_CHL.x_chlor_a.nc'    # nombre del archivo
data_chl = xr.open_dataset(dire + filename)

print(data_chl)                                         # print data del .nc

# select an area
data_chl_pp = data_chl.sel(lat=slice(-40, -55), lon=slice(-70, -46))

# simple plot
levels = np.linspace(0,3.5,15)
data_chl_pp.chlor_a.plot(levels=levels)
plt.savefig(dire + 'figuras/map-chl.png', bbox_inches='tight')
plt.savefig(dire + 'figuras/map-chl.pdf', bbox_inches='tight')

# zonal and meridional mean
mean_chl_meridional = data_chl_pp.mean(dim=('lat'))
mean_chl_zonal = data_chl_pp.mean(dim=('lon'))

# plot of two panels
fig, ax = plt.subplots(1, 2)
mean_chl_zonal.chlor_a.plot(ax=ax[0])
mean_chl_meridional.chlor_a.plot(ax=ax[1])
plt.savefig(dire + 'figuras/zonal-merid-chl.png', bbox_inches='tight')
plt.savefig(dire + 'figuras/zonal-merid-chl.pdf', bbox_inches='tight')

# select one longitud, lets say 64W
data_chl_pp_64W = data_chl_pp.sel(lon=[-64], method='nearest')

# plot of two panels
fig, ax = plt.subplots(1, 2)
data_chl_pp_64W.chlor_a.plot(ax=ax[0])
data_chl_pp_64W.chlor_a.plot.hist(ax=ax[1])
plt.savefig(dire + 'figuras/chl_64W.png', bbox_inches='tight')
plt.savefig(dire + 'figuras/chl_64W.pdf', bbox_inches='tight')


# Load the file with the data of SWF and MODIS from 2000 to 2010
filename = 'chl_9km_70-55W_55-40S_2000-2010.nc'    # nombre del archivo
data_chl = xr.open_dataset(dire + filename)

data_chl_gsm = data_chl.sel(latitude=slice(-40, -43), longitude=slice(-65, -60))    # select an area

# zonal and meridional mean
mean_chl_spatial = data_chl_gsm.mean(dim=('latitude', 'longitude'))

# plot of a mean time serie
mean_chl_spatial.chl.plot(aspect=3, size=2)
plt.savefig(dire + 'figuras/spatial-mean-timeseries-chl-gsm.png', bbox_inches='tight')
plt.savefig(dire + 'figuras/spatial-mean-timeseries-chl-gsm.pdf', bbox_inches='tight')


# plot of time series from selected gridpoints
data_chl_gsm_points = data_chl_gsm.sel(longitude=[-64], latitude=[-42,-43], method='nearest').squeeze()
data_chl_gsm_points.chl.plot.line(x='time', aspect=3, size=2)
plt.savefig(dire + 'figuras/gridpoints-timeseries-chl-gsm.png', bbox_inches='tight')
plt.savefig(dire + 'figuras/gridpoints-timeseries-chl-gsm.pdf', bbox_inches='tight')
plt.close('all')
