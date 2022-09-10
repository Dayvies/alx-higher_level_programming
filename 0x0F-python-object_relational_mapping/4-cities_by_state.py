#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def main():
    """The main function"""
    arg = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT f.id, f.name, a.name FROM cities AS f INNER\
        JOIN states AS a ON (f.state_id=a.id) ORDER BY f.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
