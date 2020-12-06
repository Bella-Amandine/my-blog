import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://amandine:pass@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''

    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args: 
        Config: The parent configuration class with General configuration settings
    '''
    pass

config_options = {
    'development' : DevConfig(),
    'production' : ProdConfig()
}