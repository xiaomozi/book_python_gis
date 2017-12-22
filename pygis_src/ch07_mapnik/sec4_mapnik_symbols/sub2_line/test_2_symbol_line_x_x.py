#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os, mapnik
from gispy_helper import renderit
###############################################################################
line_symbolizer = mapnik.LineSymbolizer()
m = renderit(line_sym = line_symbolizer)
mapnik.render_to_file(m, 'out.png')
###############################################################################
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 15.0
# line_symbolizer.line_cap = mapnik.line_cap.BUTT_CAP
# line_symbolizer.line_cap = mapnik.line_cap.ROUND_CAP
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
m = renderit(line_sym = line_symbolizer)
mapnik.render_to_file(m, 'out.png')
###############################################################################
line_symbolizer.stroke_opacity = 0.8
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.SQUARE_CAP
m = renderit(line_sym = line_symbolizer)
mapnik.render_to_file(m, 'out2.pdf')
###############################################################################
from gispy_helper import mapnik_lyr
m = mapnik.Map(600, 300, "+proj=latlong +datum=WGS84")
line_data = '/gdata/fig_data/fig_data_line.shp'
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
# line_symbolizer.stroke = mapnik.Color("#ffd3a9")
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
line_symbolizer.stroke_width = 15.0
ly1 = mapnik_lyr(m, data=line_data, line_sym=line_symbolizer)
line_symbolizer2 = mapnik.LineSymbolizer()
# line_symbolizer2.stroke = mapnik.Color('rgb(50%,80%,80%)')
line_symbolizer2.stroke = mapnik.Color("#ffd3a9")
line_symbolizer2.stroke_opacity = 0.8
line_symbolizer2.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
line_symbolizer2.stroke_width = 4.0
ly2 = mapnik_lyr(m, data=line_data, line_sym=line_symbolizer2)
m.layers.append(ly1)
m.layers.append(ly2)
m.zoom_all()
mapnik.render_to_file(m, 'out.png')
###############################################################################
line_symbolizer2 = mapnik.LinePatternSymbolizer()
line_symbolizer2.file = '/gdata/fig_data/turtle.png'
# line_symbolizer2.stroke = mapnik.Color('rgb(50%,50%,50%)')
# line_symbolizer2.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
# line_symbolizer2.stroke_width = 1
# line_symbolizer = mapnik.LineSymbolizer()
m = renderit(line_sym = line_symbolizer2)
mapnik.render_to_file(m, 'out.png')
###############################################################################
