from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
class RecipeForm(FlaskForm):
    title = StringField('Name', validators=[DataRequired()])
    Code = TextAreaField('Code', validators=[DataRequired()])
    picture = FileField('Update Store Profile Picture(jpg/png)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Post')
class CardForm(FlaskForm):
    picture = FileField('Upload Image',validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')