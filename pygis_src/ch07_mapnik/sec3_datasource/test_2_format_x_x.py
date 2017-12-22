#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
datasource = mapnik.Shapefile(file="/gdata/world_borders.shp")
###############################################################################
datasource = mapnik.Shapefile(file="/gdata/world_borders.shp", encoding="latin1")
###############################################################################
# datasource = mapnik.SQLite(file="mapData.db", table="countries", geometry_field="outline", key_field="id")
