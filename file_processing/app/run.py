from flask import current_app as app


@app.route('/')
def view():
    return "Flask is up and running!"


