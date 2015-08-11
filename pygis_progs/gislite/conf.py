import os
import sys

from osgeo import gdal

__author__ = 'bukun@osgeo.cn'
datadir = r'D:\vshare\opt\gdata'

tif_landsat7 = os.path.join(datadir, 'landsat7.img')
landsat7ds = gdal.Open(tif_landsat7)