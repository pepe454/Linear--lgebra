from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, DecimalField, BooleanField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange, ValidationError

"""
class CreateMatrixForm(FlaskForm):
    rows = IntegerField('Rows', validators=[DataRequired(),NumberRange(min=0)])
    cols = IntegerField('Columns', validators=[DataRequired(),NumberRange(min=0)])
    submit = SubmitField('Create empty Matrix')

class MatrixEntry(FlaskForm):
    entry = DecimalField('Entries', validators=[DataRequired(),NumberRange(min=0)])

class MatrixListField(FieldList):
    def __init__(self, cols=1):
        super(MatrixListField, self).__init__(FormField(MatrixEntry), min_entries=cols)

class MatrixField(FieldList):
    def __init__(self, rows=1, cols=1):
        super(MatrixField, self).__init__(FormField(MatrixListField(cols), min_entries=rows))
        
class NewMatrixForm(FlaskForm):
    def __init__(self, rows=1, cols=1):
        super(NewMatrixForm, self).__init__()
        self.L = MatrixField(5, 5)

def validate_num(form, field):
    if field.data != 42:
        raise ValidationError(u'Must be 42')"""

class EnterMatrixForm(FlaskForm):
    rows = IntegerField('Rows', validators=[DataRequired(),NumberRange(min=0)])
    cols = IntegerField('Columns', validators=[DataRequired(),NumberRange(min=0)])
    entry = TextAreaField('Matrix', validators=[DataRequired()])
    detailed_solution = BooleanField('Detailed')
    #dropdown? for different options .. interesting indeed
    submit = SubmitField('Create a Matrix')
    