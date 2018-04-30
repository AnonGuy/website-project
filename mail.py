"""Functions for various email-related purposes."""

import smtplib

from constants import EMAIL_AUTH

my_address = EMAIL_AUTH['email']


def send_message(to_address, body):
    """Send an email message to a given address."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(
        EMAIL_AUTH['email'],
        EMAIL_AUTH['password']
    )
    message = '\r\n'.join((
        'From: ' + my_address,
        'To: ' + to_address,
        'Subject: Thank you for your input!',
        '',
        body
    ))
    server.sendmail(
        my_address, to_address, message
    )
    server.close()
