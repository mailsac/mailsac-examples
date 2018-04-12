.. _doc_yougotmail

You Got Mail!
=============

Now that curl and jq are installed we can start interacting with mailsac. The
`MailSac API Documentation <https://mailsac.com/docs/api/>`_ includes all the
endpoints supported. In this example we are going to check an abritrary email address
for mail, read that email and respond to the email.

Check Mail
----------

In this example we are going to be checking mail for the address `admin@mailsac.com`.
We will be using
the `List Inbox Email Messages <https://mailsac.com/docs/api/#list-inbox-email-messages>`_ endpoint.
Documentation shows this endpoint can be accessed with :code:`GET /api/addresses/:email/messages`. We
will substitue `:email` with `admin@mailsac.com` giving us :code:`GET /api/addresses/admin@mailsac.com/messages`.
Curl does not encode URLs for us, so the `@` character needs to be url encoded as `%40` giving us
:code:`GET /api/addresses/admin%40mailsac.com/messages`. The base URI of the mailsac API is mailsac.com, which gives
us the full URL :code:`https://mailsac.com/api/addresses/admin%40mailsac.com/messages`

.. tip:: You can validate the url is properly formatted by accessing it in your web browser. Go ahead and try it with
   our `example <https://mailsac.com/api/addresses/admin%40mailsac.com/messages>`_ or try it with a different email address.

Curl requires us to add a few extra parameters. `-X GET` instructs curl to us a HTTP GET request. `-s` supresses
a progress bar. In the command below we pipe the contents of curl into JQ for json formatting. JQ requires a filter to function.
We are using the simplest filter `"."` which matches all json.

.. literalinclude:: /about/intro_curl.bash
    :language: bash
    :lines: 1
