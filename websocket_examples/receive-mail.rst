.. _doc_websocket_receive_mail_example:

Receive Mail Using a WebSocket
==============================

Receiving mail from a websocket allows for interacting with incomming email in near real time.

Prerequsites
-------------
* `Mailsac API Key <https://mailsac.com/api-keys>`_
* Node.js and npm
* :ref:`Private email address with websocket configured <doc_private_address_for_websocket>`

Setup
-----

.. code-block:: bash
    :caption: **Clone the example git repository and cd into the directory** 

    git clone https://github.com/ruffrey/mailsac-node-websocket-example.git
    cd mailsac-node-websocket-example

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

