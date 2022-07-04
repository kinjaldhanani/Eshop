

from celery.app import task, shared_task
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage, send_mail

logger = get_task_logger(__name__)


@shared_task(name='send_email_task')
def send_email_task():

    user = get_user_model().objects.last()

    mail_sub = "hi"
    message = "hello"
    send_mail(
            subject=mail_sub,
            message=message,
            from_email="kinjal.djanani@trootech.com",
            recipient_list=[user.email]

        )