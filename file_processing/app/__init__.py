from flask import Flask
from celery import Celery
import os
from celery_config import CeleryConf
from config import config_by_name

# Declared globally for easy access
celery = Celery(__name__)
app = Flask(__name__)


def create_app():
    # Change environment variable to get into development environment mode
    app.config.from_object(config_by_name[os.getenv('FLASK_ENVIRONMENT') or 'local'])
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


