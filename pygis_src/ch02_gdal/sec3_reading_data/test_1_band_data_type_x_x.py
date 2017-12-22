#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdalconst
dir(gdalconst)
###############################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
band = dataset.GetRasterBand(1)
band.DataType
