from app import db, Orders, Stock 


db.drop_all()
db.create_all()

testorders = Orders(first_name='Bill',last_name='Smith')
db.session.add(testorders)
db.session.commit()