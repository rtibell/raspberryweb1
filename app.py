#!/usr/bin/python
import MySQLdb
import json

from flask import Flask
app = Flask(__name__)

def get_article():
	db = MySQLdb.connect(host="192.168.10.22",    # your host, usually localhost
                     user="rasse",         # your username
                     passwd="mysql",  # your password
                     db="rasse")        # name of the data base

	# you must create a Cursor object. It will let
	#  you execute all the queries you need
	cur = db.cursor()

	# Use all the SQL you like
	cur.execute("SELECT * FROM product")

	# print all the first cell of all the rows
	jlist = []
	jdata = {}
	for row in cur.fetchall():
		jdata[row[0]] = row[1]
		jlist.append(jdata)

	db.close()
	return json.dumps(jlist)

def get_json():
	jlist = []
	jdata = {}
	jdata['a'] = 'b'
	jlist.append(jdata)
	return json.dumps(jlist)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return get_article()


if __name__ == "__main__":
    app.run()