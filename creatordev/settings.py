from pathlib import Path
import os 
from django.db.backends.mysql.base import DatabaseWrapper

BASE_DIR = Path(__file__).resolve().parent.parent
 
SECRET_KEY = 'django-insecure-w3g+c8v@fo^#5ttn&-x(lca)7om676aj%#zchlw7nqibm%p5w7'
 
DEBUG = False

ALLOWED_HOSTS = ['creatorsdev.herokuapp.com','*']
 
# Application definition

INSTALLED_APPS = [
    # added
    'ckeditor',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', 
    'django.contrib.sites',
    # Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    # my apps
    'article',
    'user',
    'home',  
    'api',   
    'forum',
]

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'whitenoise.middleware.WhiteNoiseMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'creatordev.urls' 

# Custom user manually added
AUTH_USER_MODEL = 'user.CustomUser'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'creatordev.wsgi.application'


# Database  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "sql8526241",
        "USER":"sql8526241",
        "PASSWORD":"aCNe7CfcjY",
        "PORT":3306,
        "HOST":"sql8.freesqldatabase.com"
    }
}
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
DISABLE_COLLECTSTATIC=1
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ 
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }, 
 
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
 

# Static files (CSS, JavaScript, Images) 
 
# For Deployment
# STATICFILES_DIRS = os.path.join(BASE_DIR, '/static'), 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static/') 
 

# heroku setup STATICFILEs


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR , 'static/') 

# STATIC_ROOT = os.path.join(BASE_DIR , 'static')
# STATICFILES_DIRS = (os.path.join(BASE_DIR , 'static'),)
# django_heroku.settings(locals())



# Media files store
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media/') 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Manually added
AUTHENTICATION_BACKENDS = [ 
    'django.contrib.auth.backends.ModelBackend', 
    'allauth.account.auth_backends.AuthenticationBackend', 
]

SITE_ID = 1
 

#  All - Auth Provider
SOCIALACCOUNT_PROVIDERS = {
    
    # Google
    'google': { 
        'SCOPE':{
            'profile',
            'email',
        },
        'APP': {
            'client_id': '710015700654-8s674ftifh4rnac60l7jpfc5sp9kjs93.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'AUTH_PARAMS':{
            'access_type':'online'
        }
    },

    # Github
    'github': { 
        'APP': {
            'client_id': '73927e38386dc3a6929b',
            'secret': 'd34aa5dfc70fb92aee94eb1a5a7abf754d8bb7db',
            'key': ''
        }
    },

    # Facebook 
      'facebook': { # callback url -> http://localhost:8000/accounts/figma/login/callback/
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],   
    }
}

LOGIN_REDIRECT_URL = "/"
ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'
LOGOUT_REDIRECT_URL = "/"
 

# CKEDITOR
CKEDITOR_UPLOAD_PATH = 'uploads/' 
CKEDITOR_CONFIGS = {
    'default':{
        'extraPlugins':'codesnippet',
        'toolbar':'full',
    },
}

# Sending Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "creatordevcommunity@gmail.com"
EMAIL_HOST_PASSWORD = "ynetdngvgscswmts"


