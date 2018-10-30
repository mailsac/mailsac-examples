.. _doc_websocket_example_overview:

WebSocket Overview
==================

A Websocket provides a unique way of monitoring the incoming email of a 
particular address. With a single persistent connection all content from an email
address can be forward over the Websocket. This allows your application to be notified
of an incoming emails as soon as it arrives. This helps reduce the number of API calls
and reduces latency from when the email arrives and your application responds to it.

Want to see it in action? The `WebSocket Test Page <https://sock.mailsac.com/>`_ allows
you to show how it works with no programming involved.

.. tip:: You will need an `API key <https://mailsac.com/pricing>`_ and a :ref:`private address <doc_private_address_for_websocket>` 
