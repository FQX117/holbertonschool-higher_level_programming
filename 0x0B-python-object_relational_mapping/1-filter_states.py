#!/usr/bin/python3
""" a script that lists all states with a name starting with N"""
import MySQLdb


def print_nstate():
    """comment one"""
    from sys import argv
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1], pw=argv[2], database=argv[3])

    cursor = data.cursor()

    cursor.execute("SELECT * FROM states")
    for rows in cursor.fetchall():
        if rows[1][0] == 'N':
            print(rows)

    cursor.close()
    data.close()

if __name__=="__name__":
    print_nstate()
