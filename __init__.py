app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://reema:tempDB47!@35.246.8.157/reema"

from flask import flask 

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)