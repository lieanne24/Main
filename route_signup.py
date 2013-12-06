from NewsServer import app, cnx
from flask import render_template, session, redirect, url_for, request
from Classes.forms import SignupForm
from flaskext.bcrypt import Bcrypt  # @UnresolvedImport
from Classes.RoleList import RoleList

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    bcrypt = Bcrypt(app)
    if 'user_id' in session:
        return redirect(url_for('profile'))
    
     
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            password = bcrypt.generate_password_hash(form.su_password.data,10)
            cursor= cnx.cursor()
            cursor.callproc('create_new_user',[form.su_username.data,form.su_firstname.data, form.su_lastname.data, form.su_email.data,password])
            user_id = cursor.fetchone()
            cursor.close()
        if request.method == 'POST':    
            rolelist = RoleList(user_id[0])
            session['user_id'] = user_id[0]
            session['roles'] = rolelist.roles
            
            
            return redirect(url_for('profile')) 
     
    elif request.method == 'GET':
        return render_template('signup.html', form=form)