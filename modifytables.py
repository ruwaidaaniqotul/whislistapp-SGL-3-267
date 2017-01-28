import sqlite3 as lite
import sys
con = lite.connect('app2.db')
cur =con.cursor()

sql ="""
UPDATE Cars
SET Price = 60000
WHERE Id =13
"""
with con:
    cur.execute(sql)
