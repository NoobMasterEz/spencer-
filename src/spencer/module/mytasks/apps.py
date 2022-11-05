from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MytasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spencer.module.mytasks'
    label = 'mytasks'
    verbose_name = _('My Tasks')
