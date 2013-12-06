from NewsServer import app


import NewsServer.routes

app.debug = True
app.run(host='0.0.0.0')