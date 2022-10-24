THIRD_PARTY_APPS = []

LOCAL_APPS = []

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MAIN_APPS = list(
    DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS)
