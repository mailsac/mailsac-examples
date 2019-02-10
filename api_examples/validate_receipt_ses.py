""" This script is an example of sending an email via AWS SES
and confirming its receipt using the mailsac api"""

import requests
import boto3
import time
import uuid

"""
Checks if a message from a given address in the a specific mailsac
inbox. If it is it returns when the message was recived, if not it returns
a message stating the message was not received"""


def check_received(receive_address, base_url, headers, id):
    api_url = '{0}/addresses/{1}/messages'.format(base_url, receive_address)
    response = requests.get(api_url, headers=headers)
    for message in response.json():
        if message['subject'] == str(id):
            return message['received']
    return str(receive_address + " did not receive message " + str(id))


SENDER = "Mailsac Testing <mailsac-test@mailsac.com>"
AWS_REGION = "us-west-2"
SUBJECT = "Testing email to mailsac"

API_TOKEN = ''
BASE_URL = 'https://mailsac.com/api/'

BODY_TEXT = ("Mailsac Validate Email Send\r\n"
             "This email was sent using the SES to test receipt of an email."
             )
client = boto3.client("ses", region_name=AWS_REGION)
uuids = []

for x in range(0, 100):
    id = uuid.uuid4()
    uuids.append(id)
    to_address = '{}@mailsac.com'.format(id)
    try:
        response = client.send_email(
                Destination={
                    'ToAddresses': [
                        to_address,
                        ],
                    },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': "UTF-8",
                            'Data': BODY_TEXT,
                            },
                        },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': str(id),
                        },
                    },
                Source=SENDER
                )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print('Email sent to: {}@mailsac.com'.format(str(id)))
        print('Message Id: ' + response['MessageId'])

time.sleep(30)

for x in uuids:
    print(check_received('{}@mailsac.com'.format(str(x)),
                         base_url=BASE_URL,
                         headers={'Mailsac-Key': API_TOKEN},
                         id=str(x)))
