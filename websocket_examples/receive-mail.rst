.. _doc_websocket_receive_mail_example:

Receive Mail Using a WebSocket
==============================

Receiving mail from a Websocket allows for interacting with incoming email in near real time.

Web sockets are a powerful tool allowing you to end-to-end test your application's email delivery
systems, or respond to incoming mail in sophisticated ways - without having to setup a mail server
or mess around with SMTP code.


Prerequsites
-------------
* `Mailsac API Key <https://mailsac.com/api-keys>`_
* Node.js and npm
* :ref:`Private email address with websocket configured <doc_private_address_for_websocket>`

Setup
-----

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


.. code-block:: javascript
   :caption: **Create example.js file with the following contents**

   const WebSocket = require('ws');
   const log = console.log; // eslint-disable-line
   
   // Mailsac uses secure web sockets. This is the web socket API base endpoint.
   const BASE_URL = 'wss://sock.mailsac.com/incoming-messages';
   
   // In this example, we pull the username and API key from environment variables.
   // You could also hardcode the credentials, or use a package like node-config for managing them.
   const username = process.env.MAILSAC_USER;
   const apiKey = process.env.MAILSAC_KEY;
   // List the addresses you want to receive messages for.
   // You MUST have web socket forwarding turned on for the addresses!
   const listenAddresses = process.env.ADDRESSES;
   
   const urlParams = '?_id=' + username + '&key=' +apiKey+ '&addresses=' + listenAddresses;
   
   log('attempting to open web socket to', BASE_URL + urlParams);
   const ws = new WebSocket(BASE_URL + urlParams);
   
   ws.on('open', function () {
     log('web socket opened');
   });
   
   ws.on('error', function (err) {
     log('connection error', err);
   });
   
   ws.on('message', function (data) {
     log(data);
   });

.. code-block:: bash
    :caption: **Install required node packages**

    npm install

.. code-block:: bash
    :caption: **Set environmental variables** 

    export MAILSAC_USER='your mailsac username / _id';
    export MAILSAC_KEY='your mailsac api key'; 
    export ADDRESSES='myaddress@mailsac.com,some-address@example.com'


Launch WebSocket Example
------------------------

.. code-block:: bash
    :caption: **Launch the node program**

    node example.js

.. code-block:: bash
    :caption: **Expected output**

    attempting to open web socket to wss://sock.mailsac.com/incoming-messages?_id=username&key=apikey&addresses=user1@mailsac.com
    web socket opened
    {"status":200,"msg":"Listening","addresses":["user1@mailsac.com"]}

    {"status":200,"msg":"ok"}


Now, when an email messages are delivered to user1@mailsac.com, they will also be sent to your web socket. Try sending
a message - it will be parsed into JSON and dumped to your console.

