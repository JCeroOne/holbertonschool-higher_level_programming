#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    """Connects to MySQL and prints cities of a given state."""
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

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    city_list = [city[0] for city in cities]
    print(", ".join(city_list))

    cursor.close()
    db.close()
