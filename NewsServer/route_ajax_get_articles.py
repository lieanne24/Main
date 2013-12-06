from NewsServer import app, cnx
from flask import render_template, request
from NewsServer.Classes.ArticleSummary import ArticleSummary

@app.route('/ajax/get_article_summaries/<category>/')
def get_article_summaries(category):
    article_start = int( request.args.get('start') )
    dog = cnx.cursor()
    dog.callproc("get_article_summaries_range", (category,article_start,5))
    results = dog.fetchall()
    dog.close()
    
    SummaryList = []
    
    for row in results:
        SummaryList.append(ArticleSummary(*row))
     
    return render_template('article_summaries.html', SummaryList=SummaryList)