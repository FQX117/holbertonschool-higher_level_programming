#!/usr/bin/python3
"""a script that takes in an argument and displays 
all values in the states table of hbtn_0e_0_usa"""

import MySQLdb


def print_statevalue():
    from sys import argh
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            pw=argv[2], database=argv[3])

    cursor = data.cursor()

    cursor.execute("SELECT * FROM states WHERE name\LIKE binary %s",
    [format(argv[4])])
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    data.close()


if __name__=="__name__":
    print_statevalue()
