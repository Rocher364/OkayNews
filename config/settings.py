from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-okaynews-2026'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Lis Aplikasyon
INSTALLED_APPS = [
    'jazzmin',  # Dwe anvan admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Aplikasyon ekstèn
    'taggit',
    'mptt',
    'django_ckeditor_5', # Sèvi ak sa a pou editè rich la
    
    # Aplikasyon ou yo
    'articles',
    'comments',
]

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

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'articles.context_processors.categories',
        ],
    },
}]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Konfigirasyon lang ak tan
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichye Statik ak Media
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- KONFIGIRASYON CKEDITOR 5 ---
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'uploadImage', 'blockQuote'],
    },
}
# Pou jere kote imaj yo ye
CKEDITOR_5_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# Konfigirasyon Imèl
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'webmaster@okaynews.com'

# Konfigirasyon Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "OkayNews Admin",
    "site_header": "OkayNews",
    "site_brand": "OkayNews",
    "welcome_sign": "Bienvenue dans l'interface d'administration d'OkayNews",
    "copyright": "OkayNews d'actualites",
    
    "custom_links": {
        "articles": [{
            "name": "Retourner dans la page d'accueil",
            "url": "/",
            "icon": "fas fa-home",
        }]
    },
    "language_chooser": True,
}