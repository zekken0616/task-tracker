from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:  # Only add if not empty
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)