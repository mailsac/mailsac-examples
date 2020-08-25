import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/private-address-forwarding/bclinton@mailsac.com'
data = { 'webhook':'https://mywebsite.com/webhooks' }

r = requests.put(url, data=data, headers=headers)
pprint(r.json())
'''
{'_id': 'bclinton@mailsac.com',
 'catchAll': None,
 'created': '2020-08-19T23:31:15.664Z',
 'enablews': False,
 'forward': None,
 'info': '',
 'owner': 'mailsac_user',
 'password': None,
 'updated': '2020-08-25T14:11:14.695Z',
 'webhook': 'https://mywebsite.com/webhooks',
 'webhookSlack': None,
 'webhookSlackToFrom': None}
 '''
