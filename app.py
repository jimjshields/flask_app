# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from config import *
# for initialization of db
from contextlib import closing

# create the app
app = Flask(__name__)
# initialize it w/ the config - from the config module
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
	"""Returns the index template."""
	return render_template('index.html')

### database operations ###

def connect_db():
	"""Connects to the configured database."""
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	"""Initializes the database with the provided schema."""
	# closing - keep connection open for duration of with block
	with closing(connect_db()) as db:
		# open_resource - flask's method for opening whatever resource you give it
		# and doing something with it (setting the context)
		with app.open_resource('schema.sql', mode='r') as f:
			# once you connect to a db, you get a connection object (here called db)
			# that can give us a cursor
			# this will execute the script found in the opened resource
			db.cursor().executescript(f.read())
		# you must explicitly tell sqlite3 to commit
		db.commit()
		print "Initialized the database."

# called before a request, passed no args
@app.before_request
def before_request():
	"""Before the db request, connects to the database."""
	# store the current db connection on the special g object
	# g is provided by flask; stores info for one request only
	# available from within each function
	g.db = connect_db()

# called after a response has been constructed
# not allowed to modify request; return value is ignored
# will handle exceptions - passed to it; otherwise, None is passed in
@app.teardown_request
def teardown_request(exception):
	"""After the db request, closes the connection,
	   and handles any exceptions."""
	# for the g object, get the 'db' attribute
	db = getattr(g, 'db', None)
	# if it exists, close the connection
	if db is not None:
		db.close()

if __name__ == '__main__':
	app.run()