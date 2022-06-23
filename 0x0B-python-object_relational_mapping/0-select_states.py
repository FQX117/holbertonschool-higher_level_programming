#!/usr/bin/python3
"""lists all states"""
import MySQLdb


def list_state():
    """func to list states"""
    from sys import argv
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
    passwd=argv[2], db=argv[3])

    cursor = data.cursor()

    cursor.execute("SELECT * FROM states")
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    data.close()

if __name__=="__main__":
    print_state()
