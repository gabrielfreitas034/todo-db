import os
from flask import Flask
from database import db
from controllers import TodoController, UserController

###### CONFIGURACOES ######
app = Flask('app')
app.config['SECRET_KEY'] = 'qEChL7R3SpF72cEA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

###### ROTAS ######
@app.route('/')
def index():
  return TodoController.index()

@app.route('/create', methods=['POST'])
def create():
  return TodoController.create()

@app.route('/delete/<int:id>')
def delete(id):
  return TodoController.delete(id)

@app.route('/complete/<int:id>')
def complete(id):
  return TodoController.complete(id)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  return TodoController.update(id)

@app.route('/login')
def login():
  return UserController.login()

@app.route('/register')
def register():
  return UserController.register()

@app.route('/signup', methods=['POST'])
def signup():
  return UserController.signup()

@app.route('/signin', methods=['POST'])
def signin():
  return UserController.signin()

@app.route('/logout')
def logout():
  return UserController.logout()

###### INICIALIZACAO ######
with app.app_context():
  db.create_all()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
