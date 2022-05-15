from django.core.mail import send_mail

from websystem.celery import app


@app.task(name="post_send_enqueries_mail", queue="estates")
def post_send_enqueries_mail(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
