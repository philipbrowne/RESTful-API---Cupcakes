from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class NewCupcakeForm(FlaskForm):
    """Form for New Cupcake"""
    flavor = StringField('Flavor', validators=[
                         InputRequired(message='Must include a Flavor')])
    size = SelectField('Size', choices=[('extra small', 'Extra Small'), ('small', 'Small'), ('medium', 'Medium'), (
        'large', 'Large'), ('extra large', 'Extra Large')], validators=[InputRequired(message='Must include a cupcake size')])
    rating = FloatField('Rating', validators=[
                        InputRequired(message='Must include rating')])
    image = StringField('Image URL', validators=[URL(
        message='Must be a valid URL'), Optional()])
