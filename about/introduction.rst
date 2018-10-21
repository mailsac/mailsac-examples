.. _about_intro: 

Introduction
============

With Mailsac, it's super easy to interact with email via REST API, webhooks and websockets. You can
reserve and release email addresses, check messages, download attachments, and route mail.

.. tip:: All API endpoints can be found in the `API Documentation <https://mailsac.com/docs/api/>`_

--------------------------------------------

------------
Curl Example
------------

You can use curl to view emails sent to admin@mailsac.com

.. literalinclude:: intro_curl.bash
    :language: bash
    :lines: 1

Information about the most recent email is returned as JSON

.. literalinclude:: intro_curl.bash
    :language: bash
    :emphasize-lines: 1
    :lines: 2-35,49-51
.. tip:: This may look for more information than you need. But it provides
         a great example of all the hard work mailsac has done to make parsing
         of email easier.
