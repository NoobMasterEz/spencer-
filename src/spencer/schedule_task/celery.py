# django_celery/celery.py
from celery import Celery, Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


class MainTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error('{0!r} failed: {1!r}'.format(task_id, exc))
