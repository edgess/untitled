#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
try:
	#db = MySQLdb.connect("192.168.10.183","edge","1234","edge" )
	db = MySQLdb.connect("192.168.10.30","log","1234","bak_log" )
	cur = db.cursor()
	cur.execute("SELECT * FROM log")
	data = cur.fetchall()
finally:
	if db:
		db.close()
for i in data:
	print i
#cur.execute("insert into test values('789','edge')")
#cur.close()
#db.commit()

#print "insert success " 
