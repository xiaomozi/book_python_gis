#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
inshp='/gdata/world_borders.shp'
datasource = ogr.Open(inshp)
layer = datasource.GetLayer(0)
dir(layer)[:6] + ['... ...'] + dir(layer)[-4:]
###############################################################################
layer.GetFeatureCount()
###############################################################################
layer.GetExtent()
###############################################################################
layerdef = layer.GetLayerDefn()
for i in range(layerdef.GetFieldCount()):
    defn = layerdef.GetFieldDefn(i)
    print(defn.GetName(),defn.GetWidth(),defn.GetType(),defn.GetPrecision())
