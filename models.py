from stationaryproject import db 


class Order(db.Model):
    order_number = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('stock.product_id'))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    postcode = db.Column (db.Integer, nullable=False)

class Stock (db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    stock_level = db.Column(db.Integer)
    product_name = db.relationship ("Order", backref = "product") #there is a relationship between the product id and product name?