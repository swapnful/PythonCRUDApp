from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Task  # Ensure models.py is correctly set up
from forms import TaskForm  # Ensure forms.py is correctly set up

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'admin'  # Replace with a strong secret key
db.init_app(app)

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            completed=form.completed.data,
            user_id=1  # Hardcoded for now; replace with dynamic user ID handling
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('manage_tasks'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', form=form, tasks=tasks)

@app.route('/tasks/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('manage_tasks'))

# Other routes like index, home, etc.

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
