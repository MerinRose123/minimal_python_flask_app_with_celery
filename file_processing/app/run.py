from . import app
from .tasks import sample_background_task


@app.route('/')
def view():
    # Here background task is called which will run independently. Heavy duty tasks like sending
    # email notifications or processing huge data can be done by this method.
    sample_background_task.delay()
    return "Flask is up and running!"


