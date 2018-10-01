.. _doc_webhook_setup:

Receive Email via JSON Webhook
==============================

Private addresses (or Catch-All addresses) can be redirected to a URL of your
choice, also called a webhook.

To enable webhooks for an email address, select Edit next to the address in the
dashboard, then enter a URL under the Forward to Webhook section, and click
Save.

.. code-block:: json

    {"text": "this is a message",
    "headers": {
         "dkim-signature": "redacted",
         "received": "2017-05-01T05:22:03.000Z",
         "content-type": "text/plain",
         "from": "mastadon@mailsac.com",
         "to": "gemini@mailsac.com",
         "subject": "",
         "message-id": "",
         "list-unsubscribe": "",
         "content-transfer-encoding": "7bit",
         "date": "Wed, 1 May 2017 05:22:03 +0000",
         "mime-version": "1.0"
    },
    "subject": "twin",
    "messageId": "MS-5412430010104145004240335343@mailsac.com",
    "priority": "normal",
    "from": [{
         "address": "mastadon@mailsac.com",
         "name": ""
    }],
    "to": [{
         "address": "gemini@mailsac.com",
         "name": ""
    }],
    "date": "2017-05-01T05:22:03.000Z",
    "receivedDate": "2017-05-01T05:22:03.000Z",
    "originalInbox": "gemini@mailsac.com",
    "inbox": "gemini@mailsac.com",
    "domain": "mailsac.com",
    "encryptedInbox": "inbox-db54b7f5f09041165aaaaae5ca9557c806cf3d95f8",
    "raw": "DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=mailsac.com;\r\n q=dns/txt; s=mailsacrelay;\r\n bh=redacted;\r\n h=from:subject:to:mime-version:content-type:content-transfer-encoding:list-unsubscribe;\r\n b=redacted\r\nReceived: from localhost (127.0.0.1) by mailer with SMTP; Wed May 1\r\n 2017 01:22:03 GMT-0400 (EDT)\r\nContent-Type: text/plain\r\nFrom: mastadon@mailsac.com\r\nTo: gemini@mailsac.com\r\nSubject: twin\r\nMessage-ID:\r\n \r\nList-Unsubscribe: \r\nContent-Transfer-Encoding: 7bit\r\nDate: Wed, 1 May 2017 05:22:03 +0000\r\nMIME-Version: 1.0\r\n\r\this is a message",
    "received": "2017-05-01T05:22:04.851Z",
    "_id": "IhnBcuaaiC",
    "ip": "127.0.0.1"
    }

Webhook contents are very similar to web `socket emails
<https://mailsac.com/docs/api/#web-socket-api>`_.

Read more about JSON Webhooks at the `API Reference
<https://mailsac.com/docs/api/#webhooks>`_
