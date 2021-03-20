.. _doc_websocket:

WebSocket
=========

A Websocket provides a unique way of monitoring the incoming email of a
particular address. With a single persistent connection all content from an email
address can be forward over the Websocket. This allows your application to be notified
of an incoming emails as soon as it arrives. This helps reduce the number of API calls
and reduces latency from when the email arrives and your application responds to it.

Want to see it in action? The `WebSocket Test Page <https://sock.mailsac.com/>`_ allows
you to show how it works with no programming involved.

.. tip:: You will need an :ref:`API key <sec_api_key_management>` and a
         :ref:`private address <doc_private_addresses>` or custom domain.


.. _sec_private_address_for_websocket:

Configure Private Address for WebSocket
----------------------------------------

To use the Websocket feature a private email is required. Private addresses can
be purchased `individually <https://mailsac.com/pricing>`_ as part of a `API Developer Subscription
<https://mailsac.com/subscription>`_.

Option 1: Reserve Private Address via API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The REST API is the easiest way to reserve a private address.

A simple HTTP POST will do. Make sure you have private address credits already, from a paid plan or addon purchase.

user1@mailsac.com in the example should be replaced with the email address you wish to reserve. If you use a custom domain,
different than mailsac.com, you must have the domain configured with DNS records to delivery mail to Mailsac.

.. code-block:: bash

     curl -X POST -H "Mailsac-Key: YOUR_API_KEY_HERE" https://mailsac.com/api/addresses/user1@mailsac.com

Next, configure the private address for web socket publishing:

.. code-block:: bash

     curl -H 'Mailsac-Key: YOUR_API_KEY_HERE' -X PUT https://mailsac.com/api/private-address-forwarding/user1@mailsac.com -d '{"enablews": true}'



Option 2: Reserve Private Address in the Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `Sign in <https://mailsac.com/login>`_ to your Mailsac account.
#. Select `Manage Email Addresses <https://mailsac.com/addresses>`_ from the dropdown.

   .. image:: dashboard.png
      :scale: 50%
      :align: center


#. Select `Add Email Address <https://mailsac.com/private-address>`_ from `Manage Email Addresses <https://mailsac.com/addresses>`_

   .. image:: add_email_address.png
      :scale: 50%
      :align: center


#. Fill in the desired email address and optionally add a note.

   .. image:: add_private_email_address.png
      :scale: 50%
      :align: center


#. Select `Manage Email Addresses <https://mailsac.com/addresses>`_ and choose settings next to the email address you want to configure for Websocket.

   .. image:: configure_email.png
      :scale: 50%
      :align: center

#. Check the box to "Forward all incoming emails via web socket"

   .. image:: forward_to_web_socket.png
      :scale: 50%
      :align: center

.. _sec_websocket_receive_mail_example:

Receive Mail Using a WebSocket
-------------------------------

Receiving mail from a Websocket allows for interacting with incoming email in near real time.

WebSockets are a powerful tool allowing you to end-to-end test your application's email delivery
systems, or respond to incoming mail in sophisticated ways - without having to setup a mail server
or mess around with SMTP code.


Prerequsites
^^^^^^^^^^^^
* `Mailsac API Key <https://mailsac.com/api-keys>`_
* Node.js and npm
* :ref:`Private email address with websocket configured <sec_private_address_for_websocket>`

Setup
^^^^^

.. code-block:: bash
    :caption: **Create directory for example code**

    $ mkdir websocket-example
    $ cd websocket-example

