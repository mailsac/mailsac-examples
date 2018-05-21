.. _doc_yougotmail

You Got Mail!
=============

Now that curl and jq are installed, we can start interacting with mailsaci API. The
`MailSac API Documentation <https://mailsac.com/docs/api/>`_ includes all supported
endpoints. The API documentation is great starting place, if you a familiar with
REST APIs or for reference after completing this step-by-step introduction.

In this example, we are going to check an abritrary email address
for mail, read that email and respond to the email.

Check Mail
----------

In this example, we will list inbox email messages for `admin@mailsac.com`.
To list the available messages we will use the 
`List Inbox Email Messages endpoint <https://mailsac.com/docs/api/#list-inbox-email-messages>`_.
This endpoint can be accessed with :code:`GET /api/addresses/:email/messages`. You 
will substitue `:email` with `admin@mailsac.com` giving us :code:`GET /api/addresses/admin@mailsac.com/messages`.
Curl does not encode URLs. The `@` character needs to be url encoded as `%40`. 
:code:`GET /api/addresses/admin%40mailsac.com/messages`. The base URI of the mailsac API is mailsac.com, which 
translates to :code:`https://mailsac.com/api/addresses/admin%40mailsac.com/messages`

.. tip:: You can validate the url is properly formatted by accessing it in your web browser. Go ahead and try it with
   our `example <https://mailsac.com/api/addresses/admin%40mailsac.com/messages>`_ or try it with a different email address.

Curl requires us to add a few extra parameters. `-X GET` instructs curl to us a HTTP GET request. `-s` supresses
a progress bar. In the command below we pipe the contents of curl into JQ for json formatting. JQ requires a filter to function.
We are using the simplest filter `"."` which matches all json. `admin@mailsac` is a popular address and receives lots of email. 
JQ will only show the first json object with the filter `".[0]"`

.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Retrieve first email in a an inbox.**
    :lines: 1


.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Inbox message**
    :emphasize-lines: 1
    :lines: 2-35,49-51

As you can see, the JSON contains information about the email message including  to address,
from address, subject, timestamp, attachments and much more. Make note of the `_id` field, you
will use it to view the contents of the email.

Read Mail
---------

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


