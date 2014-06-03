"""
Django settings for lessonkill project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')

## Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(HERE, '/admin/static/').replace('\\','/')
#MEDIA_ROOT = os.path.join(HERE, '../media').replace('\\','/')+'/'

#STATIC_ROOT = '' # can't delete it or /admin/ can't loaded
STATIC_PATH = (
        os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/'),
        )
#STATIC_URL = '/html/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
        os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/'),
        )
##

## media and files
MEDIA_URL = '/media/'
HERE = os.path.dirname(os.path.abspath(__file__))
#MEDIA_ROOT = (
#        os.path.join( os.path.dirname(__file__), '../media/').replace('\\', '/'),
#        )
MEDIA_ROOT = os.path.join(HERE, '../media/').replace('\\','/')

ADMIN_MEDIA_PREFIX='/media/'
##

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#2zza2@ncn#tc$u0^m1sdv=9zr*u4k#bq4-6xewtztcl*2_cnb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEST_DEBUG = False
#TEST_DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
        #'../html/',
        os.path.join(os.path.dirname(__file__), '../static').replace('\\', '/'),#../html
        os.path.join(os.path.dirname(__file__), 'html').replace('\\', '/'),#../html
        )


ALLOWED_HOSTS = ['127.0.0.1:8161']


# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #'lessonkill.products',
    #'lessonkill.books',
    #'django.contrib.redirects',
    #'lessonkill.blog',
    'lessonkill.admin',
    'lessonkill.index',
    'lessonkill.chapter',
    #'lessonkill.upload',
    )

SITE_ID = 1 #for error, with django.contrib.cites

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'lessonkill.urls'

WSGI_APPLICATION = 'lessonkill.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test', #should create a db in mysql first
        'USER': 'root',
        'PASSWORD': '1112611',
        #'HOST_M': 'SAE_MYSQL_HOST_M',
        #'HOST_S': 'SAE_MYSQL_HOST_S',
        'HOST': 'localhost',
        'PORT': '8016',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'
DEFAULT_CHARSET = 'utf-8'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


