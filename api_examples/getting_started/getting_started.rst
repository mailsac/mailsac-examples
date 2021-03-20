.. _doc_getting_started:

.. _REST API Specification: https://mailsac.com/docs/api
.. _List Inbox Email Messages Endpoint: https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1addresses~1{email}~1messages/get
.. _Authentication Header: https://mailsac.com/docs/api#section/Auth-Option-1:-HTTP-Header
.. _Send Email Messages Endpoint: https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1outgoing-messages/post
.. _Get Message Text Endpoint: https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1text~1{email}~1{messageId}/get


REST API - Getting Started
==========================

This example will show how to do the following using the REST API.

- list emails sent to `user1@mailsac.com`
- read an email sent to `user1@mailsac.com`
- send an email from `user1@mailsac.com`

`user1@mailsac.com` can be replaced with any email address hosted by Mailsac.
If you are familiar with REST APIs the `REST API Specification`_ can be
referenced during this example.

REST API Overview
-----------------

REST API interaction is at the core of Mailsac. The examples in this section
will provide you with easy to understand curl examples. For additional code
examples (Nodejs and Python) see: :ref:`Reading Email <doc_reading_mail>`
and :ref:`Sending Mail <doc_sending_mail>`.

Prerequisites
-------------

API access is included with all Mailsac accounts. Create or view `your API key
<https://mailsac.com/api-keys>`_. Your API key will be used as the value for the
:code:`Mailsac-Key` `Authentication Header`_.

`curl <https://curl.haxx.se/>`_ is the only program used in this example. If
you are using Linux or OS X curl is likely already installed. The following
commands can be used to install curl.

.. code-block:: bash
   :caption: For operating systems using yum

   sudo yum install curl -y

.. code-block:: bash
   :caption: For operating system using apt

   sudo apt-get install curl -y

.. code-block:: bash
   :caption: For OS X

   brew install curl

.. code-block:: bash
   :caption: For Windows's Operating System using `Chocolately Nuget
       <https://chocolatey.org/>`_.

   chocolately install curl

.. tip:: `jq <https://stedolan.github.io/jq/>`_ can be used to parse JSON,
   making the output from curl pretty.

Get Mail
--------

To list the available messages for `user1@mailsac.com` we will use the
:code:`/api/addresses/:email/messages` `endpoint
<List Inbox Email Messages Endpoint_>`_. This endpoint accepts one parameter
:code:`:email`. After substituting the :code:`:email` parameter and providing
the required `Authentication Header`_, the following curl command will return
JSON.

.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Retrieve list of messages in an inbox.**
    :lines: 1


.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Inbox messages**
    :lines: 2-

The returned JSON contains metadata about the email message including to
address, from address, subject, time stamp, attachments and much more. Make note
of the `_id` field, it will be used it to view the contents of the email.

.. tip:: API documentation is generalized. Modifications are needed to translate
         an API endpoint into a usable URL. The base URI of all Mailsac API
         requests will be https://mailsac.com.

Read Mail
---------

To read an email message we will use the :code:`/api/text/:email/:messageId`
`endpoint <Get Message Text Endpoint_>`_. This endpoint
requires two parameters, :code:`:email` and :code:`:messageId`. After
substituting the :code:`:email` and :code:`:messageId` parameters and providing
the required `Authentication Header`_, the following curl command will return a
plain-text version of the message.

.. code-block:: bash
    :caption: **Retrieve text of message**

    curl -H "Mailsac-Key: YOUR_API_KEY_HERE" https://mailsac.com/api/text/user1@mailsac.com/Jn1wa9AwLigQwIbwUGyMMollJkeWSeUd-0

.. literalinclude:: text_message
    :language: text
    :caption: **Plain text email message**

The :code:`/text/` portion of the URL can be replaced with other values, to
retrieve different parsed representations of the SMTP body.

- :code:`/text/` plaintext email body, or HTML parsed to plaintext
- :code:`/raw/` entire received SMTP message including headers, body, and
  attachments
- :code:`/body/` HTML body, with images, links and scripts scrubbed
- :code:`/dirty/` HTML body, with nothing scrubbed and images inlined
- :code:`/headers/` JSON object representation of SMTP headers. The key will be
  the header key, lowercased. When there are multiple headers with the same name
  , such as :code:`Received` header, the value of the header will be an array of
  strings. Otherwise the value will be a string.

Sending Mail
-------------

.. important:: Sending messages requires the
   `purchase <https://mailsac.com/pricing>`_ of outgoing message credits,
   unless you are sending interally, within a custom domain hosted by Mailsac.

To send an email from `user1@mailsac.com` we will use the
:code:`/api/outgoing-messages` `endpoint
<Send Email Messages Endpoint_>`_. This API endpoint uses a
POST method, unlike our previous two examples, and accepts the following
parameters in a JSON body.

* :code:`Mailsac-Key` header with `your API key <https://mailsac.com/api-keys>`_
* :code:`to` address
* :code:`from` address
* :code:`subject` subject
* :code:`text` message text body

The :code:`/api/outgoing-messages` endpoint expects a JSON encoded body,
a :code:`Content-Type: application/json` header, and a `Authentication Header`_.

.. code-block:: bash
    :caption: **Send an email**

    curl -H "Content-Type: application/json" \
        -H "Mailsac-Key: YOUR_API_KEY_HERE" \
        -X POST \
        --data '{"to": "recipient@mailsac.com.com", "subject": "This is a test", "from": "my_sender@mailsac.com", "text": "This is a test"}' \
        https://mailsac.com/api/outgoing-messages
