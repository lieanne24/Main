from NewsServer import app, cnx
from flask import render_template, request, session
from NewsServer.Classes.Article import Article
from NewsServer.Classes.Comment import Comment

@app.route('/ajax/add_comment/<int:article_id>/', methods=('GET', 'POST'))
def add_comment(article_id):
    
    if 'user_id' in session:
        pass
    return "blarg"