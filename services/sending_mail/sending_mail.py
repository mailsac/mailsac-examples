import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/outgoing-messages'
mail = { 'to':'myfriend@mailsac.com',
         'from':'user1@mailsac.com',
         'subject':'Hello Myfriend',
         'text': 'mailsac allows for sending of email'
       }

r = requests.post(url, data=mail, headers=headers)
pprint(r.json())
'''
{'from': 'user1@mailsac.com',
 'id': 'fe-tgitrk8dbga',
 'to': ['myfriend@mailsac.com']}
'''
