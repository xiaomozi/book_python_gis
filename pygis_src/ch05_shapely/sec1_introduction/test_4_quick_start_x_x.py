#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from osgeo import ogr
import shapely
###############################################################################
print(shapely.__version__)
###############################################################################
import shapely.geos
shapely.geos.geos_version
shapely.geos.geos_capi_version
shapely.geos.geos_version_string
###############################################################################
datasource = ogr.Open('/gdata/world_borders.shp')
layer = datasource.GetLayer(0)
feature = layer.GetFeature(0)
polygon = feature.GetGeometryRef()
print(polygon.ExportToWkt())
buf = polygon.Buffer(2)
buf.ExportToWkt()[:120]
###############################################################################
from shapely import speedups
speedups.available
###############################################################################
speedups.enable()
