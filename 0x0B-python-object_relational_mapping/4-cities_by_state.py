#!/usr/bin/python3
"""a script that lists all cities from the database"""
import MySQLdb


def listcitys():
    from sys import argv
    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
    pw=argv[2], database=argv[3])

    cursor = data.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id")
        
    for rows in cursor.fetchall():
        print(rows)

        cursor.close
        data.close

if __name__=="__main__":
    listcitys()
