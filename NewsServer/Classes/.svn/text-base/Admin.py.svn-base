from flask.ext.wtf import Form  # @UnresolvedImport
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, validators, ValidationError
from flask import request, flash
from NewsServer import app

class SearchEmail(Form):
    search = TextField("Search Email for User", [validators.required("Please enter an email to search"), validators.Email("Please enter a valid mail address")])
    #adminOptions = TextField("What would you like to do?", [validators.required("adminOptions")])
    submit = SubmitField("Search Email")
    
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
        