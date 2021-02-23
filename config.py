import os

class Config():
    '''
    General configuration of the parent class

    '''

class prodConfig(Config):
    '''
    production configuration of child class
    Args : 
        Config - the parent configuration class with general configuration settings

    '''

    Debug = True
config_options = {
    'development':DevConfig,
    'production':prodConfig
}