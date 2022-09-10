#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""
import MySQLdb
import sys


def main():
    """main function of module"""
    arg = sys.argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                           passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE\
         BINARY 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
