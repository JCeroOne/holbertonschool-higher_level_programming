#!/usr/bin/python3
"""Lists all states matching a given name from the database."""

import MySQLdb
import sys


if __name__ == "__main__":
    """Connects to MySQL and prints matching states."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
