"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^m90!+=gp%33ttv*+ygni-ha6ybiofb44my^_^^+y+)%n*dk%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #True for development phase

ALLOWED_HOSTS = ['samyarsworld-ecommerce.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'website',
    'django_filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # To serve static files with heroku
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myDatabase', #'DEMO_TEST',
        'USER': 'samyarsworld', #'postgres',
        'PASSWORD': '14121822', #'1412',
        'HOST': 'mydatabase.cna7xdars2rx.us-east-1.rds.amazonaws.com', #'localhost',
        'PORT':'5432'
    }
}
'''

#AWS S3: The are other ways to connect to s3 like enviornmental variables and you
# need to use them: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
AWS_S3_ACCESS_KEY_ID = 'AKIAURCWQF5QNUJAMM4F'
AWS_S3_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'samyarsworld-ecommerce'

# Uncomment to use S3
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage' # looks at s3 first
# use: python3 manage.py collectstatic
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None


# Instead of copying over the files from local 'static' folder, it's better to 
# run 'python manage.py collectstatic' after configuring AWS settings. This command 
# auto uploads all the local static files including 'admin' files.

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# for heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIR =[
    os.path.join(BASE_DIR, 'website/static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'website/static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#SMTP Configuration (simple mail transfer protocol)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'samyarfarjam7@gmail.com'
#EMAIL_HOST_PASSWORD = '14121822sS@'
EMAIL_HOST_PASSWORD = 'slicdqggircsvazg'