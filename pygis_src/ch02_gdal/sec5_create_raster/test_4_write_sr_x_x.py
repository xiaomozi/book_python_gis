#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import osr
import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
datas = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
tods = driver.Create("/tmp/x_K52E015007_3.tif",width,height,3,options=["INTERLEAVE=PIXEL"])
tods.SetGeoTransform( [ 444720, 30, 0, 3751320, 0, -30 ] )
srs = osr.SpatialReference()
srs.SetUTM( 11, 1 )
srs.SetWellKnownGeogCS( 'NAD27' )
tods.SetProjection( srs.ExportToWkt() )
