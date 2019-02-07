from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, DecimalField, BooleanField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class EnterMatrixForm(FlaskForm):
    #rows = IntegerField('Rows', validators=[DataRequired(),NumberRange(min=0)])
    #cols = IntegerField('Columns', validators=[DataRequired(),NumberRange(min=0)])
    entry = TextAreaField('Matrix', validators=[DataRequired()])
    detailed_solution = BooleanField('Detailed')
    #dropdown? for different options .. interesting indeed
    submit = SubmitField('Create a Matrix')
    