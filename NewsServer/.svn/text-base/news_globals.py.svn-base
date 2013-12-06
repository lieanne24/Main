from NewsServer import app, cnx
from NewsServer.Classes.forms import SigninForm
from NewsServer.Classes.CommentForms import CommentForm

dog = cnx.cursor()
dog.callproc("get_article_categories", () )
results = dog.fetchall()
dog.close()
categories = []

# Find the total number of characters in all categories
total_length = 0
for row in results:
    total_length = total_length + len(row[0])

# Create a list containing each category name, and its length as a percentage of the full list
for row in results:
    length = len(row[0]) / float(total_length) * 100
    categories.append( (row[0], length) )
                        
app.jinja_env.globals['categories'] = categories

@app.context_processor
def form_processor():
    def create_form():
        return SigninForm()
    return dict(create_form=create_form)

@app.context_processor
def form_processor_comment():
    def create_form_comment():
        return CommentForm()
    return dict(create_form_comment=create_form_comment)