#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import shapefile
w = shapefile.Writer()
###############################################################################
w = shapefile.Writer(shapeType=1)
w.shapeType
###############################################################################
w.shapeType = 3
w.shapeType
###############################################################################
w.autoBalance = 1
###############################################################################
w = shapefile.Writer()
w.point(122, 37)
w.shapes()[0].points
###############################################################################
w.point(118, 36, 4, 8)
w.shapes()[1].points
###############################################################################
w = shapefile.Writer()
w.poly(shapeType=3,
       parts=[[[122, 37, 4, 9], [117, 36, 3, 4]],
       [[115, 32, 8, 8], [118, 20, 6, 4], [113, 24]]])
###############################################################################
w = shapefile.Writer()
w.null()
###############################################################################
assert w.shapes()[0].shapeType == shapefile.NULL
###############################################################################
w = shapefile.Writer(shapefile.POINT)
w.point(1,1)
w.point(3,1)
w.point(4,3)
w.point(2,2)
w.field('FIRST_FLD')
w.field('SECOND_FLD','C','40')
w.record('First','Point')
w.record('Second','Point')
w.record('Third','Point')
w.record('Fourth','Point')
w.save('xx_sf_point')
###############################################################################
w = shapefile.Writer(shapefile.POLYGON)
w.poly(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.field('FIRST_FLD','C','40')
w.field('SECOND_FLD','C','40')
w.record('First','Polygon')
w.save('xx_sf_polygon')
###############################################################################
w = shapefile.Writer(shapefile.POLYLINE)
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.poly(parts=[[[1,3],[5,3]]], shapeType=shapefile.POLYLINE)
w.field('FIRST_FLD','C','40')
w.field('SECOND_FLD','C','40')
w.record('First','Line')
w.record('Second','Line')
w.save('xx_sf_line')
###############################################################################
w = shapefile.Writer(shapefile.POLYLINE)
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])
w.field('FIRST_FLD','C','40')
w.field('SECOND_FLD','C','40')
w.record(FIRST_FLD='First', SECOND_FLD='Line')
w.save('xx_sf_line2')
###############################################################################
targetName = w.save()
assert("shapefile_" in targetName)
###############################################################################
try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

shp = StringIO()
shx = StringIO()
dbf = StringIO()
w.saveShp(shp)
w.saveShx(shx)
w.saveDbf(dbf)
###############################################################################
shp = shx = dbf = None
