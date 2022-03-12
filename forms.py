"""
Forms
"""
from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    Login form
    """

    username = fields.StringField(
        'Nombre del usuario', validators=[DataRequired()]
    )
    password = fields.PasswordField('Password', validators=[DataRequired()])
    submit = fields.SubmitField('Enviar')
