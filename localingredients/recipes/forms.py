from flask_wtf import FlaskForm,RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
class RecipeForm(FlaskForm):
    title = StringField('Name(Give your recipe a nice name)', validators=[DataRequired()])
    Code = TextAreaField('Ingredients', validators=[DataRequired()])
    Code2 = TextAreaField('Instructions (how to make it)', validators=[DataRequired()])
    picture = FileField('Picture of Recipe (jpg/png)', validators=[FileAllowed(['jpg', 'png']),DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Post')
class CardForm(FlaskForm):
    picture = FileField('Upload Image',validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')