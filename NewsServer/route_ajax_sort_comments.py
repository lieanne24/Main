from NewsServer import app, cnx
from flask import render_template, request
from NewsServer.Classes.Article import Article
from NewsServer.Classes.Comment import Comment

@app.route('/ajax/get_sorted_comments/<int:article_id>/<order>/')
def get_sorted_comments(article_id, order):
    
    num_to_get = int( request.args.get('num_to_get') )
    
    # Get the article, and clear the article list
    article = Article(article_id)
    
    # If it's sorted by oldest, then the default comment ordering of an article is fine
    if order == "oldest":
        return render_template('comments.html', article=article)
    else:
        article.commentList = []
        
        dog = cnx.cursor()
        dog.callproc('get_article_comments_range', (article.article_id, order, 0, num_to_get))
        article_comments = dog.fetchall()
        dog.close()
        
        for comm in article_comments:
            article.commentList.append(Comment(*comm))
            
        return render_template('comments.html', article=article)
