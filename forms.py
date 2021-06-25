from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    order_number = IntegerField('Order Nymber')
    product_id = IntegerField('Product ID')
    street = StringField('Enter your address')
    city = StringField('Enter City')
    postcode = StringField('Enter Postcode')
    products = SelectField('Products', choices= [( 1,'Pencil'),( 2 ,'ruler'),( 3 ,'biro'), (4 , 'rubber'),( 5 ,'sharpner')], validators=[DataRequired()]
    submit = SubmitField('Submit')

class StockForm(Flaskform):
    product_id = IntegerField('Product ID')
    stock_level = IntegerField('Stock Level')
    product_name = StringField('Product Name')
