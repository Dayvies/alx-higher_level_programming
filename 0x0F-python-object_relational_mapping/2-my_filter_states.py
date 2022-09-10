#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys


def main():
    """main function"""
    arg = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    statement = "SELECT * FROM states WHERE name like BINARY\
        '{}' ORDER BY id ASC".format(
        arg[4])
    cur.execute(statement)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
