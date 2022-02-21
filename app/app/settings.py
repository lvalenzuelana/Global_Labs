"""
Institut Polytechnique de Paris
Global Laboratory for Industry-Driven Software Development
Django settings for Ethics4EU project.
Django version 3.2.10
Contributors:
→ Luis Enrique Valenzuela Navarro
→ Juan Diego Arias Rossa
→ Dennis Josue Mejicanos Garcia
→ Julio Enrique Guzman Barraza
"""
from pathlib import Path
import os
# → Base directory for the project.
BASE_DIR = Path(__file__).resolve().parent.parent

# → SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure---nn)%&-_-3q+gm@&zy-zvmjsb7c_9p+ytw6n$4fv^@gk0nw3o'

# → SECURITY WARNING: don't run with debug turned on in production!
# # To activate it, set the value of DEBUG = True
DEBUG = True

# → If you want the application to be published by a specific host or group of hosts you can set it in the following variable.
ALLOWED_HOSTS = ["*"]

# →  Application definition
INSTALLED_APPS = [
    'teacher.apps.TeacherConfig',
    'signup.apps.SignupConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# → Additional Django tools that were used for the elaboration of the project.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# → URLs used within the project.
ROOT_URLCONF = 'app.urls'

# → Here are the HTML files for the different urls configured in the application. 
# # You must insert a new HTML file each time you configure a new view within the application.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'app.wsgi.application'

# → Database
# # Here is the configuration for connecting to a Postgres database. 
# # If you want to change the database, you can refer to the following link:
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Ethics4EU',
        'USER': 'postgres',
        'PASSWORD': 'global22labs',
        'HOST': '192.168.192.150',
        'PORT': '5432'
    }
}

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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# → Here the model for authentication within the application was defined.
AUTH_USER_MODEL='signup.rol'
# → This redirection is useful for when a user logs out of the application.
LOGOUT_REDIRECT_URL = '/'
# → These variables are used to display the papers within the database. 
# # Please change the current directory to your own.
MEDIA_URL = '/home/wicho/Desktop/Papers/'
MEDIA_ROOT = os.path.join('/home/wicho/Desktop/', 'Papers')
