#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
db = sqlite.connect('xx_shapedb.sqlite')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')
cursor = db.cursor()
###############################################################################
import shapely.wkt
LONDON = 'POINT(-0.1263 51.4980)'
pt = shapely.wkt.loads(LONDON)
cursor.execute("SELECT id,level,AsText(geom) " +
     "FROM gshhs WHERE id IN " +
     "(SELECT pkid FROM idx_gshhs_geom" +
     " WHERE xmin <= ? AND ? <= xmax" +
     " AND ymin <= ? and ? <= ymax) " +
     "AND Contains(geom, GeomFromText(?, 4326))",
     (pt.x, pt.x, pt.y, pt.y, LONDON))
shoreline = None
for id,level,wkt in cursor:
    # if level == 1:
    shoreline = wkt
###############################################################################
with open("xx_uk-shoreline.wkt", "w") as fout:
    if shoreline:
        fout.write(shoreline)
###############################################################################
cursor.execute("EXPLAIN QUERY PLAN " +
    "SELECT id,level,AsText(geom) " +
    "FROM gshhs WHERE id IN " +
    "(SELECT pkid FROM idx_gshhs_geom" +
    " WHERE xmin <= ? AND ? <= xmax" +
    " AND ymin <= ? and ? <= ymax) " +
    "AND Contains(geom, GeomFromText(?, 4326))",
    (pt.x, pt.x, pt.y, pt.y, LONDON))
###############################################################################
for row in cursor:
    print (row)

