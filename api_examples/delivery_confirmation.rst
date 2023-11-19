.. _doc_delivery_confirmation_example:

.. _Java Example: https://github.com/mailsac/mailsac-integration-test-java
.. _Node.js Example: https://github.com/mailsac/mailsac-integration-test-examples

Delivery Confirmation Example
=============================

Consider a scenario, where you have an automated process that sends emails. You may wish to test that
this automated process is sending emails and they are being received. Mailsac provides an API so you can
check that these emails are being received.


These examples sends emails to mailsac.com using an SMTP server.

.. tabs::
   .. tab:: Node.js Javascript

       .. literalinclude:: validate_receipt_smtp.js
          :language: javascript
          :caption: Validate receipt using Node.js Javascript.
                    Full `Node.js Example`_.

   .. tab:: Python

       .. literalinclude:: validate_receipt_smtp.py
          :language: python
          :caption: Validate receipt using Python

   .. tab:: Java

          .. literalinclude:: validate_receipt_smtp.java
            :language: java
            :caption: Validate receipt using Java.
                      Full `Java Example`_.
