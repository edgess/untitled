#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

#db = MySQLdb.connect("192.168.10.183","edge","1234","edge" )
db = MySQLdb.connect("192.168.10.30","log","1234","bak_log" )
with db:
	cur = db.cursor()
	cur.execute("SELECT * FROM log")
	data = cur.fetchall()
for i in data:
	print i
#cur.execute("insert into test values('789','edge')")
#cur.close()
#db.commit()

#print "insert success " 
