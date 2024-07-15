CATEGORY_CHOICES = [
        ('Fazlee', 'Fazlee'),
        ('Langda', 'Langda'),
        ('Gopalbogh', 'Gopalbogh'),
        ('Himsagar', 'Himsagar'),
    ]

STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
    ]


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(user, subject, template,  context={}):
        message = render_to_string(template, context)
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()