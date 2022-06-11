import os
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-68x(o+7i-55@#n%=r)ht66tm8@%7j3ar&!qd(nau69aws^8^us'


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'social_website',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIR = [STATIC_DIR]