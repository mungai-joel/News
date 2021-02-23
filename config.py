import os

class Config():
    '''
    General configuration of the parent class

    '''
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?apiKey={}"
    ARTICLE_API_BASE_URL= "https://newsapi.org/v2/everything?sources={}&apiKey={}"
    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

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


"apikey = 03fb9adcb9bf415ebfa36d87fedc0653"