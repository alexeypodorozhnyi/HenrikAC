from henrikac.settings import *

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '.henrikac.com'
]

SECRET_KEY = get_env_variable('SECRET_KEY')
