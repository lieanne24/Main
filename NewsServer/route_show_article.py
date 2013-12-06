from NewsServer.Classes.Article import Article
from NewsServer.Classes.Comment import Comment
from flask import abort, render_template
from NewsServer import app, cnx

@app.route('/articles/<int:article_id>/')
def show_article(article_id):
    '''
    Get an article by the ID number, and display it to the page
    '''
    article = Article(article_id)
    if (article == None):
        abort(404)
    
    return render_template("article_display.html", article=article)