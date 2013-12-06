from NewsServer import app
from flask import abort, send_file

@app.route('/images/<path:filename>')
def serve_image(filename):
    if '..' in filename or filename.startswith('/'):
        abort(404)
    return send_file("images/" + filename)