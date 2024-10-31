from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Go to /todo to access the todo list app!"

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect(url_for('todo'))
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
