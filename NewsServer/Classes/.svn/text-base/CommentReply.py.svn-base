'''
Created on Dec 2, 2013

@author: devuser
'''

class CommentReply(object):
    '''
    This class represents a row from the MySQL 'reply_view' relation.  It represents a reply to a comment,
    where comments are in response to an article
    '''


    def __init__(self, reply_id, comment_id, user_id, display_name, reply_text, upvotes, downvotes, rating, create_time):
        '''
        Constructor
        '''
        self.reply_id = reply_id
        self.comment_id = comment_id
        self.user_id = user_id
        self.user_name = display_name
        self.reply_text = reply_text
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.rating = rating
        self.create_time = create_time
    
        