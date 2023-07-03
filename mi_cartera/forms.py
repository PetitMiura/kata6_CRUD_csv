from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm):
    date = DateField("Fecha", validators=[DataRequired("La fecha es obligatoria")])
    abstract = StringField("Concepto", validators=[DataRequired("Conceptos obligatorios"), Length(min=4)])
    amount = FloatField("Cantidad",validators=[DataRequired("Cantidad obligatoria")])
    currency = SelectField("Moneda",validators=[DataRequired("Moneda obligatoria")], choices=[("EUR", "Euros"), ("USD", "Dólares americanos")])

    submit = SubmitField("Enviar")
    