#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
import numpy
dataset = gdal.Open("/gdata/K52E015007.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("/tmp/x_K52E015007_3.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.WriteRaster(0,0,width,height,datas.tostring(),width,height,band_list=[1,2,3])
###############################################################################
###############################################################################
datas = []
for i in range(3):
    band = dataset.GetRasterBand(i+1)
    data = band.ReadAsArray(0,0,width,height)
    datas.append(numpy.reshape(data,(1,-1)))
datas = numpy.concatenate(datas)
