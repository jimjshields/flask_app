# configuration - class/inheritance pattern - imported into app.py
# pattern from http://flask.pocoo.org/docs/0.10/config/ 

class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE = '/db/imdb_top_250.db'
	SECRET_KEY = 'development key'
	USERNAME = 'admin'
	PASSWORD = 'default'

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True