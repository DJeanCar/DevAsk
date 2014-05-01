from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER' : 'cursodjango',
        'PASSWORD' : 'pass',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'

SOCIAL_AUTH_FACEBOOK_KEY = '733270286704397'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ff64ecddc1cdd22bd65032f9c465811f'

SOCIAL_AUTH_TWITTER_KEY = 'cND0uJxUMPJ4jEc7qRCw6Q'
SOCIAL_AUTH_TWITTER_SECRET = '4Wud568JSkx1lfrnyr8CGP6J7K5zcdjBH0gZ1dMpM'

MANDRILL_API_KEY = 'ulkTNRKjNKZZeFQGtlTwuA'


CACHES = {
        'default': {
            'BACKEND' : 'redis_cache.RedisCache',
            #'LOCATION' : 'grideye.redistogo.com:10097',
            'LOCATION' : 'localhost:6379',
            'OPTIONS' : {
                'DB' : 1
                #'PASSWORD' :'asdas6d87sf6tsd8f',
               	
                }
            }
        }