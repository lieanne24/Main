from NewsServer.Classes.Article import Article
from flask import abort, send_file, render_template, session, redirect, url_for, request
from NewsServer import app, cnx
from Classes.upload import uploadArticle
from Classes.RoleList import RoleList


@app.route('/upload/', methods=['GET', 'POST'])
def upload_article():
    # If user isn't logged in, kick them to the signin page
    if 'user_id' not in session:
        return redirect(url_for('signin') )
    
    # If user is signed in, keep going to check their access roles
    role_list = RoleList(session['user_id'])
    #roles = """"""
    #for role in role_list.roles:
        #roles = role + "\n"
    #return str(role_list.roles)
    
    # If they don't have the 'contributor' role, kick them to the home page
    # No need for a user-friendly error - a well-behaved non-contributor wouldn't have found their way here anyway
    if 'contributor' not in role_list.roles:
        return redirect(url_for('home'))
    
    # If they check out, keep processing and let them do their thing
    
    forms=uploadArticle()
    
    catCursor = cnx.cursor()
    catCursor.callproc("get_article_categories",())   
    
    category = catCursor.fetchall() 
    catCursor.close()
    
    tempCursor = cnx.cursor()
    tempCursor.callproc("get_article_templates",())
    tempFetch = tempCursor.fetchall()
    tempCursor.close()
    
    if request.method == 'POST':
        cursor = cnx.cursor()
        cursor.callproc("create_new_article", [forms.title.data, session['user_id'], request.form["category"],'brief_text', forms.body.data])
        articleId = cursor.fetchone()
        cursor.close()
        
        imageCurser = cnx.cursor()
        imageCurser.callproc("create_article_reference", [articleId[0], "01", request.form['image'],"hello"])
     
        
        imageCurser.close()
            
        #return render_template("upload.html", form=forms, category=category)
        return redirect(url_for("home"))
    return render_template("upload.html", form=forms, category=category)




