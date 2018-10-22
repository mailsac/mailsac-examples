.. _doc_checkmail:

Check Mail
=============

Now that curl and jq are installed, we can start interacting with Mailsac API. The
`MailSac API Documentation <https://mailsac.com/docs/api/>`_ includes all supported
endpoints. The API documentation is great starting place, if you a familiar with
REST APIs or for reference after completing this step-by-step introduction.

In this example, we are going to check an arbitrary email address
for mail, read that email and respond to the email.

In this example, we will list inbox email messages for `user1@mailsac.com`.
To list the available messages we will use the 
`List Inbox Email Messages endpoint <https://mailsac.com/docs/api/#list-inbox-email-messages>`_.

.. tip:: API documentation is generalized. Modifications are needed to translate an API endpoint
   into a usable URL. The base URI of all MailSac API requests will be https://mailsac.com. 

This endpoint can be accessed with :code:`GET /api/addresses/:email/messages`. You 
will substitute `:email` with `user1@mailsac.com` giving us :code:`GET /api/addresses/user1@mailsac.com/messages`.
Curl does not encode URLs. The `@` character needs to be URL encoded as `%40`. 
:code:`GET /api/addresses/user1%40mailsac.com/messages`. The base URI of the Mailsac API is Mailsac.com, which 
translates to :code:`https://mailsac.com/api/addresses/user1%40mailsac.com/messages`

.. tip:: You can validate the url is properly formatted by accessing it in your web browser. Go ahead and try it with
   our `example <https://mailsac.com/api/addresses/user1%40mailsac.com/messages>`_ or try it with a different email address.

Curl requires us to add a few extra parameters. `-X GET` instructs curl to us a HTTP GET request. `-s` suppresses
a progress bar. In the command below we pipe the contents of curl into JQ for JSON formatting. JQ requires a filter to function.
We are using the simplest filter `"."` which matches all JSON. `user1@mailsac` is a popular address and receives lots of email. 
JQ will only show the first JSON object with the filter `".[0]"`

.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Retrieve first email in a an inbox.**
    :lines: 1


.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :caption: **Inbox message**
    :lines: 2-35,49-51

As you can see, the JSON contains information about the email message including  to address,
from address, subject, time stamp, attachments and much more. Make note of the `_id` field, you
will use it to view the contents of the email.
