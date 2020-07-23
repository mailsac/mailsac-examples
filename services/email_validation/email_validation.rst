.. _doc_email_validation:

.. _Mailsac website: https://mailsac.com/email-validation

Email Validation
================

Email validation confirms that the provided email address is in a valid format
and the email address is not associated with a disposable email service.
Validations can be done using the `Mailsac website`_ or REST API.

Additional information about the REST API endpoint for Email Validation
is available in the `REST API Documentation
<https://mailsac.com/docs/api/#email-validations-api>`_. The REST API endpoint
supports bulk validation of up to 50 email addresses.

Examples
--------

.. tabs::
   .. tab:: Mailsac Website

      .. figure:: website_email_validation.gif
         
         Email validation using the `Mailsac website`_

   .. tab:: curl

      .. literalinclude:: curl_email_validation.txt
         :language: bash
         :caption: Validate email address

   .. tab:: Node.js Javascript

      .. literalinclude:: nodejs_email_validation.js
         :language: javascript
         :caption: Validate email address

   .. tab:: Python

      .. literalinclude:: python_email_validation.py
         :language: python 
         :caption: Validate email address
