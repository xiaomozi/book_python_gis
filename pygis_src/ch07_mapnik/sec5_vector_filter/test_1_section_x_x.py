#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
###############################################################################
###############################################################################
import os
import mapnik
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer2 = mapnik.PolygonSymbolizer()
polygon_symbolizer3 = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
polygon_symbolizer2.fill = mapnik.Color('#ff0000')
m = mapnik.Map(600, 200, "+proj=latlong +datum=WGS84")
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
r2 = mapnik.Rule()
r.symbols.append(polygon_symbolizer)
r2.symbols.append(polygon_symbolizer2)
r.filter = mapnik.Expression("[id] = 1")
r2.filter = mapnik.Expression("[id] = 2")
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_linecap = mapnik.stroke_linecap.ROUND_CAP
line_symbolizer.stroke_width = 5.0
r.symbols.append(line_symbolizer)
r2.symbols.append(line_symbolizer)
s.rules.append(r)
s.rules.append(r2)
m.append_style('My Style', s)
lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='/gdata/fig_data/fig_data_poly.shp')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.zoom_all()
mapnik.render_to_file(m, 'xx_mapnik_filter.png', 'png')
###############################################################################

###############################################################################

###############################################################################
###############################################################################
r3 = mapnik.Rule()
r3.set_else(True)
r3.symbols.append(line_symbolizer)
s.rules.append(r3)
m.append_style('My Style2', s)
lyr.styles.append('My Style2')
m.layers.append(lyr)
mapnik.render_to_file(m, 'xx_mapnik_filter.png', 'png')
###############################################################################
###############################################################################
###############################################################################
