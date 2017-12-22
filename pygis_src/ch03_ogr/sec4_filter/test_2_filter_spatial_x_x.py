#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os
from osgeo import ogr
def create_shp_by_layer(shp, layer):
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver. CreateDataSource ( outputfile )
    pt_layer = newds.CopyLayer ( layer, '')
    newds.Destroy ()
###############################################################################
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = '/gdata/world_borders.shp'
cover_shp = '/gdata/10740.shp'
world_ds = ogr.Open(world_shp)
cover_ds = ogr.Open(cover_shp)
world_layer = world_ds.GetLayer(0)
cover_layer = cover_ds.GetLayer(0)
###############################################################################
world_layer.GetFeatureCount()
###############################################################################
cover_feats = cover_layer.GetNextFeature()
poly = cover_feats.GetGeometryRef()
world_layer.SetSpatialFilter(poly)
out_shp = '/tmp/world_cover.shp'
create_shp_by_layer(out_shp, world_layer)
###############################################################################
from osgeo import ogr
import os
shpfile = '/gdata/world_borders.shp'
ds = ogr.Open(shpfile)
world_layer = ds.GetLayer(0)
world_layer.SetSpatialFilterRect(50, 60, 25, 35)
print(world_layer.GetFeatureCount())
out_shp = '/gdata/world_spatial_filter.shp'
create_shp_by_layer(out_shp, world_layer)
