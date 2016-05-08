#!/usr/bin/python
import MySQLdb

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="rasse",         # your username
                     passwd="mysql",  # your password
                     db="rasse")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM product")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]
    print row[1]

db.close()

