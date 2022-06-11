import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-68x(o+7i-55@#n%=werf66tm8@%7j3ar&!qd(nau69aws^8^us'
#with open(os.path.join(BASE_DIR,'secret_keys.txt')) as f:
#    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'social',
        'USER': 'social',
        'PASSWORD': 'stq1w12r',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
DEBUG = False

ALLOWED_HOSTS = ['37.228.117.132']

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
