#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)
my_map.drawmapboundary(fill_color='aqua')
my_map.fillcontinents(color='#cc9955',lake_color='aqua')
my_map.drawcoastlines()
lon = -135.3318
lat = 57.07
x, y = my_map(lon, lat)
plt.text(x, y, 'Lagos',fontsize=12,fontweight='bold',
                    ha='left',va='bottom',color='k')
lon = -136
lat = 56.3
x, y = my_map(lon, lat)
plt.text(x, y, 'Barcelona',fontsize=12,fontweight='bold',
                    ha='left',va='center',color='k',
                    bbox=dict(facecolor='b', alpha=0.2))
plt.show()
