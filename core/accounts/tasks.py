from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reset_email(user_email, reset_link):
    send_mail(
        'Password Reset Request',
        f'Click the link to reset your password: {reset_link}',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )