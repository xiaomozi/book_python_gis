#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
import os
shpfile = '/gdata/world_borders.shp'
ds = ogr.Open(shpfile)
layer = ds.GetLayer(0)
lyr_count = layer.GetFeatureCount()
print(lyr_count)
###############################################################################
layer.SetAttributeFilter("AREA > 800000")
lyr_count = layer.GetFeatureCount()
print(lyr_count)
###############################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
extfile = '/tmp/xx_filter_attr.shp'
if os.access(extfile, os.F_OK):
    driver.DeleteDataSource(extfile)

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect', None, ogr.wkbPolygon)
feat = layer.GetNextFeature()
while feat is not None:
    layernew.CreateFeature(feat)
    feat = layer.GetNextFeature()
newds.Destroy()
