
THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'django_celery_results',
    'drf_yasg',
]

API_APPS = [
    'spencer.api.image',
]

LOCAL_APPS = [
    'spencer.module.camera',
    'spencer.module.mytasks',
    'spencer.module.users',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MAIN_APPS = list(
    DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS + API_APPS)
