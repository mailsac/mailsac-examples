.. _doc_delivery_confirmation_example:

Delivery Confirmation Example
=============================

Consider a scenario, where you have an automated process that sends emails. You may wish to test that
this automated process is sending emails and they are being received. Mailsac provides an API so you can
check that these emails are being received.

Prerequisites
-------------
* Python3
* `Mailsac API Key <https://mailsac.com/api-keys>`_


This python example sends emails to user1@mailsac.com through user10@mailsac.com using an SMTP server. Your
mail server may or may not use authentication, in this example we are using authentication with TLS.

.. literalinclude:: validate_receipt_smtp.py
   :language: python
