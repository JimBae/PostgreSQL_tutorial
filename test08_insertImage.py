
#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


def readImage():

    try:
        fin = open("Ship_1490.tif", "rb")
        img = fin.read()
        return img
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        
        if fin:
            fin.close()


try:


    con = psycopg2.connect(database="testdb_01", user="jinhyukb") 
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Images")
    cur.execute("CREATE TABLE Images(Id INT PRIMARY KEY, Data BYTEA)")

    data = readImage()
    binary = psycopg2.Binary(data)
    cur.execute("INSERT INTO Images(Id, Data) VALUES (1, %s)", (binary,) )

    con.commit()    
    
except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e    
    sys.exit(1)
    
finally:
    
    if con:
        con.close()   
