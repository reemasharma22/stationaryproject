from app import db, Order, Stock 


db.drop_all()
db.create_all()

#adding order 

Name = Order(order_number = 231, product_id = 345, first_name ='Bill',last_name ='Smith')
db.session.add(Name)
db.session.commit()

#adding stock of product 

Pencil = Stock( product_id = '345', stock_level = 4, product_name = 'Pencil')
db.session.add(Pencil)
db.session.commit 



