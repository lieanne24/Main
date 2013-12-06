from NewsServer.Classes.User import User
from NewsServer.Classes.Admin import SearchEmail
from flask import abort,send_file, render_template, session, redirect, url_for, request
from NewsServer import app, cnx
from Classes.RoleList import RoleList
from NewsServer import app
from Classes.RoleList import RoleList

@app.route('/admin/', methods =['GET','POST'])
def Admin():
    form=SearchEmail() #create a value for the search email and hold it in form
    if 'user_id' not in session:
        return redirect(url_for('signin'))
    
    role_list = RoleList(session['user_id'])
    
    if 'admin' not in role_list.roles:
        return redirect(url_for('home'))
    
    if request.method =='GET':
        
        
        return render_template('admin_1.html',form=form)
    else:       #is a post
        
        if not form.validate():
            return render_template('admin.html',form=form)
            user = User.byEmail(form.search.data)
            user_id = user.user_id
                        
                
        return render_template('admin_1.html', user_id=user_id, email=form.search.data)