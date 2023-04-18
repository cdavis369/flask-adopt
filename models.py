from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  """ Connect to databse """
  db.app = app
  db.init_app(app)
  
class Pet(db.Model):
  """ Pet """
  __tablename__ = "pets"
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(length=50), nullable=False)
  species = db.Column(db.String(length=50), nullable=False)
  photo = db.Column(db.Text, nullable=True)
  age = db.Column(db.Integer, nullable=True)
  notes = db.Column(db.Text, nullable=True)
  available = db.Column(db.Boolean, nullable=False, default=True)