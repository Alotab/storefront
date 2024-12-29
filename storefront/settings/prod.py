import os
from .common import *
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = []