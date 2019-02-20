from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, DecimalField, BooleanField, SubmitField, FieldList, FormField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError

class EnterMatrixForm(FlaskForm):
    entry = TextAreaField('Matrix', validators=[DataRequired()])
    detailed_solution = BooleanField('Detailed')
    submit = SubmitField('Create a Matrix')
    c = [('g', 'Gaussian Elimination'), ('s', 'Solve Matrix'), ('i', 'Inverse'), ('d', 'Determinant'), ('t', 'Transpose')] #choices for the user
    options = SelectField('Operation', choices=c, validators=[DataRequired()])

class EnterMatrixForm2(FlaskForm):
    c = [('g', 'Go to bed'), ('s', 'Set date'), ('i', 'Inverse'), ('d', 'Determinant'), ('t', 'Transpose')] #choices for the user
    options = SelectField('Operation', choices=c, validators=[DataRequired()])