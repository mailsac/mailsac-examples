curl -H "Mailsac-Key: YOUR_API_KEY_HERE" \
     -H "Content-Type: application/json" \
     -X PUT https://mailsac.com/api/private-address-forwarding/bclinton@mailsac.com \
     --data '{"webhook": "https://mywebsite.com/webhooks"}'

# Curl Output
{
  "_id": "bclinton@mailsac.com",
  "owner": "mailsac_user",
  "forward": null,
  "enablews": false,
  "webhook": "https://mywebsite.com/webhooks",
  "webhookSlack": null,
  "webhookSlackToFrom": null,
  "catchAll": null,
  "password": null,
  "info": "",
  "created": "2020-08-19T23:31:15.664Z",
  "updated": "2020-08-25T13:59:05.430Z"
}
