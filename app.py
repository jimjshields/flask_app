# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from config import *

# create the app
app = Flask(__name__)
# initialize it w/ the config - from the config module
app.config.from_object(DevelopmentConfig)

@app.route('/')
def hello_world():
	return render_template('index.html')

# for connecting to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run()