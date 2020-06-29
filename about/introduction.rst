.. _about_intro:

Introduction
============

With Mailsac, it is easy to interact with email via REST API, Webhooks and WebSockets. You can
reserve and release email addresses, check messages, download attachments, and route mail.

.. tip:: All REST API endpoints can be found in the `API Specification <https://mailsac.com/docs/api/>`_

--------------------------------------------

cURL REST API Example
---------------------

In this example, we are fetching messages sent to the email address
`user1@mailsac.com`.

.. literalinclude:: intro_curl.bash
    :language: bash
    :lines: 1

Information about the most recent email is returned as JSON

.. literalinclude:: intro_curl.bash
    :language: bash
    :emphasize-lines: 1
    :lines: 2-
.. tip:: This may look for more information than you need. But it provides
         a great example of all the hard work Mailsac has done to make parsing
         of email easier.
