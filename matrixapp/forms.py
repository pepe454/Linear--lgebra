from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, DecimalField, BooleanField, SubmitField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class EnterMatrixFormBase(FlaskForm):
    entry = TextAreaField('Matrix', validators=[DataRequired()])
    detailed_solution = BooleanField('Detailed')
    submit = SubmitField('Submit a matrix for operation')
    c = [('g', 'Gaussian Elimination'), ('s', 'Solve Matrix'), ('i', 'Inverse'), ('d', 'Determinant'), ('t', 'Transpose')] #choices for the user
    options = SelectField('Operation', choices=c, validators=[DataRequired()])

class EnterMatrixFormIndex(EnterMatrixFormBase):
    c = [('g', 'Gaussian Elimination'), ('s', 'Solve Matrix'), ('i', 'Inverse'), ('d', 'Determinant'), ('t', 'Transpose')] #choices for the user
    options = SelectField('Operation', choices=c, validators=[DataRequired()])

class EnterMatrixFormSolution(EnterMatrixFormBase):
    c = [('g', 'Gaussian Elimination'), ('s', 'Solve Matrix'), ('i', 'Inverse'), ('d', 'Determinant'), ('t', 'Transpose')] #choices for the user
    options = SelectField('Operation', choices=c, validators=[DataRequired()])