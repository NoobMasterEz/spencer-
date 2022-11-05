from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CameraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spencer.module.camera'
    label = 'camera'
    verbose_name = _('Camera')
