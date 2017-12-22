#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
conn = sqlite.connect('/tmp/xx_new_db.sqlite')
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')  # In Debian 9
cur = conn.cursor()
recs = cur.execute("SELECT name, AsText(geom) FROM MyTable;")
for rec in recs:
    print(rec)
###############################################################################
###############################################################################
import sqlite3 as db
conn = db.connect('/tmp/xx_new_db.sqlite')
cur = conn.cursor()
###############################################################################
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
# res.next()
###############################################################################
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
# res.next()
conn.rollback()
res = cur.execute(sql)
# res.next()
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
res = cur.execute(sql)
# res.next()
conn.commit()
res = cur.execute(sql)
# res.next()
