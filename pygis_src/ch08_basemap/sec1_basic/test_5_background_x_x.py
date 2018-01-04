#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.subplot(121)
map = Basemap(projection='ortho',lon_0=0,lat_0=0,resolution='c')
map.drawmapboundary()
plt.subplot(122)
map = Basemap(projection='sinu',lon_0=0,resolution='c')
map.drawmapboundary(fill_color='aqua')
plt.show()
###############################################################################
map = Basemap()
map.drawcoastlines()
plt.show()
###############################################################################
map = Basemap(projection='poly',
              lon_0=0.0, lat_0=0,
              llcrnrlon=-80.,llcrnrlat=-40,urcrnrlon=80.,urcrnrlat=40.)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
###############################################################################
map.drawmeridians(range(0, 360, 20))
###############################################################################
map.drawparallels(range(-90, 100, 10), linewidth=2, dashes=[4, 2], labels=[1,0,0,1], color='r' )
plt.show()
###############################################################################
###############################################################################
map = Basemap(projection='ortho', lat_0=0, lon_0=0)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()
plt.show()
