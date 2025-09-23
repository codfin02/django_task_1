import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-me'
DEBUG = True
ALLOWED_HOSTS: list[str] = ["*"]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'users',
]

THIRD_PARTY_APPS: list[str] = []

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / '.static_root'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user
AUTH_USER_MODEL = 'users.User'

# Email: fallback to in-memory backend; can be overridden by secret.json
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 0
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = ''

# Load secrets if available
secret_file = BASE_DIR / '.secret_config' / 'secret.json'
if secret_file.exists():
    try:
        SECRET = json.loads(secret_file.read_text(encoding='utf-8'))
        SECRET_KEY = SECRET.get('DJANGO_SECRET_KEY', SECRET_KEY)
        email_conf = SECRET.get('EMAIL', {})
        if email_conf:
            EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            EMAIL_HOST = email_conf.get('HOST', 'smtp.gmail.com')
            EMAIL_PORT = int(email_conf.get('PORT', 587))
            EMAIL_HOST_USER = email_conf.get('USER', '')
            EMAIL_HOST_PASSWORD = email_conf.get('PASSWORD', '')
            EMAIL_USE_TLS = bool(email_conf.get('USE_TLS', True))
            DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or DEFAULT_FROM_EMAIL
    except Exception:
        pass

