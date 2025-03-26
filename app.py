from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from models import db, Task  # Correct the import here!
from resources.task_resource import TaskResource

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Ensure this is after app is created and db is initialized
@app.before_request
def create_tables():
    with app.app_context():  # Ensure the app context is active before database operations
        db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()  # Fetch all tasks from the database
    return render_template('index.html', tasks=tasks)

# Setting up the Flask-RESTful API
api = Api(app)

# Registering the API resource for tasks with the corresponding routes
api.add_resource(TaskResource, '/api/tasks', '/api/tasks/<int:task_id>')

if __name__ == "__main__":
    app.run(debug=True)
