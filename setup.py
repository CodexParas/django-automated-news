from pathlib import Path
import django
from django.conf import settings
BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'home',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
settings.ALLOWED_HOSTS = ['*']
settings.configure(
    INSTALLED_APPS = INSTALLED_APPS,
    DATABASES = DATABASES,
)
django.setup()