#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
symbolizer = mapnik.PolygonSymbolizer()
###############################################################################
symbolizer.fill = mapnik.Color("red")
###############################################################################
symbolizer.fill_opacity = 0.5
###############################################################################
symbolizer.gamma = 0.63
###############################################################################
import os
import mapnik
from gispy_helper import renderit
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
line_symbolizer.stroke_width = 5.0
###############################################################################
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
shpfile = '/gdata/fig_data/fig_data_poly.shp'
m = renderit(line_sym=line_symbolizer, poly_sym=polygon_symbolizer, shpfile = shpfile)
mapnik.render_to_file(m, 'out.png')
###############################################################################
polygon_symbolizer.fill = mapnik.Color('#ff0000')
m = renderit(line_sym=line_symbolizer, poly_sym=polygon_symbolizer,shpfile = shpfile)
mapnik.render_to_file(m, 'out.png')
###############################################################################
sym_img = '/gdata/fig_data/turtle.png'
polygon2_symbolizer = mapnik.PolygonPatternSymbolizer()
polygon2_symbolizer.file = sym_img
polygon2_symbolizer.fill = True
polygon2_symbolizer.stroke_file = sym_img
polygon2_symbolizer.stroke_fill = sym_img
m = renderit(line_sym=line_symbolizer, poly_sym=polygon2_symbolizer,shpfile = shpfile)
mapnik.render_to_file(m, 'out.png')
###############################################################################
import os
import mapnik
stylesheet = '/gdata/world_map_poly.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.zoom_all()
# m.background = mapnik.Color('steelblue')
# bbox = mapnik.Box2d(118, 36.6, 124.6, 40.7)
bbox = mapnik.Box2d(70, 20, 135, 57)
m.zoom_to_box(bbox)
mapnik.render_to_file(m,'xx_map_poly.png', 'png')
