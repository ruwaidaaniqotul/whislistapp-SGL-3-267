import sqlite3 as lite
import sys
Cars = (
    (9,'Suzuki',52642),
    (10,'Honda',57127),
    (11,'Nissan',9000),
    (12,'Hyundai',29000),
    (13,'Jialing',350000),
)
con = lite.connect('app2.db')
with con:
    cur = con.cursor()
    cur.executemany("INSERT INTO Cars VALUES(?,?,?)",Cars)
