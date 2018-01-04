#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
###############################################################################
map = Basemap()
###############################################################################
map.drawcoastlines()
plt.show()
###############################################################################
plt.savefig('xx_test.png')
###############################################################################
map = Basemap(projection='ortho',lat_0=0, lon_0=105)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color= 'coral',lake_color='aqua')
map.drawcoastlines()
plt.show()
###############################################################################
plt.cla()   # Clear axis
plt.clf()   # Clear figure
plt.close() # Close a figure window
