import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///database.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
