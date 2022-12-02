#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
returns a query where a specified name is searched
with SQL injection avoided
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """The code is not executed when imported
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
