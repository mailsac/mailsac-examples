import requests

headers = {'Mailsac-Key': 'YOUR_API_KEY_HERE'}
url = 'https://mailsac.com/api/addresses/bclinton@mailsac.com/messages'
r = requests.delete(url, headers=headers)
print(r.status_code)

'''
204
'''
