from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    HiddenField,
    RadioField,
    StringField,
    SubmitField,
)
from wtforms.validators import data_required, number_range


class Movimientoform(FlaskForm):
    id = HiddenField()
    fecha = DateField('Fecha', validators=[
        data_required('Debes indicar la fecha del movimiento')
    ])
    concepto = StringField('Concepto', validators=[
        data_required('No has especificado un concepto para este movimiento')
    ])
    tipo = RadioField(choices=[('I', 'Ingreso'), ('G', 'Gasto')], validators=[
        data_required('Necesito saber si es un gasto o un ingreso')
    ])
    cantidad = DecimalField('Cantidad', places=2, validators=[
        data_required(
            'No puede haber un movimiento sin una cantidad asociada'),
        number_range(
            min=0.1, message='No se permiten cantidades inferiores a 10 centimos')
    ])

    submit = SubmitField('Guardar')
