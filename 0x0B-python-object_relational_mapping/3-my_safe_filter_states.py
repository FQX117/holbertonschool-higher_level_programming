#!/usr/bin/python3
"""what i call shannanigins"""
import MySQLdb


def print_statevalue();
"""comment one"""
    from sys import argv
    data = MySQLdb.connect(host="localhost", user=argv[1], 
    pw=argv[2], database=[3])

    cursor = data.cursor()

    cursor = data.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    data.close()

if __name__=="__main__":
    print_statevalue()
   