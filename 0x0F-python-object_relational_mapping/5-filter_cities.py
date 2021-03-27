#!/usr/bin/python3
"""
This module all cities of that state
"""

import MySQLdb
import sys


if __name__ == "__main__":
    usr = sys.argv[1]
    passw = sys.argv[2]
    dtb = sys.argv[3]
    st = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=p, db=dtb)

    cur = db.cursor()

    cur.execute("SELECT name " +
                "FROM cities WHERE state_id IN " +
                "(SELECT id FROM states " +
                "WHERE name='{}')".format(st))

    rows = cur.fetchall()
    sep = ""
    for row in rows:
        print("{}{}".format(sep, row[0]), end="")
        sep = ", "
    print()

    cur.close()
    db.close()
