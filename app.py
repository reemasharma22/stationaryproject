from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to the Stationary Shop!'

@app.route('/about')
def about():
    return 'About us!'

if __name__ == "__main__":
    app.run(debug=True)

#creatingthetables


class Order(db.Model):
    order_number = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), db.ForeignKey('product_name'))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Stock (db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    stock_level = db.Column((db.Integer)
    price = db.Column((db.Integer)
