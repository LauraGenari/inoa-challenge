from django.core.mail import send_mail

def send_alert_email(asset, price, alert_type):
    subject = f"Stock Alert: {asset.name} - {alert_type.upper()}"
    message = f"The price of {asset.name} has reached {price}. Consider {alert_type}ing."
    send_mail(subject, message, 'from@example.com', ['to@investor.com'])

import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, recipient):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'seuemail@example.com'
    msg['To'] = recipient

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()