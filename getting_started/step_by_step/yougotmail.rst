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
Using curl we need to do a little bit of manual formatting of the API URL.
