from NewsServer import app, cnx
from flask import render_template, request
from NewsServer.Classes.Comment import Comment
from NewsServer.Classes.Article import Article

@app.route('/ajax/get_comments/<int:article_id>/')
def get_article_comments(article_id):
    
    comment_start = int( request.args.get('start') )
    order = request.args.get('order')
    
    dog = cnx.cursor()
    dog.callproc("get_article_comments_range", (article_id,order,comment_start,5))
    results = dog.fetchall()
    dog.close()
    
    article = Article(article_id)
    article.commentList = []   
    
    for row in results:
        article.commentList.append(Comment(*row))
     
    return render_template('comments.html', article=article)