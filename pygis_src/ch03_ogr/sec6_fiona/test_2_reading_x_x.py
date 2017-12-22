#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import fiona
c = fiona.open('/gdata/world_borders.shp', 'r')
c.closed
###############################################################################
next(c)
len(list(c))
###############################################################################
c = fiona.open('/gdata/world_borders.shp')
len(list(c))
###############################################################################
from pprint import pprint
with fiona.open('/gdata/world_borders.shp') as src:
    pprint(src[1])
###############################################################################
try:
    with fiona.open('/gdata/world_borders.shp') as c:
        print(len(list(c)))
        # assert True is False
except:
    print(c.closed)
    raise
###############################################################################
import fiona
c = fiona.open('/gdata/world_borders.shp')
c.driver
###############################################################################
c.crs
###############################################################################
from fiona.crs import to_string
print(to_string(c.crs))
###############################################################################
from fiona.crs import from_string
from_string("+datum=WGS84 +ellps=WGS84 +no_defs +proj=longlat")
###############################################################################
from fiona.crs import from_epsg
from_epsg(3857)
###############################################################################
len(c)
###############################################################################
c.bounds
