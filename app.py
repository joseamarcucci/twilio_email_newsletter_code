# Test integration code provided by Twilio Sendgrid
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='info@clayss.org',
    to_emails='jmarcucci@usal.edu.ar',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
