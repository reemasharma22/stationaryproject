class Order(db.Model):
    order_number = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('stock.product_id'))
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Stock (db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    stock_level = db.Column(db.Integer)
    product_name = db.Column(db.String(30))