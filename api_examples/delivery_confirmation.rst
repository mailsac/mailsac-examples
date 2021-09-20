.. _doc_delivery_confirmation_example:

Delivery Confirmation
=====================

Consider a scenario, where you have an automated process that sends emails. You may wish to test that
this automated process is sending emails and they are being received. Mailsac provides an API so you can
check that these emails are being received.

The following code examples sends emails to user1@mailsac.com through user10@mailsac.com using an SMTP server.

Probing Specific Inboxes
------------------------

.. tabs::
   .. tab:: Python3

      .. literalinclude:: validate_receipt_smtp.py
         :language: python
   
   .. tab:: Node.js Javascript

      .. literalinclude:: validate_receipt_smtp.js
         :language: javascript
         :caption: Required libraries: 
                   :code:`npm install superagent nodemailer`
   
   .. tab:: Java

      .. literalinclude:: validate_receipt_smtp.java
         :language: java
         :caption: Required libraries: JavaMail, Unirest, Jackson
