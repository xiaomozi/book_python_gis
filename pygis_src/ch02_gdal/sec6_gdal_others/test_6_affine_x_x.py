#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
dataset.GetGCPs()
dataset.GetGeoTransform()
###############################################################################
###############################################################################
###############################################################################
dataset.GetGeoTransform()
dataset.RasterXSize
dataset.RasterYSize
###############################################################################
###############################################################################
# from osgeo import gdal
# dataset = gdal.Open("e:/gisdata/gtif/spot.tif")
# dir(dataset)
sr = dataset.GetProjectionRef()
sr
###############################################################################
