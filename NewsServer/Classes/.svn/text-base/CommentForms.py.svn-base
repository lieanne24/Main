from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired
from flask import request, flash

class CommentForm(Form):
    '''
    classdocs
    '''
    
    commentText = TextAreaField('Speak your comment!', validators=[DataRequired()])


    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        