"""
En esta rutina exploramos un archivo .nc proveniente del
sensor MODIS a bordo del satelite Aqua

Dani Risaro
Noviembre 2019
"""


import xarray as xr

dire = '/home/daniu/charla_gis/'
filename = 'A20021822019212.L3m_MC_CHL_chlor_a_9km.nc'
data_chl = xr.open_dataset(dire + filename)

print(data)
