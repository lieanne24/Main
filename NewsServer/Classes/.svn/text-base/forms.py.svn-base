from flask.ext.wtf import Form  # @UnresolvedImport
from wtforms import TextField, TextAreaField, SubmitField, PasswordField, validators, ValidationError
from flask import request, flash
from flaskext.bcrypt import Bcrypt  # @UnresolvedImport
from flaskext.bcrypt import check_password_hash  # @UnresolvedImport
from NewsServer import app, cnx
import User


flask_bcrypt = Bcrypt(app)

class SignupForm(Form):

    su_username = TextField("username",[validators.Required("Please enter your username")])
    su_firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
    su_lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
    su_email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    su_password = PasswordField('Password', [validators.Required("Please enter a password."),validators.EqualTo('confirm',message='password must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Create account")
    
    
    def validate(self):
        cursor=cnx.cursor()
        if not Form.validate(self):
            return False
        cursor.callproc('check_username',[self.su_username.data])
        username=cursor.fetchall()
        cursor.close()
        
        cursor=cnx.cursor()
        cursor.callproc('check_email',[self.su_email.data.lower()],)
        user_email=cursor.fetchone()
        cursor.close()
        
        if username:
            self.su_username.errors.append('username already taken')
            return False
        
        if len(self.su_password.data) < 12:
            self.su_password.errors.append('password must be greater than 12 characters')
            return False
        
   
        if user_email:
            self.su_email.errors.append("email address is already taken" )
            return False
        
        else:
            return True
        
class SigninForm(Form):
    email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Sign In")
   
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
 
    def validate(self):
        if not Form.validate(self):
            return False
    
        cursor = cnx.cursor()
        cursor.callproc("check_pwd", [self.email.data.lower(),])
        user = cursor.fetchone()
        cursor.close()
      
        
       
        
        if user:
                hashpwd=self.password.data
                hashing_pwd =flask_bcrypt.check_password_hash(user[0],hashpwd)
                if hashing_pwd:
                     return True
                else: 
                    self.email.errors.append("Invalid password")
                    return False
        else:
            self.email.errors.append("Invalid e-mail")
            return False  
    