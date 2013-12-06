from NewsServer import cnx
from NewsServer.Classes.CommentReply import CommentReply

class Comment(object):
    
    '''
    This class will get a comment from the database
    '''
    def __init__(self, comment_id, article_id, user_id, display_name, comment_text, upvotes, downvotes, rating, create_time):
        
        self.comment_id = comment_id
        self.article_id = article_id
        self.user_id = user_id
        self.user_name = display_name
        self.comment_text = comment_text
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.rating = rating
        self.create_time = create_time
        self.replies = []
        
        #get first three replies to this comment
        dog = cnx.cursor()
        dog.callproc('get_comment_replies_range', (self.comment_id,0,3))
        results = dog.fetchall()
        dog.close()
        
        for reply in results:
            self.replies.append(CommentReply(*reply))