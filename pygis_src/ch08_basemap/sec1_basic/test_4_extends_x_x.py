#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
my_map = Basemap(projection='ortho', lat_0=0, lon_0=-100,
                 resolution='l', area_thresh=1000.0)
my_map.drawcoastlines()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
map = Basemap(projection='cyl')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
map = Basemap(projection='mbtfpq', lon_0=105)
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
map = Basemap(projection='sinu', lon_0=105, lat_0=39)
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()
