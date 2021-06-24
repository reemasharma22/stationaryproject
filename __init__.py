app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://reema:Password1234@35.197.222.73/projectdb"

from flask import flask 

db = SQLAlchemy(app)

def create_app():
    app = Flask(__name__)