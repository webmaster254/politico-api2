import os


class BaseConfig:
    """ Parent configurattions """
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """ Development mode configurations """
    DEBUG = True


class TestingConfig(BaseConfig):
    """ Testing mode configurations """
    DEBUG = True
    TESTING = True

APP_CONFIG = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
    }