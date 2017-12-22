#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os, mapnik
from gispy_helper import renderit
shpfile='/gdata/fig_data/fig_data_poly.shp'
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
line_symbolizer.stroke_width = 5.0
symbolizer = mapnik.PointSymbolizer()
m = renderit(point_sym=symbolizer, line_sym=line_symbolizer, poly_sym=polygon_symbolizer,shpfile=shpfile)
m.zoom_all()
mapnik.render_to_file(m, get_tmp_file(__file__, 'bb'))
###############################################################################
# symbolizer.stroke = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'xx_sym_file_ptt.png')
symbolizer.file = '/gdata/fig_data/turtle.png'
symbolizer.opacity = .8
m = renderit(point_sym=symbolizer, line_sym=line_symbolizer, poly_sym=polygon_symbolizer,shpfile=shpfile)
m.zoom_all()
mapnik.render_to_file(m, get_tmp_file(__file__, 'bb'))
###############################################################################
###############################################################################
stylesheet = '/gdata/world_map_shield.xml'
m = mapnik.Map(600, 300)
mapnik.load_map(m, stylesheet)
m.background = mapnik.Color('steelblue')
m.zoom_all()
mapnik.render_to_file(m, 'xx_shield_lz.png', 'png')
