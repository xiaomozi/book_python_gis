#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from geojson import Point
Point((-115.81, 37.24))  # doctest: +ELLIPSIS
###############################################################################
from geojson import MultiPoint
MultiPoint([(-155.52, 19.61), (-156.22, 20.74), (-157.97, 21.46)])  # doctest: +ELLIPSIS
###############################################################################
from geojson import LineString
LineString([(8.919, 44.4074), (8.923, 44.4075)])  # doctest: +ELLIPSIS
###############################################################################
from geojson import MultiLineString
MultiLineString([
    [(3.75, 9.25), (-130.95, 1.52)],
    [(23.15, -34.25), (-1.35, -4.65), (3.45, 77.95)]
])  # doctest: +ELLIPSIS
###############################################################################
from geojson import Polygon
Polygon([[(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)]])  # doctest: +ELLIPSIS
###############################################################################
# hole within polygon
Polygon([
    [(2.38, 57.322), (23.194, -20.28), (-120.43, 19.15), (2.38, 57.322)],
    [(-5.21, 23.51), (15.21, -10.81), (-20.51, 1.51), (-5.21, 23.51)]
])  # doctest: +ELLIPSIS
###############################################################################
from geojson import MultiPolygon
MultiPolygon([
    ([(3.78, 9.28), (-130.91, 1.52), (35.12, 72.234), (3.78, 9.28)],),
    ([(23.18, -34.29), (-1.31, -4.61), (3.41, 77.91), (23.18, -34.29)],)
])  # doctest: +ELLIPSIS
###############################################################################
from geojson import GeometryCollection, Point, LineString
my_point = Point((23.532, -63.12))
my_line = LineString([(-152.62, 51.21), (5.21, 10.69)])
GeometryCollection([my_point, my_line])  # doctest: +ELLIPSIS
###############################################################################
from geojson import Feature, Point
my_point = Point((-3.68, 40.41))
Feature(geometry=my_point)  # doctest: +ELLIPSIS
###############################################################################
Feature(geometry=my_point, properties={"country": "Spain"})  # doctest: +ELLIPSIS
###############################################################################
Feature(geometry=my_point, id=27)  # doctest: +ELLIPSIS
###############################################################################
from geojson import Feature, Point, FeatureCollection
my_feature = Feature(geometry=Point((1.6432, -19.123)))
my_other_feature = Feature(geometry=Point((-80.234, -22.532)))
FeatureCollection([my_feature, my_other_feature])  # doctest: +ELLIPSIS