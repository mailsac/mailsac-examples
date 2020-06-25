.. _doc_sendmail:

Sending Mail
============

.. important:: Sending messages requires the `purchase <https://mailsac.com/pricing>`_ of outgoing message credits, unless you are sending interally, within a custom domain you are hosting on Mailsac.

Sending an email uses the `outgoing-messages endpoint <https://mailsac.com/docs/api/#send-email-messages>`_. This 
endpoint is accessed with :code:`POST /api/outgoing-messages`. This API uses a POST method, unlike our previous 
two examples, which use GET. Several pieces of information are required to send an email.

* :code:`Mailsac-Key` header with `your API key <https://mailsac.com/api-keys>`_
* :code:`to` address
* :code:`from` address
* :code:`text` message text body

Since emails without subjects frequently get marked as spam, we are also going to include a subject in our email. Our email
message will be transmitted in JSON, therefore we must set the content type to :code:`Content-Type: application/json`.
Our message data will be a JSON object. Mailsac also supports sending raw
SMTP text through this REST API - see the REST API specification for more info.

.. code-block:: bash
    :caption: **Send an email**

    curl -H "Content-Type: application/json" \
        -H "Mailsac-Key: YOUR_API_KEY_HERE" \
        -X POST \
        --data '{"to": "recipient@mailsac.com.com", "subject": "This is a test", "from": "my_sender@mailsac.com", "text": "This is a test"}' \
        https://mailsac.com/api/outgoing-messages

