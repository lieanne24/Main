'''
Created on Nov 27, 2013

@author: devuser
'''
from NewsServer import cnx
from NewsServer.Classes.Comment import Comment

class Article(object):
    '''
    This class represents a row from the "article" database view"
    '''
    
    def __init__(self, article_id):
    #def __init__(self, article_id, title, author_id, author_name, template, category, body_text, pub_date):
        '''
        Constructor
        '''
        cursor = cnx.cursor()
        cursor.callproc("get_article_by_id", (article_id,))
        
        result = cursor.fetchone()
        cursor.close()
        
        try:
            #unpack stored procedure result into instance variables... order of variables is important!
            self.article_id, self.title, self.author_id, self.author_name, self.template, self.category, self.body_text, self.pub_date = result
            
            self.commentList = []
            
            #Get first 5 comments
            dog = cnx.cursor()
            dog.callproc("get_article_comments_range",(self.article_id,"oldest", 0, 5) )
            article_comments = dog.fetchall()
            dog.close()
            
            for comm in article_comments:
                self.commentList.append(Comment(*comm))
            
        except: pass
        