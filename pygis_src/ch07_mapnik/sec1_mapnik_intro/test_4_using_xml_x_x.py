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
