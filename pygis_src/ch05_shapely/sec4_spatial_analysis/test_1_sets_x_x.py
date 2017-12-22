#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import LineString, MultiLineString, Point
from pprint import pprint
coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
lines.boundary
lines.boundary.boundary
lines.boundary.boundary.is_empty
###############################################################################
LineString([(0, 0), (1, 1)]).centroid
LineString([(0, 0), (1, 1)]).centroid.wkt
###############################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.difference(b)
###############################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.intersection(b)
###############################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.symmetric_difference(b)
###############################################################################
a = Point(1, 1).buffer(1.5)
b = Point(2, 1).buffer(1.5)
a.union(b)
###############################################################################
a.union(b).boundary
a.boundary.union(b.boundary)
