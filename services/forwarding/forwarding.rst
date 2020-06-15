.. _doc_mailforwarding:

Email Forwarding
================

Forwarding allows email to be sent to a different email address or
service (Webhook, Websocket, Slack Webhook). Private addresses and custom
domains can be configured for email forwarding. Forwarding is not available on
disposable email addresss.

Forward to Another Mailsac Address
----------------------------------

Any private address can be forwarded to another email private address.
This allows you to consolidate many email addresses into a single inbox.

For example, if you own 1@mailsac.com, 2@mailsac.com, 3@mailsac.com, and
main@mailsac.com, you could setup the following scheme:

* 1@mailsac.com forwards to main@mailsac.com
* 2@mailsac.com forwards to main@mailsac.com
* 3@mailsac.com forwards to main@mailsac.com
* main@mailsac.com is checked by POP3 in GMail

Catch-All Domain Forwarding Addresses
-------------------------------------
A :ref:`Catch-All email address <doc_catchall>` can receive all the mail for
a custom domain, and optionally forward it to another address or service (
Webhook, Websocket, or Slack Webhook). A Catch-All address is a private address
which in the format `*@example.com`.


Slack Email Forwarding
----------------------

Without writing any code, you can direct :ref:`inbound emails to a Slack Channel <doc_slack_webhook>`.

Slack forwarding requires a private address to be configured, but this can be a custom domain with a catch-all
private address (included with a verified custom domain).


Alternate Forwarding
--------------------

By writing a little *code*, you can forward emails to a :ref:`Webhook <doc_webhook_setup>`
or a `Web Socket
<https://mailsac.com/docs/api/#web-socket-api>`_. 
