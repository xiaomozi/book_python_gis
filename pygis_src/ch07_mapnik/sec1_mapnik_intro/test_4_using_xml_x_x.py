#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
stylesheet = '/gdata/world_style.xml'
image = 'xworld2.png'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
mapnik.render_to_file(m,'xworld2.png', 'png')
m.zoom_all()
mapnik.render_to_file(m, image)
print("rendered image to '%s'" % image)
###############################################################################
###############################################################################
import mapnik
mapfile = "/gdata/world_population.xml"
m = mapnik.Map(1400, 600)
mapnik.load_map(m, mapfile)
bbox = mapnik.Envelope(mapnik.Coord(-180.0, -75.0), mapnik.Coord(180.0, 90.0))
m.zoom_to_box(bbox)
mapnik.render_to_file(m, 'world_population.png', 'png')
###############################################################################
###############################################################################
