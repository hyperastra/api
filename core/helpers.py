import sendgrid
from django.conf import settings


def send_email(**kwargs):
    subject = kwargs.get('subject')
    from_email = sendgrid.Email('Hyperastra <support@hyperastra.com>')
    to_email = sendgrid.To(kwargs.get('email'))

    message = sendgrid.Mail(from_email=from_email, to_emails=to_email)
    message.dynamic_template_data = kwargs.get('data')
    message.template_id = kwargs.get('template_id')

    if subject:
        message.subject = subject

    try:
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e)
        print(
            f"Error while sending template {kwargs.get('template_id')} to {kwargs.get('email')}")