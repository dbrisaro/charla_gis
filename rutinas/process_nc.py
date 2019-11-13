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

# zonal and meridional mean
mean_chl_meridional = data_chl_pp.mean(dim=('lat'))
mean_chl_zonal = data_chl_pp.mean(dim=('lon'))

# plot of two panels
fig, ax = plt.subplots(1, 2)
mean_chl_zonal.chlor_a.plot(ax=ax[0])
mean_chl_meridional.chlor_a.plot(ax=ax[1])
plt.savefig(dire + 'figuras/zonal-merid-chl.png', bbox_inches='tight')

# select one longitud, lets say 64W
data_chl_pp_64W = data_chl_pp.sel(lon=[-64], method='nearest')

# plot of two panels
fig, ax = plt.subplots(1, 2)
data_chl_pp_64W.chlor_a.plot(ax=ax[0])
data_chl_pp_64W.chlor_a.plot.hist(ax=ax[1])
plt.savefig(dire + 'figuras/chl_64W.png', bbox_inches='tight')

plt.close('all')
