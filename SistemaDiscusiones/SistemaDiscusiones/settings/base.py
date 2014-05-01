from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'o0k45-ya1i79l!6p2s4+9g^h$_04j(qtahmi2krd2wkv2)%%)k'

DJANGO_APPS = (
		'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	)

THIRD_PARTY_APPS = (
		#'south',
		'social.apps.django_app.default',
		'djrill',
	)

LOCAL_APPS = (
		'apps.home',
		'apps.users',
		'apps.discuss',
		'apps.tests',
	)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = (
		'social.backends.facebook.FacebookAppOAuth2',
		'social.backends.facebook.FacebookOAuth2',
		'social.backends.twitter.TwitterOAuth',
		'django.contrib.auth.backends.ModelBackend',
	)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/extra-data/'
SOCIAL_AUTH_LOGIN_URL = '/error/'

SOCIAL_AUTH_USER_MODEL = 'users.User'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
		'social.pipeline.social_auth.social_details',
	    'social.pipeline.social_auth.social_uid',
	    'social.pipeline.social_auth.auth_allowed',
	    'social.pipeline.social_auth.social_user',
	    'social.pipeline.user.get_username',
	    'social.pipeline.user.create_user',
	    'social.pipeline.social_auth.associate_user',
	    'social.pipeline.social_auth.load_extra_data',
	    'social.pipeline.user.user_details',
	    'apps.users.pipelines.get_avatar',
	)

EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
		'social.apps.django_app.context_processors.backends',
	)
