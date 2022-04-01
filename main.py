from flask import Flask, render_template, request, redirect
app = Flask('app')

todos = [
  { 
    'title': 'Estudar Python',
    'complete': False
  },
  { 
    'title': 'Estudar JavaScript',
    'complete': True
  }
]

@app.route('/')
def index():
  return render_template(
    'index.html',
    todos=todos
  )

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  cat = request.form.get('category')
  todos.append({
    'title': title,
    'complete': False,
    'category': cat
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  todos.pop(index)
  return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
  todos[index]['complete'] = True
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  title = request.form.get('title')
  todos[index]['title'] = title
  return redirect('/')

# IMPORTANTE V
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)