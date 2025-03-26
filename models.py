from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # db object initialized here

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.String(10), default="Normal")
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"
