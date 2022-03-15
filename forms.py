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


class TodoForm(FlaskForm):
    description = fields.StringField('Description', validators=[DataRequired()])
    submit = fields.SubmitField('Create')


class DeleteForm(FlaskForm):
    submit = fields.SubmitField('Delete')


class UpdateForm(FlaskForm):
    submit = fields.SubmitField('Update')
