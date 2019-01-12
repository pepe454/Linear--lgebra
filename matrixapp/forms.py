from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, BooleanField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, NumberRange

class CreateMatrixForm(FlaskForm):
    rows = IntegerField('Rows', validators=[DataRequired(),NumberRange(min=0)])
    cols = IntegerField('Columns', validators=[DataRequired(),NumberRange(min=0)])
    submit = SubmitField('Create empty Matrix')

class MatrixListForm(FlaskForm):
    def __init__(self, cols=1):
        self.L = FieldList(DecimalField('Entries', validators=[DataRequired(),NumberRange(min=0)]), min_entries=cols)#, max_entries=cols)


#class SubmitMatrixForm(FlaskForm):
#    A = FieldList(FormField(MatrixListForm())) #min_entries=rows, max_entries=rows)