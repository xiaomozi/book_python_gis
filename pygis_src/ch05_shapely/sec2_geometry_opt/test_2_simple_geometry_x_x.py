#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import Point
point = Point(0.0, 0.0)
###############################################################################
from shapely.geometry import LineString
line = LineString([(0, 0), (1, 1)])
print(line.area)
print(line.length)
###############################################################################
print(line.bounds)
###############################################################################
len(line.coords)
list(line.coords)
###############################################################################
LineString(line)
###############################################################################
from shapely.geometry import Polygon, LinearRing
ring = LinearRing([(0, 0), (1, 1), (1, 0)])
list(ring.coords)
###############################################################################
from shapely.geometry import  Polygon
from shapely.geometry import LinearRing
polygon = Polygon([(0, 0), (1, 1), (1, 0)])
###############################################################################
list(polygon.interiors)
coords = [(0, 0), (1, 1), (1, 0)]
r = LinearRing(coords)
s = Polygon(r)
s.area
t = Polygon(s.buffer(1.0).exterior, [r])
t.area
###############################################################################
from shapely.geometry import Polygon, box
b = box(0.0, 0.0, 1.0, 1.0)
list(b.exterior.coords)
###############################################################################
b.orient(polygon,sign=1.0)
