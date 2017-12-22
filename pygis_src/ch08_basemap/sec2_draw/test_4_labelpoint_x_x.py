#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
my_map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                 resolution='h', area_thresh=0.1,
                 llcrnrlon=-136.25, llcrnrlat=56.0,
                 urcrnrlon=-134.25, urcrnrlat=57.75)
my_map.drawcoastlines(); my_map.drawcountries(); my_map.drawmapboundary()
# my_map.fillcontinents(color='coral')
lons = [-135.3318, -134.8331, -134.6572]
lats = [57.0799, 57.0894, 56.2399]
x, y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)
###############################################################################
labels = ['Sitka', 'Baranof Warm Springs', 'Port Alexander']
###############################################################################
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt, ypt, label)
plt.show()
###############################################################################
my_map.drawcoastlines(); my_map.drawcountries(); my_map.drawmapboundary()
x,y = my_map(lons, lats)
my_map.plot(x, y, 'bo', markersize=10)
for label, xpt, ypt in zip(labels, x, y):
    plt.text(xpt+10000, ypt+5000, label)
plt.show()
