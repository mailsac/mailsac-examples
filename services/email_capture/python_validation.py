import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/addresses/mycustomer@gmail.com/messages'

r = requests.get(url, headers=headers)
pprint(r.json())
"""
[{'_id': '9j1rpnMNc2KbgH9hzk0umIgq-0',
  'attachments': [],
  'bcc': [],
  'cc': [],
  'domain': 'gmail.com',
  'folder': 'inbox',
  'from': [{'address': 'no-reply@mywebapp.com',
            'name': 'Mywebapp Customer Support'}],
  'inbox': 'mycustomer@gmail.com',
  'ip': '98.244.15.2',
  'labels': [],
  'links': ['https://mywebapp.com/password-reset/PasswordResetToken'],
  'originalInbox': 'mycustomer@gmail.com',
  'read': None,
  'received': '2020-07-05T22:25:41.408Z',
  'rtls': True,
  'savedBy': 'mjmayer',
  'size': 603,
  'spam': 0.114,
  'subject': 'Password reset',
  'to': [{'address': 'mycustomer@gmail.com', 'name': ''}],
  'via': '172.31.27.141'}]
"""
