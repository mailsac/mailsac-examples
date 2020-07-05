.. _doc_direct_deliver:

Direct Delivery
===============

Direct Delivery is the service that allows Mailsac to act as a fake SMTP
server. Email messages sent using direct delivery will not be delivered to
the intended recipients but instead will be available in Mailsac.

Direct Delivery Example in a Non-Production Environment
----------------------------------------------------------

Non-production environments of applications often do not send email for fear
that non-production systems may send email to a customer. Using Direct Delivery
emails can be sent and verified using customer email addresses, without the
customer receiving the email.

.. tabs::
   .. tab::  Python

      .. literalinclude:: direct_delivery_example.py
         :language: python

   .. tab:: Javascript

      .. literalinclude:: direct_delivery_example.js

Traditional Email Flow
----------------------

The basic components involved when sending email are:

* Mail User Agent (end user email client)
* Mail Transfer Agent (transfers email messages between servers. May also
  receive email from email clients)
* Mail Delivery Agent (receives mail from a mail transfer agent)
