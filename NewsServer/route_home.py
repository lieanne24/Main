from NewsServer import app, cnx
from NewsServer.Classes.ArticleSummary import ArticleSummary
from flask import render_template


@app.route('/')
def home():
    dog = cnx.cursor()
    dog.callproc("get_article_summaries_range", ("all",0,5))
    results = dog.fetchall()
    dog.close()
    
    SummaryList = []
    
    for row in results:
        SummaryList.append(ArticleSummary(*row))
     
    return render_template('home.html', category="all", SummaryList=SummaryList)