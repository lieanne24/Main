'''
Created on Nov 28, 2013

@author: devuser
'''

class ArticleSummary(object):
    '''
    Truncated article format
    '''


    def __init__(self, *args):
        '''
        Constructor
        '''
        self.article_id, self.title, self.author_id, self.author_name, self.template, self.category, self.body, self.create_time = args