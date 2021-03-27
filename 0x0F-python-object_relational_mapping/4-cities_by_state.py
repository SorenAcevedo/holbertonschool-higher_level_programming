#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=u, passwd=p, db=d)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name " +
                "FROM states INNER JOIN cities " +
                "ON states.id=state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
