#!/usr/bin/python3

import socket
import smtplib
from email.mime.text import MIMEText


class EmailFailureServer(Exception):
    def __init__(self, sender, destination, error):
        self.message = f'Failure trying to send email from {sender} to {destination} with ERROR message: \n'
        self.message += error
    def __str__(self):
        return self.message


def send_email(subject, body, destination, sender_name='root'):
    sender = f'{sender_name}@{socket.gethostname()}'
    message = MIMEText(body)
    message['subject'] = subject
    message['From'] = sender
    message['To'] = destination
    to = [destination]
    try:
        server = smtplib.SMTP()
        server.connect()
        server.sendmail(sender, destination, message.as_string())
        server.close()
    except Exception as ex:
        raise EmailFailureServer(sender, destination, ex)
