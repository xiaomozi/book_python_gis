#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import gdal
src_filename = "/gdata/lu75c.tif"
dst_filename = "/tmp/xx_copy_img.tif"
driver = gdal.GetDriverByName('GTiff')
src_ds = gdal.Open( src_filename )
dst_ds = driver.CreateCopy( dst_filename, src_ds, 0 )
###############################################################################
dst_filename2 = "/tmp/K52E015007_copy2.tif"
dst_ds = driver.CreateCopy( dst_filename2, src_ds, 0,
   [ 'TILED=YES', 'COMPRESS=PACKBITS' ] )
dst_filename3 = "/tmp/K52E015007_copy3.tif"
dst_ds3 = driver.CreateCopy( dst_filename3, src_ds, 0,
   [ 'TILED=YES', 'COMPRESS=PACKBITS' ] )
###############################################################################
dataset = gdal.Open("/gdata/K52E015007.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("/tmp/sd.tif",dataset,0);
###############################################################################
dataset = gdal.Open("/gdata/K52E015007.tif")
width = dataset.RasterXSize
height = dataset.RasterYSize
data = dataset.ReadAsArray(0,0,width,height)
driver = gdal.GetDriverByName("GTiff")
driver.CreateCopy("/tmp/sd2.tif",dataset,0,["INTERLEAVE=PIXEL"]);
