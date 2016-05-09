#!/usr/bin/python
import MySQLdb
import json

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class CreateUser(Resource):
    def get(self):
        return {'status': 'success'}

api.add_resource(CreateUser, '/CreateUser')

def get_article():
	db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
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
	for row in cur.fetchall():
		jdata = {}
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
    return get_article()


if __name__ == "__main__":
    app.run()