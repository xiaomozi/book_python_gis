#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import asShape
d = {"type": "Point", "coordinates": (0.0, 0.0)}
shape = asShape(d)
shape.geom_type
tuple(shape.coords)
list(shape.coords)
###############################################################################
class GeoThing(object):
    def __init__(self, d):
        self.__geo_interface__ = d
thing = GeoThing({"type": "Point", "coordinates": (0.0, 0.0)})
shape = asShape(thing)
shape.geom_type
tuple(shape.coords)
list(shape.coords)
###############################################################################
from shapely.geometry import mapping
thing = GeoThing({"type": "Point", "coordinates": (0.0, 0.0)})
m = mapping(thing)
m['type']
m['coordinates']
