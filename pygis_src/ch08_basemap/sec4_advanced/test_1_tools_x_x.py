#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid
map = Basemap(projection='tmerc',
              lat_0=0, lon_0=3,
              llcrnrlon=1.819757266426611,
              llcrnrlat=41.583851612359275,
              urcrnrlon=1.841589961763497,
              urcrnrlat=41.598674173123)
ds = gdal.Open("/gdata/sample_files/dem.tiff")
data = ds.ReadAsArray()
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
cmap = plt.get_cmap('PiYG')
colormesh = map.pcolormesh(xx, yy, data, vmin = 500, vmax = 1300, cmap=cmap)
contour = map.contour(xx, yy, data, range(500, 1350, 50), colors = 'k', linestyles = 'solid')
map.colorbar(colormesh)
cb = map.colorbar(colormesh, location='bottom', label="contour lines")
cb.add_lines(contour)
cb.set_ticks([600, 760, 1030, 1210])
plt.show()
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
map = Basemap(llcrnrlon=-10.5,llcrnrlat=35,urcrnrlon=4.,urcrnrlat=44.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = -3.25)
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#cc9955',lake_color='aqua')
map.drawcoastlines()
map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')
map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize = 14)
plt.show()
