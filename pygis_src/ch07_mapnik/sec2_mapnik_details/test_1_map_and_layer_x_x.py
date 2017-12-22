#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
map = mapnik.Map(600, 400 )
###############################################################################
map.srs
###############################################################################
style1, style2, style3 = [mapnik.Style()] * 3
map.append_style("s1", style1)
map.append_style("s2", style2)
map.append_style("s3", style1)
map.append_style("s1", style3)
###############################################################################
layer = mapnik.Layer('lyrname')
layer.srs
###############################################################################
ds = mapnik.Shapefile(file='/gdata/world_borders.shp')
layer.datasource = ds
layer.styles.append("s1")
layer.styles.append("s2")
###############################################################################
map.layers.append(layer)
