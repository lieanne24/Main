from flask.ext.wtf import Form  # @UnresolvedImport
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, validators, ValidationError  # @UnresolvedImport
from flask import request, flash
from NewsServer import app



class uploadArticle(Form):
   
    title = TextField("Title",  [validators.Required("Article Title")])
    # author = TextField("Author",[validators.Required("Author")])
    body = TextAreaField("body",  [validators.Required("Please enter something")])
    submit = SubmitField("Upload Article")
    
    
    def __init__(self, *args, **kwargs):
      Form.__init__(self, *args, **kwargs)
 
    
    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True
    
        

