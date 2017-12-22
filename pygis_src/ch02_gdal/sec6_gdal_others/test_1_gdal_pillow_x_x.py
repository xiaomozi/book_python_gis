#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
data_arr = dataset.ReadAsArray(30,70,5,5)
type(data_arr)
data_arr
data_bin = dataset.ReadRaster(30,70,5,5)
data_bin
###############################################################################
data_arr.tostring()
###############################################################################
from PIL import Image
im = Image.open("/gdata/K52E015007.tif")
region = im.crop((30,70,35,75))
region.tobytes()
###############################################################################
import numpy as np
data = dataset.ReadAsArray(30,70,5,5)
datas = [i for i in data]
from numpy import reshape
datas = [reshape(i,(-1,1)) for i in data]
datas = np.concatenate(datas,1)
datas.tostring()
###############################################################################
r,g,b = region.split()
r.tobytes()
band = dataset.GetRasterBand(1)
band.ReadRaster(30,70,5,5)
