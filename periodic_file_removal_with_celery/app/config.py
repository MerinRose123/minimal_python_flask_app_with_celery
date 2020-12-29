from os import environ


class Config:
    DEBUG = False
    SERVICE_NAME = 'piracy_detection'

    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = 6379
    BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(
        host=REDIS_HOST, port=str(REDIS_PORT)))
    CELERY_RESULT_BACKEND = BROKER_URL


class LocalConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = False


config_by_name = {
    "local": LocalConfig,
    "dev": DevelopmentConfig,
}