#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


def main():
    """main function of module"""
    arg = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s  ORDER BY id ASC", (arg[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
