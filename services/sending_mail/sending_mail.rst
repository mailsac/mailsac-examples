.. _Unified Inbox: https://mailsac.com/app
.. _Dashboard: https://mailsac.com/dashboard
.. _Web Form: https://mailsac.com/compose
.. _API Key: https://mailsac.com/api-keys

.. _doc_sendingmail:

Sending Mail
============

Mail can be sent via the following methods:

- `Web Form`_
- `Unified Inbox`_
- `REST API <https://mailsac.com/docs/api/#send-email-messages>`_
- :ref:`SMTP <sec_sendingmail_smtp>`

.. _sec_send_mail_message:

Send a Mail Message
-------------------

.. tabs::
   .. tab:: Mailsac Website

      .. figure:: webform.png 

         Send using the `Compose Message Form <Web Form_>`_

   .. tab:: Unified Inbox

      .. figure:: unified_inbox_sending_mail.gif

         Send using the `Unified Inbox`_

   .. tab:: curl

       .. literalinclude:: sending_mail.sh
          :language: bash
          :caption: Send using curl

   .. tab:: Node.js Javascript 

       .. literalinclude:: sending_mail.js
          :language: javascript
          :caption: Send using Node.js. requires
                    :code:`npm install superagent`

   .. tab:: Python

       .. literalinclude:: sending_mail.py
          :language: python
          :caption: Send using Python

Allowed from addresses
----------------------
The :code:`from` address must be a :ref:`Private Address
<doc_private_addresses>` or an address within a :ref:`doc_custom_domains`.

Sending credits
---------------

Sending mail, both replies and new messages, is available only from private
addresses and private domains. Sending or replying requires `mail credits
<https://mailsac.com/pricing>`_.

Sent Messages Are Not Saved
---------------------------
Outgoing messages are not saved. They may be visible or cached temporarily by
our outgoing mail services, and logged in debugging messages on Mailsac
servers, but not explicitly archived by Mailsac at this time.

Sending from the API
--------------------

The REST API is the preferred method for sending messages programmattically.
The :code:`/api-outgoing-messages` endpoint is documented in the
`REST API documentation <https://mailsac.com/api/#send-email-messages>`_.

1. Generate an API by selecting `API Keys <https://mailsac.com/api-keys>`_ from
   the Dashboard_.
2. Send email using curl or your favorite HTTP library. :ref:`Code Examples <sec_send_mail_message>`

.. _sec_sendingmail_smtp:

Sending with SMTP
-----------------

Sending via SMTP allows email clients to send email using Mailsac.

**Authentication**

SMTP uses a username and password for authentication. The API key for your
account can be used to send from any of your private addresses or domains.
Alternatively, you can use a per private address SMTP password. The per private
address SMTP password can be set through using the Dashboard_
-> *Manage Email Addresses* -> Select the
*POP/SMTP* button next to the email address -> Select *Set New Password*

    .. figure:: pop_smtp_set_password.png
        :align: center
        :width: 400px

**Email Client Configuration**

Configure your email client (Gmail, Apple mail, Thunberbird, Outlook, iPhone,
etc) using these SMTP settings:

+-----------------------+-------------------------------------------------------+
| **Hostname / Server** | out.mailsac.com                                       |
+-----------------------+-------------------------------------------------------+
| **Email Address**     | Private email address                                 |
+-----------------------+-------------------------------------------------------+
| **Username**          + Private email address                                 |
+-----------------------+-------------------------------------------------------+
| **Password**          | `API Key`_ or SMTP Key                                |
+-----------------------+-------------------------------------------------------+
| **Port**              | 587                                                   |
+-----------------------+-------------------------------------------------------+
| **Auth Settings**     | Password / allow plain / insecure                     |
+-----------------------+-------------------------------------------------------+
| **Encryption**        | TLS                                                   |
+-----------------------+-------------------------------------------------------+

To configure a mail client for reading see the :ref:`Reading Mail via POP3 
Section <sec_reading_mail_pop3>`.

.. _doc_internal_smtp:

Internal SMTP Sending
---------------------

For `plans <https://mailsac.com/pricing>`_ with unlimited internal sending
messages can be sent through Mailsac's outbound SMTP server
(out.mailsac.com). Any messages sent to a Mailsac hosted domain will not require
sending credits.

+-----------------------+-------------------------------------------------------------------------------------------+
| **Hostname / Server** | out.mailsac.com                                                                           |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Email Address**     | Private email address or email address in a private domain                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Username**          + Private email address or email address in a private domain                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Password**          | `API Key`_                                                                                |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Port**              | 587                                                                                       |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Auth Settings**     | Password / allow plain / insecure                                                         |
+-----------------------+-------------------------------------------------------------------------------------------+
| **Encryption**        | TLS                                                                                       |
+-----------------------+-------------------------------------------------------------------------------------------+
