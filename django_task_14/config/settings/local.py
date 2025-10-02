from .base import *

DEBUG = True

ALLOWED_HOSTS: list[str] = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql'
        if SECRET.get('DB')
        else 'django.db.backends.sqlite3',
        'NAME': SECRET.get('DB', {}).get('NAME', BASE_DIR / 'db.sqlite3'),
        'USER': SECRET.get('DB', {}).get('USER', ''),
        'PASSWORD': SECRET.get('DB', {}).get('PASSWORD', ''),
        'HOST': SECRET.get('DB', {}).get('HOST', ''),
        'PORT': SECRET.get('DB', {}).get('PORT', ''),
    }
}

