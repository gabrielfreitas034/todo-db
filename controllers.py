from flask import render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from models import Todos, Users, db

class TodoController():
  def index():
    if 'user_id' not in session:
      flash('Usuário não logado', 'error')
      return redirect('/login')
    
    todos = Todos.query.filter_by(
      user_id=session['user_id']
    ).all()
    return render_template(
      'index.html',
      todos=todos
    )

  def create():
    title = request.form.get('title')
    cat = request.form.get('category')
  
    if len(title) > 10:
      flash('Título menor 10 caracteres', 'error')
      return redirect('/')
    
    new_todo = Todos(
      title=title,
      category=cat,
      complete=False,
      user_id=session['user_id']
    )
    db.session.add(new_todo)
    db.session.commit()
  
    flash('TODO criado com sucesso', 'success')
    return redirect('/')

  def delete(id):
    todo = Todos.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
  
    flash('TODO deletado com sucesso', 'success')
    return redirect('/')

  def complete(id):
    todo = Todos.query.filter_by(id=id).first()
    todo.complete = True
    db.session.commit()
  
    flash('TODO completado com sucesso', 'success')
    return redirect('/')

  def update(id):
    title = request.form.get('title')
  
    if len(title) > 10:
      flash('Título menor 10 caracteres', 'error')
      return redirect('/')
  
    todo = Todos.query.filter_by(id=id).first()
    todo.title = title
    db.session.commit()
  
    flash('TODO editado com sucesso', 'success')
    return redirect('/')

class UserController():
  def login():
    return render_template('login.html')

  def register():
    return render_template('register.html')

  def signup():
    name_input = request.form.get('name')
    email_input = request.form.get('email')
    password_input = request.form.get('password')
  
    # Verificar se já existe o email no bd
    user = Users.query.filter_by(
      email=email_input
    ).first()
    if user:
      flash('Este e-mail já existe', 'error')
      return redirect('/register')
  
    new_user = Users(
      name=name_input,
      email=email_input,
      password=generate_password_hash(password_input)
    )
    db.session.add(new_user)
    db.session.commit()
  
    flash('Usuário criado com sucesso', 'success')
    return redirect('/login')

  def signin():
    email_input = request.form.get('email')
    password_input = request.form.get('password')
  
    # Verificar se existe um usuário com o email
    user = Users.query.filter_by(
      email=email_input
    ).first()
    if not user:
      flash('E-mail não encontrado', 'error')
      return redirect('/login')
  
    # Verificar se senha está correta
    if not check_password_hash(
      user.password,
      password_input
    ):
      flash('Senha incorreta', 'error')
      return redirect('/login')
  
    # Guardar usuário na sessão
    session['user_id'] = user.id
  
    flash(f'Olá, {user.name}', 'info')
    return redirect('/')

  def logout():
    session.pop('user_id', None)
    return redirect('/login')