.. _doc_readmail:

Read Mail
=========

To read a plain text email message you use the `text endpoint <https://mailsac.com/docs/api/#get-message-text>`_.
This endpoint can be accessed by :code:`GET /api/text/:email/:messageId`. You will substitute in the email address
the email was sent to and the message ID for that email. Using the values from the previous section will yield,
:code:`user1@mailsac.com` is the email address, and :code:`BotvTxaona7gLID1Adtpfj8Fnfi7HSSv-0` is the Mailsac messageId.

The email message can be retrieved using curl:

.. code-block:: bash
    :caption: **Retrieve text of message** 

    curl -H "Mailsac-Key: YOUR_API_KEY_HERE" https://mailsac.com/api/text/user1@mailsac.com/Jn1wa9AwLigQwIbwUGyMMollJkeWSeUd-0

.. literalinclude:: text_message
    :language: text 
    :caption: **Plain text email message**

The :code:`/text/` portion of the URL can be replaced with other values, to retrieve different parsed representations of the
SMTP body.

- :code:`/text/` plaintext email body, or HTML parsed to plaintext
- :code:`/raw/` entire received SMTP message including headers, body, and attachments 
- :code:`/body/` HTML body, with images, links and scripts scrubbed
- :code:`/dirty/` HTML body, with nothing scrubbed and images inlined
- :code:`/headers/` JSON object representation of SMTP headers. The key will be the header key, lowercased. When there are multiple headers with the same name, such as :code:`Received` header, the value of the header will be an array of strings. Otherwise the value will be a string.
