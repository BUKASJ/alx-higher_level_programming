#!/usr/bin/python3

""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb


def main():

    mysql_username = input("Enter MySQL username: ")
    mysql_password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")

    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
        )

        cur = conn.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")

        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:

        if cur:
            cur.close()
            if conn:
                conn.close()


if __name__ == "__main__":
    main()
