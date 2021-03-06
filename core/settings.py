
import dj_database_url
from pathlib import Path
from decouple import config
import cloudinary
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')

# DEBUG = config('DEBUG', bool)
DEBUG = False

ALLOWED_HOSTS = ['fpcbackend.herokuapp.com', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third_party apps
    'rest_framework',
    'corsheaders',

    # Media Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # myapp
    'fpc_api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise setting
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Heroku: Update database configuration from $DATABASE_URL.
if not DEBUG:
    db_from_env = dj_database_url.config(conn_max_age=500)
    db_from_env['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = f'{BASE_DIR}/staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary stuff for serving media files
if DEBUG:
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config('CLOUD_NAME', default=""),
        'API_KEY': config('API_KEY', default=""),
        'API_SECRET': config('API_SECRET', default=""),
    }

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# media fields
MEDIA_URL = '/media/'
MEDIA_ROOT = f'{BASE_DIR}/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django cors settings
CORS_ALLOWED_ORIGINS = [
    "https://fiddypolyclinic.netlify.app",
    "https://sub.example.com",
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
]

# Django rest settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
}
