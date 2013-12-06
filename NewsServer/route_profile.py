from NewsServer import app, cnx
from flask import render_template, session, redirect, url_for, request, flash
from Classes.profile import ProfileForm
from Classes.User import User
from flaskext.bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
@app.route('/profile/')
def profile():
    form = ProfileForm()
    if 'user_id' not in session:
        return redirect(url_for('signin'))

    else:
        user = User.byId(session['user_id'])
        cursor= cnx.cursor()
        cursor.callproc("get_article_titles_by_author", [user.user_id])
        articles = cursor.fetchall()
        cursor.close
        return render_template('profile.html', user=user, articles = articles)
       

@app.route('/profile/<int:user_id>')
def profile_by_id(user_id):
        user = User.byId(user_id)
    
        cursor= cnx.cursor()
        cursor.callproc("get_article_titles_by_author", [user.user_id])
        articles = cursor.fetchall()
        cursor.close
        return render_template('profile.html', user=user, articles = articles)
        #return render_template('profile.html',username= user_email[0])
        


@app.route('/editProfile/', methods=['GET', 'POST'])
def editProfile():
    form = ProfileForm()

    user = User.byId(session['user_id']) 
    if 'user_id' not in session:
        return redirect(url_for('signin'))
    
    if form.validate_on_submit() == False:
        
        form.firstname.data = user.first_name
        form.lastname.data = user.last_name
        form.about.data = user.about_me
    else:
    
        cursor= cnx.cursor()
        cursor=cnx.cursor()
        cursor.callproc('update_user',(user.user_id,form.firstname.data,form.lastname.data,form.about.data))
        cursor.close()
        cnx.commit()
        flash('saved changes')
    if form.change_password.data:   
            hashing_pwd = bcrypt.generate_password_hash(form.change_password.data,10)
            cursor = cnx.cursor()
            cursor.callproc("update_user_password", [user.user_id,hashing_pwd])
            cursor.close()
            flash('saved changes')
       
    return render_template('editProfile.html',form=form)
