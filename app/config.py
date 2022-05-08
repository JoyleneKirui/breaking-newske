class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=a7c82e01873d4300a2317a0bfd25f4c5'
    NEWS_API_KEY ='a7c82e01873d4300a2317a0bfd25f4c5'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True