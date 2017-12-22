#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mpl_toolkits.basemap
print(mpl_toolkits.basemap.supported_projections)
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
map = Basemap(projection='cyl')
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()
###############################################################################
map = Basemap(projection='aeqd', lon_0=180, lat_0=50)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral', lake_color='aqua')
map.drawcoastlines()
plt.show()
###############################################################################
###############################################################################
map = Basemap(projection='mbtfpq', lon_0=105)
###############################################################################
map.drawcoastlines()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()
