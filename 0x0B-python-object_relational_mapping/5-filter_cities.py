#!/usr/bin/python3
"""a script that takes in the name of a state as an
argument and lists all cities of that state"""

import MySQLdb


def listcitys():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
        = states.id WHERE states.name LIKE %s ORDER BY cities.id", (argv[4],))
    print(", ".join(rows[0] for rows in cur.fetchall()))

    cur.close()
    db.close()


if __name__ == "__main__":
    listcitys()
