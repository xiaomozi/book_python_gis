#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import os, sys, stat
import shutil
import sqlite3 as sqlite
sqlite_file = '/tmp/xx_new_db.sqlite'
if os.path.exists(sqlite_file):
    os.remove(sqlite_file)
shutil.copy("/gdata/test-2.3.sqlite", sqlite_file)
os.chmod(sqlite_file, stat.S_IRUSR + stat.S_IWUSR)
conn = sqlite.connect(sqlite_file)
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()
sql = 'create virtual table uu using virtualshape("/gdata/shape_towns", cp1252, 32632)'
cur.execute(sql)
cur.execute('PRAGMA table_info(uu)')
for rec in cur:
    print(rec)

cur.execute('SELECT PK_UID, Name, Peoples, AsText(Geometry) FROM uu LIMIT 5')
for rec in cur:
    print(rec)
###############################################################################
sql2 = '''SELECT PK_UID, Name, Peoples, AsText(Geometry)
    FROM uu WHERE Peoples > 350000 ORDER BY Name;'''
cur.execute(sql2)
for rec in cur:
    print(rec)
###############################################################################
cur.execute('DROP TABLE uu')
