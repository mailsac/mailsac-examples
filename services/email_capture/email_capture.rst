.. _doc_email_capture:

.. _Mailsac website: https://mailsac.com
.. _Mailsac API: https://mailsac.com/api

Email Capture
===============

Email Capture is the service that allows Mailsac to act as a fake SMTP
server. Email messages sent using Email Capture will not be delivered to
the intended recipients but instead will be available via the `Mailsac website`_
and `Mailsac API`_.

Email Validation in a Non-Production Environment
------------------------------------------------

Non-production environments of applications often do not send email for fear
that non-production systems may send email to customers. Using Email Capture,
emails can be sent and verified using customer email addresses, without the
customer receiving the email.

Sending with Email Capture
^^^^^^^^^^^^^^^^^^^^^^^^^^

To configure applications to use Email Capture replace existing
SMTP configuration with these settings.

- Server Name: `capture.mailsac.com`
- Port: 5587
- Use Secure Connection: Yes (TLS)
- User Authentication: No

.. tabs::
   .. tab:: Node.js Javascript

      .. pygments throws error because of the \r\n in the code example use force
      .. literalinclude:: email_capture_example.js
         :language: javascript
         :force:
         :caption: Send email using Email Capture

   .. tab::  Python

      .. literalinclude:: email_capture_example.py
         :language: python
         :caption: Send email using Email Capture

Validate Email Was Received
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to check that an email was received is to use the `Mailsac
website`_. Use the "Check the mail!" button on the
homepage of the `Mailsac website`_ to view the inbox that the email was sent to.

.. figure:: check_customer_mail.png
   :align: center
   :width: 400px

   Check any inbox from the Mailsac homepage

Validating an email was received can also be done using any programming
language that supports HTTP requests, in combination with the `Mailsac API`_.
Code examples for Javascript and Python
are provided.

.. tabs::
   .. tab:: Mailsac Website

      .. figure:: mycustomer_at_gmail.png

         Validate email was received

   .. tab:: curl

       .. literalinclude:: curl_validation.txt
          :language: bash
          :caption: Validate email was received

   .. tab:: Node.js Javascript 

       .. literalinclude:: javascript_validation.js
          :language: javascript
          :caption: Validate email was received

   .. tab:: Python

       .. literalinclude:: python_validation.py
          :language: python
          :caption: Validate email was received

Traditional Email Flow
----------------------

Email traditionally flows from an email client (Mail User Agent - MUA), to a
outbound SMTP server (Mail Transfer Agent - MTA), to the receiving SMTP server
(also an MTA), then to a Mail Delivery Agent (MDA), which is polled by the email
client (MUA) using POP3 or IMAP.

.. figure:: email_flow.svg
   :width: 600px
   :align: center

   By Polluks - eigene Arbeit, ArgoUML, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=3645799

Along the way, there are typically several places where authentication and
integrity are verified. A sender is typically authenticated when connecting to
an outbound SMTP server. The receiving MTA
will use SPF records, to validate that the sending MTA is allowed to send the
mail, and DKIM records to validate the integrity of the email. Finally, the MUA
authenticates against the MDA, typically using a username and password.

Email Capture Flow
-------------------

In the Email Capture model the Mail User Agent uses Mailsac's receiving Mail
Transfer Agent as the outbound MTA. The Mailsac MTA will accept all mail,
regardless of the destination domain.

Considerations
--------------

- All email sent will be public (Unless sent to a :ref:`private domain
  <doc_privatedomains>`)
- Email will be throttled
