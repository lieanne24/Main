from flask.ext.wtf import Form  # @UnresolvedImport
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, validators, ValidationError
from flask import request, flash
from NewsServer import app, cnx

class ProfileForm(Form):
    firstname= TextField("First Name",  [validators.Optional()])
    lastname = TextField('Last Name', [validators.Optional()])
    about= TextAreaField('About me',[validators.Optional()])
    password = PasswordField('Password',[validators.Optional()])
    change_password = PasswordField('Change Password', [validators.Optional(),validators.EqualTo('confirm',message='password must match')])
    confirm = PasswordField('Repeat Password')
    submit=SubmitField("save")
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
   