#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
###############################################################################
map = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)
map = Basemap(projection='robin', lat_0=0, lon_0=-100,
                 resolution='l', area_thresh=1000.0)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.drawcoastlines()
# map.readshapefile('/gdata/world_borders', 'comarques')
map.readshapefile('/gdata/GSHHS_c', 'comarques')
plt.show()
###############################################################################
map = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.drawcoastlines()
# map.readshapefile('/gdata/sample_files/comarques', 'comarques')
plt.show()
# plt.savefig( get_tmp_file(__file__, 2))

