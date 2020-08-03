curl -H "Mailsac-Key: YOUR_API_KEY_HERE" -X POST \
https://mailsac.com/api/outgoing-messages \
-H "Content-Type: application/json" --data '{ "to":"myfriend@mailsac.com", "from": "user1@mailsac.com", "subject": "Hello Myfriend", "text": "test message from mailsac" }'

# Response
{
  "from": "user1@mailsac.com",
  "to": [
    "myfriend@mailsac.com"
  ],
  "id": "fe-3hl55xcrzgr"
}
