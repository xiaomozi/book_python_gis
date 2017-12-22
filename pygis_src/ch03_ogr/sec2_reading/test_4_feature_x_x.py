#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
inshp ='/gdata/world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
dir(feature)
###############################################################################
layer.ResetReading()
feature = layer.GetNextFeature()
while feature:
    feature = layer.GetNextFeature()
dir(feature)
###############################################################################
layer.ResetReading()
feat=layer.GetFeature(0)
feat.keys()
feat.GetField('CNTRY_NAME')
###############################################################################
for i in range(feat.GetFieldCount()):
     print(feat.GetField(i))
###############################################################################
geom = feat.GetGeometryRef()
geom.GetGeometryName()
geom.GetGeometryCount()
geom.GetPointCount()
geom.ExportToWkt()
###############################################################################
polygon=geom.GetGeometryRef(0)
polygon.GetGeometryName()
polygon.GetGeometryCount()
polygon.GetPointCount()
polygon.GetX(0)
polygon.GetY(0)
polygon.GetZ(0)
polygon.ExportToWkt()
