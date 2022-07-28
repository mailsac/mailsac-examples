""" This script is an example of sending an email via smtp
and confirming its receipt using the mailsac api"""

import time
import sys
import smtplib
import email.utils
import requests
from email.mime.text import MIMEText

"""
Checks if a message from a given address in the a specific mailsac
inbox. If it is it returns when the message was recived, if not it returns
a message stating the message was not received"""
def check_received(receive_address, send_address, base_url, headers):
    api_url = '{0}addresses/{1}/messages'.format(base_url, receive_address)
    response = requests.get(api_url, headers=headers)
    for message in response.json():
        if message['from'][0]['address'] == send_address:
            return message['received']
        return '{0} has not received an email from {1}'.format(receive_address, send_address)


SMTP_USERNAME = 'mysmtp_user'
SMTP_PASSWORD = 'mysmtp_password'
SMTP_SERVER = 'mysmtp_server.company.com'
SMTP_PORT = 587
FROM_ADDRESS = 'myuser@company.com'
FROM_NAME = 'MyTest User'
SUBJECT = "Testing email to mailsac"

API_TOKEN = 'MY_API_TOKEN_FROM_MAILSAC'
BASE_URL = 'https://mailsac.com/api/'

BODY_TEXT = ("Mailsac SMTP Validate Email Send\r\n"
             "This email was sent using the SMTP to test receipt of an email."
            )

for x in range(1, 10):
    try:
        to_address = 'user{}@mailsac.com'.format(x)
        msg = MIMEText(BODY_TEXT)
        msg['Subject'] = SUBJECT
        msg['From'] = email.utils.formataddr((FROM_NAME, FROM_ADDRESS))
        msg['To'] = to_address

        conn = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        conn.set_debuglevel(True)
        conn.ehlo()
        conn.starttls()
        conn.ehlo()
        conn.login(SMTP_USERNAME, SMTP_PASSWORD)
        try:
            conn.sendmail(FROM_ADDRESS, to_address, msg.as_string())
            conn.close()
        except Exception as e:
            print("Error: ", e)
        else:
            print("Email Sent!")
    except Exception as ex:
        print(ex)

time.sleep(30)

for x in range(1, 10):
    print(check_received('user{}@mailsac.com'.format(x), send_address=FROM_ADDRESS,
                      base_url=BASE_URL, headers={'Mailsac-Key': API_TOKEN}))
