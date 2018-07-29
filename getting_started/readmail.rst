.. _doc_readmail:

Read Mail
=========

To read a plain text email message you use the `text endpoint <https://mailsac.com/docs/api/#get-message-text>`_.
This endpoint can be accessed by :code:`GET /api/text/:email/:messageId`. You will substitue in the email address
the email was sent to and the message ID for that email. Using the values from the previous section will yield,
:code:`GET /api/text/admin%40mailsac.com:BotvTxaona7gLID1Adtpfj8Fnfi7HSSv-0`. The email message can be retrieved
using curl.

.. code-block:: bash
    :caption: **Retrieve text of message** 

    curl -s -X GET https://mailsac.com/api/text/admin%40mailsac.com/Jn1wa9AwLigQwIbwUGyMMollJkeWSeUd-0

.. literalinclude:: text_message
    :language: text 
    :caption: **Plain text message**


