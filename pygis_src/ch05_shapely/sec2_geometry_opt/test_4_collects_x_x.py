#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import LineString
a = LineString([(0, 0), (1,1), (1,2), (2,2)])
b = LineString([(0, 0), (1,1), (2,1), (2,2)])
x = a.intersection(b)
from pprint import pprint
pprint(list(x))
###############################################################################
from shapely.geometry import MultiPoint
m = MultiPoint([(0, 0), (1, 1), (1,2), (2,2)])
m[:1].wkt
m[3:].wkt
m[4:].wkt
###############################################################################
from shapely.geometry import MultiPoint
points = MultiPoint([(0.0, 0.0), (1.0, 1.0)])
points.area
points.length
points.bounds
###############################################################################
import pprint
pprint.pprint(list(points.geoms))
pprint.pprint(list(points))
###############################################################################
from shapely.geometry import MultiLineString
coords = [((0, 0), (1, 1)), ((-1, 0), (1, 0))]
lines = MultiLineString(coords)
lines.area
lines.length
lines.bounds
len(lines.geoms)
###############################################################################
pprint.pprint(list(lines.geoms))
pprint.pprint(list(lines))
###############################################################################
