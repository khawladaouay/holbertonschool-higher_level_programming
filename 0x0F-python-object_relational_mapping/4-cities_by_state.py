#!/usr/bin/python3
"""lists all cities from database"""
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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id")
    n = c.fetchall()
    for i in n:
        print(i)
    

    """close all cursor and database"""
    c.close()
    db_connection.close()
