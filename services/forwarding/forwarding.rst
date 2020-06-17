.. _doc_mailforwarding:
.. _Dashboard: https://mailsac.com/dashboard
.. _`Manage Email Addresses`: http://mailsac.com/addresses
.. _`Manage Domains`: http://mailsac.com/domains

Email Forwarding
================

Forwarding allows email to be sent to a different email address or
service (Webhook, WebSocket, Slack Webhook). Private addresses and custom
domains can be configured for email forwarding. Forwarding is not available on
disposable email addresss.

Forward to Another Mailsac Address
----------------------------------

Any private address, in the *@mailsac.com* domain or private domain can be
forwarded to another private address. This allows you to consolidate many email
addresses into a single inbox.

Forwarding to another private address can be configured by selecting
`Manage Email Addresses`_ from the Dashboard_. Select the *Settings* button
next to the email address to manage, then choose the private address to forward
to from the *Forward to Another Email Address* dropdown and select *Save
Settings* 

For example, if you own 1@mailsac.com, 2@mailsac.com, 3@mailsac.com, and
main@mailsac.com, you could setup the following scheme:

* 1@mailsac.com forwards to main@mailsac.com
* 2@mailsac.com forwards to main@mailsac.com
* 3@mailsac.com forwards to main@mailsac.com
* main@mailsac.com is checked by POP3 in GMail

Catch-All Domain Forwarding Addresses
-------------------------------------

A Catch-All email address can receive all the mail for
a custom domain, and optionally forward it to another address or service (
Webhook, WebSocket, or Slack Webhook). A Catch-All address is a private address
in the format `*@example.com`.

A Catch-All email address can be configured by selecting `Manage Domains`_ from
the Dashboard_, then choosing *Manage* next to the domain, and then selecting
the *Forwarding* tab.

Slack Email Forwarding
----------------------

Emails sent to a private address or Catch-All can be forwarded
:ref:`to a Slack Channel <doc_slack_webhook>`.

Slack forwarding requires a private address to be configured, but this can be 
a custom domain with a Catch-All private address (included with a verified
custom domain).

Forwarding to Slack can be configured by selecting `Manage Email Addresses`_
from the Dashboard_. Select the *Settings* button next to the email address to
manage, then input the Slack Webhook URL and select *Save Settings*.
Step-by-Step instructions are :ref:`provided <doc_slack_webhook>`.

Webhook Forwarding
------------------

Private addresses and Catch-All addresses can have their mail forwarded to a
webhook. :ref:`Configuration <doc_webhook_setup>` of the webhook only requires
a destination URL.

Forwarding to a Webhook can be configured by selecting `Manage Email Addresses`_
from the Dashboard_. Select the *Settings* button next to the email address to
manage, then input the URL under *Forward To Custom Webhook* and select *Save
Settings*.

WebSocket Forwarding
--------------------

Private addresses and Catch-All addresses can have their mail forwarded to a
WebSocket. A WebSocket uses a single persistent connection to notify a WebSocket
client as soon as a message arrives. The `WebSocket Test Page
<https://sock.mailsac.com>`_ demonstrates a WebSocket.

Forwarding to a WebSocket can be configured by selecting
`Manage Email Addresses`_ from the Dashboard_. Select the *Settings* button next
to the email address to manage, then check the box labeled *Enable forwarding
all incoming email via web socket*, and select *Save Settings*.

A code example for a WebSocket is available :ref:`available
<doc_websocket_example_overview>`.

Additional information about the WebSocket endpoint, authentication and example
frame format is show in the `API Documentation
<https://mailsac.com/docs/api/#web-socket-api>`_. 
