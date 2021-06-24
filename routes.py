from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from os import getenv


#add

@app.route('/add', methods=['POST', 'GET'])
def add():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        street = form.street.data
        city = form.city.data
        postcode = form.city.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return 'Thank you' + first_name + last_name + "for shopping with us! Your item will be delivered to" + street + city + postcode

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')


#update 

@app.route('/update', methods=['GET', 'PULL'])
def update():
    error = ""
    form = BasicForm()
    
