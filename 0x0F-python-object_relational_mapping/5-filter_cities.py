#!/usr/bin/python3
"""SCRIPT TO LIST ALL CITIES WITH USER INPUTED STATE"""
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
    state_name = (argv[4], )
    cm = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id  AND states.name = %s \
            ORDER BY cities.id ASC"
    c.execute(cm, state_name)
    n = c.fetchall()
    h = [x[0] for x in n]
    a = ", ".join(h)
    print(a)

    """close all cursor and database"""
    c.close()
    db_connection.close()
