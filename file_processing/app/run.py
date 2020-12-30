from . import app


@app.route('/')
def view():
    return "Flask is up and running!"


