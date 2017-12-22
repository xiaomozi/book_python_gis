#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
import time
dataset = gdal.Open("/gdata/lu75c.tif")
band = dataset.GetRasterBand(1)
width, height = dataset.RasterXSize, dataset.RasterYSize
bw, bh = 128, 128
bxsize = width/bw
bysize = height/bh
band.ReadAsArray(0,0,width,height)
start = time.time()
band.ReadAsArray(0,0,width,height)
print (time.time()-start)
start2 = time.time()
for i in range(int(bysize)):
    for j in range(int(bxsize)):
        band.ReadAsArray(bw*j,bh*i,bw,bh)
print (time.time()-start2)
###############################################################################
