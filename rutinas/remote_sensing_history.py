import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

# CZCS onboard Nimbus-7
# OCTS onboard ADEOS
# SW onboard OrbView-2
# MODIS onboard Aqua
# MERIS onboard Envisat
# VIIRS onboard SNPP
# GOCI onboard COMS
# OLCI onboard Sentinel-3
# Hawkeye onboard Seahawk

time_range = pd.date_range('1978-01-01', '2022-12-01', freq='MS')
time_CZCS = pd.date_range('1978-11-01', '1986-06-01', freq='MS')
time_OCTS = pd.date_range('1996-11-01', '1997-07-01', freq='MS')
time_SWF = pd.date_range('1997-09-01', '2010-12-01', freq='MS')
time_MODIS = pd.date_range('2002-02-01', '2022-12-01', freq='MS')
time_MERIS = pd.date_range('2002-05-01', '2012-04-01', freq='MS')
time_VIIRS = pd.date_range('2012-01-01', '2022-12-01', freq='MS')
time_GOCI = pd.date_range('2011-04-01', '2022-12-01', freq='MS')
time_OLCI = pd.date_range('2016-12-01', '2022-12-01', freq='MS')
time_hawkeye = pd.date_range('2018-04-01', '2022-12-01', freq='MS')

time = [time_CZCS, time_OCTS, time_SWF, time_MODIS, time_MERIS,
        time_VIIRS, time_GOCI, time_OLCI, time_hawkeye]

sensors = ('CZCS', 'OCTS', 'SWF', 'MODIS', 'MERIS', 'VIIRS', 'GOCI', 'OLCI', 'hawkeye')
colors = ['red', 'orange', 'gold', 'lawngreen', 'mediumturquoise', 'seagreen', 'darkcyan', 'blueviolet', 'darkmagenta']
y_pos = np.arange(len(sensors))

# Declaring a figure "gnt"
plt.close('all')
fig, gnt = plt.subplots(figsize=(4, 2.5))

gnt.set_xlim(pd.Timestamp(time_range[0]), pd.Timestamp(time_range[-1]))
gnt.set_ylim(-1, 9)
gnt.set_xlabel('Time [Years]', fontsize=6)
gnt.set_ylabel('Sensor', fontsize=6)
gnt.set_yticks(y_pos)
gnt.set_yticks([])
gnt.set_yticklabels(sensors)
gnt.set_yticklabels([])
gnt.grid(axis='y', lw=0.2)
gnt.axvspan(pd.Timestamp(time_CZCS[-1]), pd.Timestamp(time_OCTS[0]), alpha=0.15, color='grey', edgecolor=None)

for i in range(len(sensors)):
    itime = time[i]
    start = pd.Timestamp(itime[0])
    finish = pd.Timestamp(itime[-1])
    dif = finish - start

    gnt.broken_barh( [(start, dif)], (y_pos[i]-0.25,0.5), facecolors=(colors[i]), alpha=0.65)
    gnt.axvline(x=dt.date.today(), color='gray', lw=0.6)

    start = pd.Timestamp(itime[2])
    gnt.text(start, y_pos[i]-0.1, sensors[i], fontsize=5)

gnt.set_title('Global ocean color sensors', fontsize=6, loc='left')
gnt.tick_params(labelsize=6)
fig.savefig('/home/daniu/Documentos/charla_GIS/figuras/global_ocean_color_sensors.pdf', bbox_inches='tight')
