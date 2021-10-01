from celery import shared_task

from apps.api import models
from apps.api.models import AgreeMessage


@shared_task
def to_start_agreeMessage_task(message_id):
    models.AgreeMessage.objects.filter(id=message_id).update(status=AgreeMessage.STATUS_START)


@shared_task
def to_end_agreeMessage_task(message_id):
    models.AgreeMessage.objects.filter(id=message_id).update(status=AgreeMessage.STATUS_END)
