#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None
f = None

try:
     
    con = psycopg2.connect(database='testdb_01', user='jinhyukb') 
    
    cur = con.cursor()
    cur.execute( 'DELETE FROM Cars' )


    f = open('cars', 'r')
    cur.copy_from(f, 'cars', sep="|")                    
    con.commit()
   
except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)

except IOError, e:    

    if con:
        con.rollback()

    print 'Error %s' % e   
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

    if f:
        f.close()  
