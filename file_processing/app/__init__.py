from flask import Flask
from celery import Celery
from celery_config import CeleryConf
from config import config_by_name

celery = Celery(__name__)
app = Flask(__name__)


def create_app():
    app.config.from_object(config_by_name['local'])

    return app


def make_celery(app):
    # create context tasks in celery
    celery.conf.update(app.config)
    celery.config_from_object(CeleryConf)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery


