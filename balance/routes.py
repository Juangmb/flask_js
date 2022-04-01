from balance import app

@app.route("/")
def inicio():
    return "Website is up and running"