from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from models import db, Task  
from resources.task_resource import TaskResource

app = Flask(__name__)

# ((configuring the SQLite database))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  # ((SQLite database))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ((initialize the database with the app))
db.init_app(app)

# ((this is after app is created and db is initialized))
@app.before_request
def create_tables():
    with app.app_context():  
        db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()  
    return render_template('index.html', tasks=tasks)

# ((setting up the Flask-RESTful API))
api = Api(app)

# (registering the API resource for tasks with the corresponding routes)
api.add_resource(TaskResource, '/api/tasks', '/api/tasks/<int:task_id>')

if __name__ == "__main__":
    app.run(debug=True)
