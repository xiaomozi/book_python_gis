#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import gdal
dataset = gdal.Open('/gdata/lu75c.tif')
dataset.RasterCount
band = dataset.GetRasterBand(1)
###############################################################################
dir(band)
###############################################################################
band.XSize
band.YSize
band.DataType
###############################################################################
band.GetNoDataValue()
band.GetMaximum()
band.GetMinimum()
band.ComputeRasterMinMax()
