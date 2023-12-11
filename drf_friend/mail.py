from django.core.mail import send_mail
from django.template.loader import render_to_string

EMAIL_TEMPLATES = {
    'registration_email': 'mail/register_user.html',
    # Add more templates as needed
}


def send_template_mail(subject, template_name, recipient_list, context=None):
    # Render the email template with the given context
    email_body = render_to_string(template_name, context)
    
    # Send the email
    send_mail(
        subject=subject,
        message='',
        from_email='hiremostafa@gmail.com',
        recipient_list=recipient_list,
        html_message=email_body,
    )
    
def send_a_mail(title='', description='', mail_from='', mail_to=''):
  send_mail(
    title,
    description,
    mail_from,
    [mail_to],
    fail_silently=False,
  )