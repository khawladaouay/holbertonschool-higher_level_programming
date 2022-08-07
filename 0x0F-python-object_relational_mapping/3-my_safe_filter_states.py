#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states where name matches the arg"""
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
    c.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]))
    n = c.fetchall()
    for i in n:
        print(i)
    

    """close all cursor and database"""
    c.close()
    db_connection.close()
