#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
ds = mapnik.Shapefile(file='/gdata/GSHHS_c.shp')
ds.envelope()
###############################################################################
import os
stylesheet = '/gdata/world_map.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
m.background = mapnik.Color('steelblue')
print(m.scale())
mapnik.render_to_file(m, 'xx1.png', 'png')
chinabox = mapnik.Box2d(73, 0, 135, 54)
m.zoom_to_box(chinabox)
print(m.scale())
mapnik.render_to_file(m, 'xx2.png', 'png')
for x in m.layers:
    print(x.name)
    print(x.envelope())
