#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
import os
import mapnik
m = mapnik.Map(1000, 800, '+init=epsg:4326')
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)
line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.1
r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style', s)
lyr = mapnik.Layer('world', "+proj=latlong +datum=WGS84")
lyr.datasource = mapnik.Shapefile(file='/gdata/world_borders.shp')
lyr.styles.append('My Style')
m.layers.append(lyr)
m.zoom_to_box(lyr.envelope())
mapnik.render_to_file(m, 'xx_b.png', 'png')
