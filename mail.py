"""Functions for various email-related purposes."""

import smtplib

from constants import EMAIL_AUTH

my_address = EMAIL_AUTH['email']

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

server.login(
    EMAIL_AUTH['email'],
    EMAIL_AUTH['password']
)


def send_message(to_address, body):
    """Send an email with body "body", to address "to_address"."""
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
