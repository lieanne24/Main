from NewsServer import app
from flask import session, redirect, url_for

@app.route('/signout/')
def signout():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    session.pop('user_id', None)
    session.pop('roles', None)
    return redirect(url_for('home'))