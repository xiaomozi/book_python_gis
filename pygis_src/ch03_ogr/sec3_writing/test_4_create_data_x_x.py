#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
import os,math
inshp = '/gdata/world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = '/tmp/xx_world_borders_copy.shp'
if os.access( outputfile, os.F_OK ):
    driver.DeleteDataSource(outputfile)
pt_cp = driver.CopyDataSource(ds, outputfile)
pt_cp.Release()
###############################################################################
from osgeo import ogr
import os, math
inshp = '/gdata/world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile = '/tmp/xx_world_borders_copy2.shp'
if os.access(outputfile, os.F_OK):
    driver.DeleteDataSource(outputfile)
layer = ds.GetLayer()
newds = driver.CreateDataSource(outputfile)
###############################################################################
pt_layer = newds.CopyLayer(layer, 'abcd')
newds.Destroy()
###############################################################################
dir(pt_layer)
###############################################################################
from osgeo import ogr
import os,math
inshp = '/gdata/world_borders.shp'
ds = ogr.Open(inshp)
driver = ogr.GetDriverByName("ESRI Shapefile")
outputfile ='/tmp/xx_world_borders_copy3.shp'
if os.access( outputfile, os.F_OK ):
    driver.DeleteDataSource( outputfile )
newds = driver.CreateDataSource(outputfile)
layernew = newds.CreateLayer('worldcopy',None,ogr.wkbLineString)
###############################################################################
layer = ds.GetLayer()
feature = layer.GetNextFeature()
while feature is not None:
    layernew.CreateFeature(feature)
    feature = layer.GetNextFeature()
newds.Destroy()
dir(feature)[:6] + ['... ...'] + dir(feature)[-3:]
