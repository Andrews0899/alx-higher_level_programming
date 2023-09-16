#!/usr/bin/python3
"""Script that takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches the
  argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """In order to put our new connnection to good use we
     need to create a cursor object"""
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT * FROM states\
        WHERE BINARY name = '{}'\
            ORDER BY id ASC".format(sys.argv[4]))
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
