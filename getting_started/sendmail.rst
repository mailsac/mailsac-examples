.. _doc_sendmail:

Sending Mail
============

.. important:: Sending messages requires the `purchase <https://mailsac.com/pricing>`_ of outgoing message credits.

Sending an email uses the `outgoing-messages endpoint <https://mailsac.com/docs/api/#send-email-messages>`_. This 
endpoint is accessed with :code:`POST /api/outgoing-messages`. This API uses a POST method, unlike our previous 
two examples, which use GET. Several pieces of information are required to send an email.

* Mailsac API Key
* To address
* From address
* Text

Since emails without subjects frequently get marked as spam, we are also going to include a subject in our email. Our email
message will be transmitted in JSON, therefore we have to set the content type to ::code:`Content-Type: application/json`.
Our message data will be a comma separated key value array.

.. code-block:: bash
    :caption: **Send an email**

    curl --header "Content-Type: application/json" --request POST \
    --data '{"_mailsacKey": "eoj1mn7x5y61w0egs25j6xrvs6lwrrld0oh43rj583cgdps10tokp2ceux9s6ri8eoj1mn7x5y6", \
    "to": "recipient@gmail.com", "subject": "This is a test", "from": "sender@mailsac.com", \
    "text": "This is a test"}' https://mailsac.com/api/outgoing-messages

