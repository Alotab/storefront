import os
from dotenv import load_dotenv
from .common import *

load_dotenv()

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'), 
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),   
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

