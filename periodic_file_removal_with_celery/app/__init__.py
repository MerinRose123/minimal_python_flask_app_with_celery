from flask import Flask
from celery import Celery
from . import celery_config
from .config import config_by_name

app = Flask(__name__)
app.config.from_object(config_by_name['local'])


def make_celery(app):
    # create context tasks in celery
    celery = Celery(
        app.import_name,
        broker=app.config['BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.config_from_object(celery_config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


celery = make_celery(app)


@app.route('/')
def view():
    return "Flask is up and running!"


if __name__ == "__main__":
    app.run()