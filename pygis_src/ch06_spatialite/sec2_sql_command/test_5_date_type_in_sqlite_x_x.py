#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import sqlite3 as sqlite
db = sqlite.connect(':memory:')
db.enable_load_extension(True)
db.execute('SELECT load_extension("mod_spatialite.so.7")')  # In Debian 9
cursor = db.cursor()
cursor.execute('SELECT InitSpatialMetaData();')
cursor.execute("CREATE TABLE cities (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "name CHAR(255))")
cursor.execute('CREATE TABLE some_table ( N1 SMALLINT, N2 INTEGER NOT NULL, N3 DOUBLE, STR VARCHAR(4) NOT NULL);')
cursor.execute("INSERT INTO some_table VALUES (10, 11, 111.1111, 'first');")
cursor.execute("INSERT INTO some_table VALUES (NULL, 12, NULL, 'second');")
cursor.execute("INSERT INTO some_table VALUES (30, 6, 222.2222, 'third');")
###############################################################################
cursor.execute("INSERT INTO some_table VALUES ('aaaa', 'bbbb', 'cccc', 1234)")
cursor.execute("INSERT INTO some_table VALUES ('A', 'B', 'C', 1234.6789)")
###############################################################################
cursor.execute("SELECT * FROM some_table")
for rec in cursor:
    print(rec)
###############################################################################
