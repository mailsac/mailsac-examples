.. _doc_private_address_for_websocket:

Configure Private Address for WebSocket
=======================================

To use the Websocket feature a private email is required. Private addresses can
be purchased `individually <https://mailsac.com/pricing>`_ as part of a `API Developer Subscription
<https://mailsac.com/subscription>`_. 

Option 1: Reserve Private Address via API
-----------------------------------------

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
--------------------------------------------------

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
