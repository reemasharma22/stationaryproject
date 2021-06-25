from flask import Flask, render_template, request
from flask_wtf import Flaskform
from wtforms import StringField, SubmitField, IntegerField
from stationaryproject.models import Order, Stock
from stationaryproject.forms import BasicForm, StockForm


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
    


#add

@app.route('/add', methods=['POST', 'GET'])
def add():
    error = ""
    form = BasicForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        street = form.street.data
        city = form.city.data
        postcode = form.city.data

        order = Order (first_name = first_name, last_name = last_name, product_id = 1)

        db.session.add(Order)
        db.session.commit()
    
    return render.template('add.html',form=form)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')



#update 

@app.route('/update', methods=['GET', 'PULL'])
def update():
    form = BasicForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        street = form.street.data 
        city = form.city.data
        postcode = form.postcode.data

        order = Order (first_name = first_name, last_name = last_name, product_id = 1)
        db.session.update(Order)
        db.session.commit()
    return render_template('update.html', form=form)

#delete

@app.route('/delete', methods=['DELETE', 'GET'])
def delete():
    form = BasicForm()
    if form.validate_on_submit():
         first_name = form.first_name.data
         last_name = form.last_name.data
         street = form.street.data
         city = form.city.data
         postcode = form.city.data

    order = Order (first_name = first_name, last_name = last_name, product_id = 1)
    db.session.update(Order)
    db.session.commit()
    return redirect(url_for('/home'))
    return render_template('delete.html', form=form)
