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
- :ref:`SMTP <doc_sendingmail_smtp>`

Sending mail, both replies and new messages, is available only from private
addresses and private domains. Sending or replying requires `mail credits
<https://mailsac.com/pricing>`_.

Sent messages are not save using any method, with the exception of the Unified
Inbox.

Allowed from addresses
----------------------
When sending an email, the :code:`from` address must be a private address or an address
within a private domain.

Sending from the Web Form
-------------------------

The `Web Form`_ is the easiest way to get started
sending mail through mailsac.

#. Use the `Web Form`_ or select *Compose New Email* from the Dashboard_
#. Fill in the *From*, *To*, *Subject*, and *Text* fields
#. Click *Send*

  .. figure:: webform.png
       :align: center
       :width: 400px

Sending from the Unified Inbox
------------------------------

The `Unified Inbox`_ allows you to send and receive
like you would with gmail or yahoo mail.

1. Go to the `Unified Inbox`_ or select *Unified
   Inbox* from the Dashboard_
2. Select *compose* from the Unified Inbox

    .. figure:: unified_inbox_compose_button.png
        :align: center
        :width: 400px

3. Select the *from address* in the from dropdown, fill out the to address,
   subject, and text.

    .. figure:: unified_inbox_compose_form.png
        :align: center
        :width: 400px

4. Click *Send* to send the message.

Sending from the API
--------------------

The REST API is the preferred method for sending messages programmattically.
The :code:`/api-outgoing-messages` endpoint is documented in the
`REST API documentation <https://mailsac.com/api/#send-email-messages>`_.

1. Generate an API by selecting `API Keys <https://mailsac.com/api-keys>`_ from
   the Dashboard_.
2. Send email using curl or your favorite HTTP library.

    .. code-block:: bash
       :caption: curl

       curl -H "Mailsac-Key: MY_MAILSAC_API_KEY" -X POST
       https://mailsac.com/api/outgoing-messages
       -H "Content-Type: application/json" --data '{ "to":"myfriend@mailsac.com", "from": "user1@mailsac.com",
       "subject": "Hello Myfriend", "text": "test message from mailsac" }'

    .. code-block:: python
        :caption: Python

        import requests
        url = 'https://mailsac.com/api/outgoing-messages'
        headers = {'Mailsac-Key': 'MY_MAILSAC_API_KEY'}
        mail = { 'to':'myfriend@mailsac.com', 'from':'user1@mailsac.com', 'subject':'Hello Myfriend', 'text': 'mailsac allows for sending of email'}
        x = requests.post(url, data=mail, headers=headers)
        print(x.text)

   .. code-block:: javascript
        :caption: Node.js - requires :code:`npm install superagent`

        const superagent = require('superagent')
        superagent.post('https://mailsac.com/api/outgoing-messages')
            .set('Mailsac-Key', 'MY_MAILSAC_API_KEY')
            .send({
                to: "myfriend@mailsac.com",
                from: "user1@mailsac.com",
                subject: "Hello Myfriend",
                text: "test message from mailsac"
            })
            .ok(res => res.status === 200)
            .then(res => console.log(res.body))
            .catch(err => console.error(err))

Response example:

    .. code-block:: bash

        {
            "from": "user1@mailsac.com",
            "to": ["myfriend@mailsac.com"],
            "id": "fe-f2r4tdoe3a"
        }

.. _doc_sendingmail_smtp:

Sending with SMTP
-----------------

Sending via SMTP allows email clients to send email using mailsac.

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


Sent Messages Are Not Saved
---------------------------
Outgoing messages are not saved. They may be visible or cached temporarily by
our outgoing mail services, and logged in debugging messages on Mailsac
servers, but not explicitly archived by Mailsac at this time.

.. _doc_internal_smtp:

Internal SMTP Sending
---------------------
Mailsac's receiving SMTP servers accept all mail regardless of the
recipient. This allows customers to send directly to Mailsac using
their existing SMTP client or library. This mail is only delivered to Mailsac.
If the recipient domain is a private domain, the mail will only be visible to
the owner of the domain. If the domain is not private, the email will be publicly
accessible.

+-----------------------+-------------------------------------------------------+
| **Hostname / Server** | in.mailsac.com                                        |
+-----------------------+-------------------------------------------------------+
| **Username**          + Not required                                          |
+-----------------------+-------------------------------------------------------+
| **Password**          | Not required                                          |
+-----------------------+-------------------------------------------------------+
| **Port**              | 25                                                    |
+-----------------------+-------------------------------------------------------+
| **Auth Settings**     | Not required                                          |
+-----------------------+-------------------------------------------------------+
| **Encryption**        | None/TLS                                              |
+-----------------------+-------------------------------------------------------+

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