.. code-block:: json
    :caption: **Create package.json file with the following contents**

    {
      "name": "mailsac-node-websocket-example",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "keywords": [],
      "author": "",
      "license": "MIT",
      "dependencies": {
        "ws": "^2.2.3"
      }

.. code-block:: bash
    :caption: **Install required node packages**

    npm install

.. code-block:: javascript
   :caption: **Create example.js file with the following contents**

   const WebSocket = require('ws');
   const log = console.log; // eslint-disable-line

   // Mailsac uses secure WebSockets. This is the WebSocket API base endpoint.
   const BASE_URL = 'wss://sock.mailsac.com/incoming-messages';

   // In this example, we pull the username and API key from environment variables.
   // You could also hardcode the credentials, or use a package like node-config for managing them.
   const username = process.env.MAILSAC_USER;
   const apiKey = process.env.MAILSAC_KEY;
   // List the addresses you want to receive messages for.
   // You MUST have WebSocket forwarding turned on for the addresses!
   const listenAddresses = process.env.ADDRESSES;

   const urlParams = '?_id=' + username + '&key=' +apiKey+ '&addresses=' + listenAddresses;

   log('attempting to open WebSocket to', BASE_URL + urlParams);
   const ws = new WebSocket(BASE_URL + urlParams);

   ws.on('open', function () {
     log('WebSocket opened');
   });

   ws.on('error', function (err) {
     log('connection error', err);
   });

   ws.on('message', function (data) {
     log(data);
   });


.. code-block:: bash
    :caption: **Set environmental variables**

    export MAILSAC_USER='your mailsac username / _id';
    export MAILSAC_KEY='your mailsac api key';
    export ADDRESSES='myaddress@mailsac.com,some-address@example.com'


Launch WebSocket Example
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash
    :caption: **Launch the node program**

    node example.js

.. code-block:: bash
    :caption: **Expected output**

    attempting to open WebSocket to wss://sock.mailsac.com/incoming-messages?_id=username&key=apikey&addresses=user1@mailsac.com
    WebSocket opened
    {"status":200,"msg":"Listening","addresses":["user1@mailsac.com"]}



Now, when an email messages are delivered to user1@mailsac.com, they will also be sent to your WebSocket. Try sending
a message - it will be parsed into JSON and logged to the console.


.. code-block:: json
    :caption: **Example message received over WebSocket**

    {
      "_id": "8mryf3viZQpWLX7E8SUzI3a5rEwg-0",
      "to": [
        {
          "address": "user1@mailsac.com",
          "name": ""
        }
      ],
      "from": [
        {
          "address": "from_test@mailsac.com",
          "name": ""
        }
      ],
      "subject": "This is a subject",
      "inbox": "user1@mailsac.com",
      "originalInbox": "user1@mailsac.com",
      "domain": "mailsac.com",
      "received": "2020-06-23T01:33:13.790Z",
      "raw": "Received: from 0.0.0.0 by frontend1-172-31-29-224 via 172.31.42.57 with HTTP id 8ml9bOrEQ7J_0VMd0vjPULgc for ; Tue Jun 23 2020 01:33:13 GMT+0000 (Coordinated Universal Time)\nReceived: from 0.0.0.0\n\tsmtp-in2-172-31-42-57 via 172.31.23.10 (proxy)\n\twith SMTP id 8ml9bOrEQ7J_0VMd0vjPULgc\n\tfor ; Tue, 23 Jun 2020 01:33:13 UTC\nX-Mailsac-Whitelist: user1@mailsac.com,from_test@mailsac.com,0.0.0.0\nX-Mailsac-Inbound-Version: 7463aab\nDKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=mailsac.com;\n q=dns/txt; s=mailsacrelay;\n bh=r0Rk73qDq89EuDZsfA4VqbZ/rqPclpo6FwUp6HTtsgg=;\n h=from:subject:to:mime-version:content-type:list-unsubscribe;\n b=C7leDzbCghwRfubINLbVmzTiecO/nA7zEsX0xuFJ9D8om617iGcD6q7CGysMu8jXcohxeeINI\n i2GvfKq2L7sXNPPFwBsnjGvIL8mJQYHWI+FEG3+TCnTc7ZRavKmQPAJl3B2k9QroWp5s2RyCdpJ\n vX+qjcoo7zwld6R2+C6Kmz4=\nContent-Type: multipart/alternative;\n boundary=\"----sinikael-?=_1-15928759930350.8681360034141601\"\nReceived: from frontend1-172-31-29-224 ([34.211.232.3]) with HTTP by\n cranberry; Mon Jun 22 2020 21:33:12 GMT-0400 (Eastern Daylight Time)\nReceived: from ruffrey (from_test@mailsac.com) ([76.20.5.183]) with HTTP id\n fe-vlp0jxneoa8 by frontend1-172-31-29-224 ([34.211.232.3]);\n 2020-06-23T01:33:12.177Z\nFrom: from_test@mailsac.com\nTo: user1@mailsac.com\nSubject: This is a subject\nMessage-ID: <8lncjPWgrxtLxryJG2VNSf6z@mailsac.com>\nList-Unsubscribe: \nDate: Tue, 23 Jun 2020 01:33:13 +0000\nMIME-Version: 1.0\n\n------sinikael-?=_1-15928759930350.8681360034141601\nContent-Type: text/plain\nContent-Transfer-Encoding: 7bit\n\nHere's some message text.\n\nWe are testing web sockets.\n\n------sinikael-?=_1-15928759930350.8681360034141601\nContent-Type: text/html\nContent-Transfer-Encoding: 7bit\n\n Here's some message text.\n\nWe are testing web sockets.\n \n------sinikael-?=_1-15928759930350.8681360034141601--",
      "size": 1697,
      "rtls": true,
      "ip": "0.0.0.0",
      "spam": 0.014,
      "headers": {
        "received": [
          "from 0.0.0.0 by frontend1-172-31-29-224 via 172.31.42.57 with HTTP id 8ml9bOrEQ7J_0VMd0vjPULgc for ; Tue Jun 23 2020 01:33:13 GMT+0000 (Coordinated Universal Time)",
          "from 0.0.0.0 smtp-in2-172-31-42-57 via 172.31.23.10 (proxy) with SMTP id 8ml9bOrEQ7J_0VMd0vjPULgc for ; Tue, 23 Jun 2020 01:33:13 UTC",
          "from frontend1-172-31-29-224 ([0.0.0.0]) with HTTP by cranberry; Mon Jun 22 2020 21:33:12 GMT-0400 (Eastern Daylight Time)",
          "from ruffrey (from_test@mailsac.com) ([0.0.0.0]) with HTTP id fe-vlp0jxneoa8 by frontend1-172-31-29-224 ([0.0.0.0]); 2020-06-23T01:33:12.177Z"
        ],
        "x-mailsac-whitelist": "user1@mailsac.com,from_test@mailsac.com,0.0.0.0",
        "x-mailsac-inbound-version": "7463aab",
        "dkim-signature": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=mailsac.com; q=dns/txt; s=mailsacrelay; bh=r0Rk73qDq89EuDZsfA4VqbZ/rqPclpo6FwUp6HTtsgg=; h=from:subject:to:mime-version:content-type:list-unsubscribe; b=C7leDzbCghwRfubINLbVmzTiecO/nA7zEsX0xuFJ9D8om617iGcD6q7CGysMu8jXcohxeeINI i2GvfKq2L7sXNPPFwBsnjGvIL8mJQYHWI+FEG3+TCnTc7ZRavKmQPAJl3B2k9QroWp5s2RyCdpJ vX+qjcoo7zwld6R2+C6Kmz4=",
        "content-type": "multipart/alternative; boundary=\"----sinikael-?=_1-15928759930350.8681360034141601\"",
        "from": "from_test@mailsac.com",
        "to": "jeff@mailsac.com",
        "subject": "This is a subject",
        "message-id": "<8lncjPWgrxtLxryJG2VNSf6z@mailsac.com>",
        "list-unsubscribe": "",
        "date": "Tue, 23 Jun 2020 01:33:13 +0000",
        "mime-version": "1.0"
      },
      "text": "Here's some message text.\n\nWe are testing web sockets.\n",
      "html": "<div>Here's some message text.\n\nWe are testing web sockets.</div>\n",
      "via": "172.31.42.57"
    }

The WebSocket message body is nearly identical to the
`Messages REST API <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1addresses~1{email}~1messages~1{messageId}/get>`_
with the addition of the key `"raw"` which contains the entire raw email
message received over SMTP.

Try It
^^^^^^

Visit the `Web Socket Test Page <https://sock.mailsac.com>`_ and receive emails in your web browser, without writing any code.

Troubleshooting
---------------

If the WebSocket is not working, additional debugging information is
available in :ref:`doc_recent_activity`.
