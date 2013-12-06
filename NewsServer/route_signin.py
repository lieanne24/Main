from NewsServer import app, cnx
from flask import session, redirect, url_for, request, render_template
from flaskext.bcrypt import Bcrypt  # @UnresolvedImport
from Classes.forms import SigninForm
from Classes.User import User

@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if 'user_id' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        if not form.validate():
            return render_template('signin.html', form=form)
        else:
            user = User.byEmail(form.email.data)
                                    
            session['user_id'] = user.user_id
            session['roles'] = user.roles
            return redirect(url_for('home'))
                                 
    elif request.method == 'GET':
        return render_template('signin.html', form=form)