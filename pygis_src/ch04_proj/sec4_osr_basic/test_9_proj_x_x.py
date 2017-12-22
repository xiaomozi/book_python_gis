#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
###############################################################################
import osr
import gdal
dataset = gdal.Open("/gdata/K52E015007.tif")
sr = dataset.GetProjectionRef()
###############################################################################
osrobj = osr.SpatialReference()
osrobj3 = osr.SpatialReference()
osrobj3.SetWellKnownGeogCS("WGS84")
osrobj3.IsSame(osrobj)
osrobj3.ExportToWkt()
osrobj3.IsGeographic()
ct = osr.CoordinateTransformation(osrobj,osrobj3)
# ct.TransformPoint([590000.0,4928000.0,0])
# ct.TransformPoint(609000,4928000)
# ct.TransformPoint(609000,4914000)
# ct.TransformPoint(590000,4914000)

###############################################################################
###############################################################################
from osgeo import ogr
from osgeo import osr
source = osr.SpatialReference()
source.ImportFromEPSG(2927)
target = osr.SpatialReference()
target.ImportFromEPSG(4326)
transform = osr.CoordinateTransformation(source, target)
point = ogr.CreateGeometryFromWkt("POINT (1120351.57 741921.42)")
point.Transform(transform)
point.ExportToWkt()
