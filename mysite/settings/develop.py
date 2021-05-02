from .base import *


SECRET_KEY = 'uz&t=9409*c9h&zic+pva+wus=jimxx-^7u7a=m0vxqge#&j@g'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}