from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField(label='Author', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField(label='Create')


class DeleteBookForm(FlaskForm):
    submit = SubmitField(label='Delete')


class UpdateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = StringField(label='Author', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField(label='Update')

