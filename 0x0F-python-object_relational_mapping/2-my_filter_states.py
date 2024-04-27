#!/usr/bin/python3

"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb


if __name__ = "__main__":
    db = Mysqldb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[],
            port=3306
            )
    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                 ORDER BY id ASC", (sys.argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
