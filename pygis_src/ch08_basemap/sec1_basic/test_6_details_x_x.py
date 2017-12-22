#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
para = {
    'projection': 'merc',
    'lat_0': 38.8,
    'lon_0': 121.3,
    'resolution': 'l',
    'area_thresh': 1000.0,
    'llcrnrlon': 118,
    'llcrnrlat': 36.6,
    'urcrnrlon': 124.6,
    'urcrnrlat': 40.7
}
###############################################################################
my_map = Basemap(**para)
###############################################################################
my_map.drawcoastlines()
my_map.drawcountries()
plt.show()
###############################################################################
para['resolution'] = 'h'
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines()
my_map.drawcountries()
plt.show()
###############################################################################
para['area_thresh'] = .1
###############################################################################
my_map = Basemap(**para)
my_map.drawcoastlines()
my_map.drawcountries()
plt.show()
