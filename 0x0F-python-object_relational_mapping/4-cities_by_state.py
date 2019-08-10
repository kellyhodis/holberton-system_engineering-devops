#!/usr/bin/python3
""" This is a module containing a script that lists
all cities from the database hbtn_0e_4_usa."""

import sys
import MySQLdb


def list_all(mysql_username="", mysql_password="", database_name=""):
    ''' This is a function that lists all states from a database. '''
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM cities ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_all(username, password, database)
