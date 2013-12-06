from NewsServer import app, cnx
from flask import render_template
from NewsServer.Classes.ArticleSummary import ArticleSummary

@app.route('/categories/<category>/')
def show_category(category):
    dog = cnx.cursor()
    dog.callproc("get_article_summaries_range", (category,0,5))
    results = dog.fetchall()
    dog.close()
    
    SummaryList = []
    
    for row in results:
        SummaryList.append(ArticleSummary(*row))
     
    return render_template('home.html', SummaryList=SummaryList, category=category)