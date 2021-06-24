from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from os import getenv

app = Flask(__name__)

#configs 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Password1234@35.197.222.73:3306/reema"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)


app.config ['SECRET KEY'] = getenv ('SKEY')

#direct to main page and about us 

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to the Stationary Shop!'

@app.route('/about')
def about():
    return 'About us!'

if __name__ == "__main__":
    app.run(debug=True)
    
    
  
