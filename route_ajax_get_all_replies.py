from NewsServer import app, cnx
from flask import render_template
from NewsServer.Classes.CommentReply import CommentReply
from NewsServer.Classes.Comment import Comment

@app.route('/ajax/get_all_replies/<comment_id>/')
def get_comment_replies(comment_id):
    
    #fetch the parent comment
    dog = cnx.cursor()
    dog.callproc("get_comment_by_id", (comment_id,))
    result = dog.fetchone()
    dog.close()
    
    comment = Comment(*result)
    
    #replace the default set of 3 comments with a blank list (easier to start blank than to append)
    comment.replies = []
    
    #fetch all of the comment replies
    dog = cnx.cursor()
    dog.callproc('get_comment_replies_all', (comment_id,))
    results = dog.fetchall()
    dog.close()

    for reply in results:
        comment.replies.append(CommentReply(*reply))
     
    return render_template('comments_single.html', comment=comment)