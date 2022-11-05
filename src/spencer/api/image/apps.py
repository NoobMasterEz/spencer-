from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spencer.api.image'
    label = 'image'
    verbose_name = _('API Image')
