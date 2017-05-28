#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='testdb_01', user='jinhyukb') 
    
    cur = con.cursor() 

    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id serial PRIMARY KEY, Name VARCHAR(10))")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    
	#We create a Friends table and try to fill it with data. However, as we will see, the data will be not committed
    #con.commit()
       
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
        
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()

