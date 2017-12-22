#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.geometry import LineString
line = LineString()
line.is_empty
line.length
line.bounds
line.coords
###############################################################################
line.coords = [(0, 0), (1, 1)]
line.is_empty
line.length
line.bounds
###############################################################################
ip = LineString([(0, 0), (0, 1), (1, 1)]).interpolate(1.5)
ip.wkt
LineString([(0, 0), (0, 1), (1, 1)]).interpolate(0.75, normalized=True).wkt
###############################################################################
LineString([(0, 0), (0, 1), (1, 1)]).project(ip)
LineString([(0, 0), (0, 1), (1, 1)]).project(ip, normalized=True)
###############################################################################
