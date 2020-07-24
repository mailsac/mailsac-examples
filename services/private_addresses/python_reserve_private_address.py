import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/addresses/unitedmonkey@mailsac.com'

r = requests.post(url, headers=headers)
pprint(r.json())
'''
{'_id': 'unitedmonkey@mailsac.com',
 'catchAll': None,
 'created': '2020-07-23T15:04:15.981Z',
 'enablews': None,
 'forward': None,
 'info': '',
 'owner': 'mjmayer',
 'password': None,
 'updated': '2020-07-23T15:04:15.981Z',
 'webhook': None,
 'webhookSlack': None,
 'webhookSlackToFrom': None}
 '''
