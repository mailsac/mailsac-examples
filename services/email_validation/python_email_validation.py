import requests
from pprint import pprint

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/validations/addresses/jimmy@mailsac.com'

r = requests.get(url, headers=headers)
pprint(r.json())
"""
{'aliases': ['ledoktre.com',
             'totalvista.com',
             '52.41.136.113',
             'mailsac.com',
             'slothmail.net',
             'tztmax.com',
             'aiwa.fm',
             'zeie.xyz',
             'yinpinpin.club',
             'beautyoa.com',
             'lqpakswoowkw729292929292929.msdc.co'],
 'disposableDomains': ['ledoktre.com',
                       'totalvista.com',
                       'mailsac.com',
                       'slothmail.net'],
 'domain': 'mailsac.com',
 'email': 'jimmy@mailsac.com',
 'isDisposable': True,
 'isValidFormat': True,
 'local': 'jimmy'}
 """"
