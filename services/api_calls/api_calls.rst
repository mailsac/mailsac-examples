.. _`REST API`: https://mailsac.com/api
.. _`Ops Usage`: https://mailsac.com/usage

.. _doc_api_calls:

Ops (Operations) Usage
======================

*Ops* or *Operations* are used to meter usage of the Mailsac service. Ops
usage resets on the first of the month UTC.

Ops were referred to as "api calls" until November 2021. The name was changed
to *Ops* because not all tracked operations are REST API calls.

What Counts as an Op?
---------------------------

The following actions count as one Op:

- API call to the `REST API`_
- Inbound message to a :ref:`private address <doc_private_addresses>`
- Inbound message to a :ref:`custom domain <doc_custom_domains>`
- Publish message to a :ref:`WebSocket <doc_websocket>`
- Publish message to :ref:`Webhook <doc_webhook_setup>`
- Publish message to :ref:`Slack <doc_slack_webhook>`

The following actions **do not** count as an Op:

- Viewing messages via the website
- Deleting messages via the website
- Forwarding (re-routing) mail internally to another
  :ref:`Mailsac address <sec_forward_to_another_mailsac_address>`

Monitor Ops Usage
-----------------

Ops usage can be monitored via the `Ops Usage`_ page. The page includes
current month, past usage by month, and all time usage.

Usage is not updated in real time. The metrics are calculated
periodically throughout the day.

Calculating Ops Usage
---------------------

Ops calls can be calculated by summing the number of calls to the
`REST API`_,  messages published to WebSockets, Webhooks, and Slack, and
messages sent to a private domain.

Inbound Message Ops
-------------------------

Inbound messages are tracked as Ops. The first forward of the
message to Slack, Webhook, or WebSocket does not count as an additional
Op. Second and third forwards will count as additional Ops.

Public Domain Ops
-----------------------

Validated :ref:`doc_custom_domains` can be set as public. API calls to
the domain, its addresses or messages will be tracked on the domain
owners account, not necessarily the account which performs the action.

Example Ops Calculation - Fetch Messages and Body of an Email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Viewing the body of a message via the `REST API`_ requires 2 API calls.

1. The first Op is used to
   `list all the messages in the inbox <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1addresses~1{email}~1messages/get>`_.
2. The second Op is used to
   `retrieve the plaintext body of a specific message <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1text~1{email}~1{messageId}/get>`_.

Example APOpsI Calculation - Forward Message from Private Domain to Slack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Receiving a message and publishing to Slack requires 1 Op.

1. The Op is to receive the message in a private domain.

The first forward of an inbound message to Slack, Webhook, or WebSocket
does not count as an additional Op.

Example Ops Calculation - Forward Message from Private Domain to Multiple Destinations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Receiving a message and publishing to Slack and a WebSocket
requires 2 Ops.

1. The first Op is to receive the message in a private domain.
2. The second Op is for the second message forward.

The first forward of an inbound message to Slack, Webhook, or WebSocket
does not count as an additional Op.

Example Ops Calculation - Forward message to a Private Domain Catch-All
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Receiving a message and forwarding to a Private Domain Catch-All
requires one Op.

1. Receive message in a private domain.

Catch-All addresses are considered Mailsac addresses, and internal
forwarding is not counted as an additional Op.
