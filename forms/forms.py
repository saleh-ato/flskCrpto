from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired,Email,EqualTo, InputRequired

class signUpForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    passWord=PasswordField('Password',validators=[DataRequired(),EqualTo('passWord_Repeat', message='Passwords must match')])
    passWord_Repeat=PasswordField('Repeat Password')
    email_Address=EmailField('Email', validators=[InputRequired("Please enter your email address."),Email()])
    submit=SubmitField('Submit')