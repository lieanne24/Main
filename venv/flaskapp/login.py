from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from wtforms import *


app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE='/tmp/note_app.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def register():
	#if 'user_id' in session:
	#	return redirect(url_for('timeline'))
	error = None
	if request.method == 'POST':
		username = TextField('Username', [validators.Required()])
		password = PasswordField('Password', [validators.Required()(), validators.EqualTo('confirm', message='Passwords must match')])
		confirm = PasswordField('Confirm Password', [validators.Required()])
		email = TextField('eMail', [validators.Required()])
		accept_tos = BooleanField('I accept the TOS', [validators.Required])
		g.db.execute('''insert into user (
                 username, email, pw_hash) values (?, ?, ?)''',
                 [request.form['username'], request.form['email'],
                  generate_password_hash(request.form['password'])])
		g.db.commit()
		flash('You were successfully registered and can login now')
		return redirect(url_for('login'))
	return render_template('register.html', error=error)
if __name__ =='__main__':
	init_db()
	app.run()