#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid
para = {
    'projection': 'tmerc',
    'lat_0': 0,
    'lon_0': 3,
    'llcrnrlon': 1.819757266426611,
    'llcrnrlat': 41.583851612359275,
    'urcrnrlon': 1.841589961763497,
    'urcrnrlat': 41.598674173123
}
dem_tif = '/gdata/sample_files/dem.tiff'
###############################################################################
p1 = plt.subplot(121)
map = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
cs = map.contour(xx, yy, data, range(400, 1500, 100), cmap=plt.cm.cubehelix)
p2 = plt.subplot(122)
map = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
cs = map.contour(xx, yy, data, range(400, 1500, 100), cmap=plt.cm.cubehelix)
plt.clabel(cs, inline=True, fmt='%1.0f', fontsize=12, colors='k')
plt.show()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
p1 = plt.subplot(121)
map = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
map.contourf(xx, yy, data)
###############################################################################
p2 = plt.subplot(122)
map = Basemap(**para)
ds = gdal.Open(dem_tif)
data = ds.ReadAsArray()
x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)
map.pcolormesh(xx, yy, data)
plt.show()
