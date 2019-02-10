import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'fdajl12342332afwew35'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'bitadel.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
