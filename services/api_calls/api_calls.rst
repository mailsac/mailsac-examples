.. _`REST API`: https://mailsac.com/api
.. _`API Usage`: https://mailsac.com/usage

.. _doc_api_calls:

API Calls
=========

API Calls are used to meter usage of the Mailsac service.

What Counts as an API Call?
---------------------------

The following actions count as an API call:

- API call to the `REST API`_
- Inbound message to a :ref:`private address <doc_private_addresses>`
- Inbound message to a :ref:`custom domain <doc_custom_domains>`
- Publish message to a :ref:`WebSocket <doc_websocket>`
- Publish message to :ref:`Webhook <doc_webhook_setup>`
- Publish message to :ref:`Slack <doc_slack_webhook>`

The following actions **do not** count as an API call:

- Viewing messages via the Website (using cookie authentication)
- Deleting messages via the website (using cookie authentication)
- Forwarding Mail to another
  :ref:`Mailsac address <sec_forward_to_another_mailsac_address>`

Monitor API Usage
-----------------

API usage can be monitored via `API Usage`_. The API Usage page includes
current month, past usage by month, and all time API calls.

API Usage is not updated in real time. The metrics are calculated
periodically throughout the day.

Calculating API Usage
---------------------

API calls can be calculated by summing the number of calls to the
`REST API`_,  messages published to WebSockets, Webhooks, and Slack, and
messages sent to a private domain.

Example API Calculation - Fetch Messages and Body of an Email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Viewing the body of a message via the `REST API`_ requires 2 API calls.

1. The first call is used to
   `list all the messages in the inbox <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1addresses~1{email}~1messages/get>`_.
2. The second call is used to
   `retrieve the plaintext body of a specific message <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1text~1{email}~1{messageId}/get>`_.

Example API Calculation - Forward Message from Private Domain to Slack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The receiving of a message and publishing to Slack requires 2 API calls.

1. The first call is to receive the message in a private domain.
2. The second call is to publish the :ref:`message to Slack <doc_slack_webhook>`.

Example API Calculation - Forward message to a Private Domain Catch-All
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The receiving of a message and forwarding to a Private Domain Catch-All
requires one API call.

1. Receive message in a private domain.

There is no API call required to forward a message to another Mailsac
address. Catch-All addresses are considered Mailsac addresses.
