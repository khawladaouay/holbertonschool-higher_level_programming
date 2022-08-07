#!/usr/bin/python3
"""a script that lists all states with a name sarting with N"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """make a connectin"""
    db_connection = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user=argv[1],
                                    password=argv[2],
                                    database=argv[3])

    """create a cursor"""
    c = db_connection.cursor()

    """execute query"""
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    i = c.fetchall()
    for j in i:
        print(j)

    """close all cursor and database"""
    c.close()
    db_connection.close()
