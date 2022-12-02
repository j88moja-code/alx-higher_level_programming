#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """The code is not executed when imported
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY states.id ASC")

    query_result = c.fetchall()
    if query_result:
        for row in query_result:
            if row[1][0] == 'N':
                print(row)
    c.close()
    db.close()
