#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """this code is executable when not imported
    """
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
