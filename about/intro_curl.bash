curl -H 'Mailsac-Key: YOUR_API_KEY_HERE' https://mailsac.com/api/addresses/user1@mailsac.com/messages | jq .

[{
  "_id": "BotvTxaona7gLID1Adtpfj8Fnfi7HSSv-0",
  "from": [
    {
      "address": "microsoftstore@e.microsoft.com",
      "name": "Microsoft Store"
    }
  ],
  "to": [
    {
      "address": "user1@mailsac.com",
      "name": ""
    }
  ],
  "cc": null,
  "bcc": null,
  "subject": "Ahoy, Sea of Thieves for PC is here",
  "savedBy": null,
  "originalInbox": "inbox-c942bfeeafb96c0e5ce8b4e5c0d747c608@mailsac.com",
  "inbox": "user1@mailsac.com",
  "domain": "mailsac.com",
  "received": "2018-03-29T18:28:07.732Z",
  "size": 23420,
  "attachments": ["c830ee26e0a326e0a30c585494793479"],
  "ip": "65.55.234.211",
  "via": "144.202.71.79",
  "folder": "inbox",
  "labels": [],
  "read": null,
  "rtls": true,
  "links": [
    "https://support.xbox.com/games/game-titles/xbox-play-anywhere-help",
    "https://e.microsoft.com/Key-3567701.C.CQZpy.J.K0.-.CpMBp0",
    "https://account.microsoft.com/profile/unsubscribe?CTID=0&ECID=jIce0uXtDC5qRlyCYqZsz5yCL"
  ],
  "spam": 0.331
}]
