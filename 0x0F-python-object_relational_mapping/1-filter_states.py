#!/usr/bin/python3
""" This is a script that lists all states with a name starting with N
from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def list_all_n(mysql_username="", mysql_password="", database_name=""):
    ''' This is a script that lists all states with a name starting with N.'''
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_all_n(username, password, database)
