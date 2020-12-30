from datetime import timedelta


class CeleryConf:
    CELERY_IMPORTS = 'app.tasks'
    CELERY_TASK_RESULT_EXPIRES = 30
    CELERY_TIMEZONE = 'UTC'

    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    # Add celery tasks which should be run in scheduled manner here
    CELERYBEAT_SCHEDULE = {
        'test-celery': {
            # the celery task name
            'task': 'periodic_temporary_file_delete',
            # Duration in which the task should be repeated. Currently set as 1 min
            'schedule': timedelta(seconds=60),
        }
    }