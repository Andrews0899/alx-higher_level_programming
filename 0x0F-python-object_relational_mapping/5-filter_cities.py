#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
 lists all cities of that state, using the database
  hbtn_0e_4_usa"""
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
    cur.execute("SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE BINARY states.name = %s\
        ORDER BY cities.id ASC;", (sys.argv[4], ))
    """Obtaining Query Results"""
    rows = cur.fetchall()
    cities_list = []
    for row in rows:
        cities_list.append(row[0])
    print(", ".join(cities_list))
