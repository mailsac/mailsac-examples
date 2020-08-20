import requests
from pprint import pprint

message_id = 'YOUR_MESSAGE_ID'
headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/addresses/bclinton@mailsac.com/messages/' + message_id
r = requests.delete(url, headers=headers)
pprint(r.json())

'''
{'_id': '4xnxBtJpZxLQTU2MvcIPD65cdWQC-0',
 'inbox': 'bclinton@mailsac.com',
 'message': 'Message was deleted.'}
'''
