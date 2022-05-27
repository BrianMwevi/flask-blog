from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ArticleForm(FlaskForm):
    body = TextAreaField(validators=[DataRequired()])
    title = StringField('Enter title', validators=[DataRequired()])
    category = StringField('Enter pitch category', validators=[DataRequired()])
    submit = SubmitField("Post Article")
