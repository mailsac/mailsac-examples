import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/addresses/calendartrinity@mailsac.com/messages'
r = requests.get(url, headers=headers)
message_id =  r.json()[0]['_id']
url = 'https://mailsac.com/api/text/calendartrinity@mailsac.com/' + message_id
r = requests.get(url, headers=headers)
pprint(r.text)

'''
'Dogteats are good!'
'''
