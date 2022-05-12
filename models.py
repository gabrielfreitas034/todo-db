from database import db

class Todos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  complete = db.Column(db.Boolean)
  category = db.Column(db.String(50))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  password = db.Column(db.String())
  role = db.Column(db.String())