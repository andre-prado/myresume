import environ

from myportfolio.settings.base import *


env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRECT_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DABASES = {
    'default': env.deb(),
}