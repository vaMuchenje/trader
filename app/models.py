from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	full_name = db.Column(db.String(120))
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	date_joined = db.Column(db.DateTime, index=True, default=datetime.utcnow)


	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class Strategy(db.Model):
	strategy_id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
	common_name = db.Column(db.String(64), index=True, unique=True)
	description = db.Column(db.String(255))
	transaction = db.relationship('Transaction', backref='publisher', lazy='dynamic')

	def __repr__(self):
		return '<Strategy {}>'.format(self.common_name)

class Transaction(db.Model):
	transaction_id = db.Column(db.Integer, primary_key=True)
	security_id =db.Column(db.String(64), index=True)
	quantity = db.Column(db.Float)
	side = db.Column(db.String(64), index=True)
	limit=db.Column(db.Integer)                   
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	strategy_id = db.Column(db.Integer, db.ForeignKey('strategy.strategy_id'))

	def __repr__(self):
		return '<Transaction {}>'.format(self.transaction_id)

class Subscription(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	strategy_id = db.Column(db.String(120), index=True)
	username = db.Column(db.String(120), index=True)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		return '<Subscription User:{} , Strategy:{}>'.format(self.username, self.strategy_id)
