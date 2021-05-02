import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

# AWS Example
ALLOWED_HOSTS = ['.elasticbeanstalk.com']

DATABASE = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : os.environ['DATABASE_NAME'],
        'PASSWORD' : os.environ['DATABASE_USER'],
        'HOST' : 'django.mysql.ap-northeast-s.rds.amazonaws.com',
        'PORT' : '3306',
        'OPTIONS' : {
            'init_command' : "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}