from app import db, Order, Stock 


db.drop_all()
db.create_all()

Name = Order(first_name ='Bill',last_name ='Smith')
db.session.add(Name)
db.session.commit()

Pencil = Stock( product_id = '345')
db.session.add(Pencil)
db.session.commit 



