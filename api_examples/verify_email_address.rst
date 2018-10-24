.. _doc_verify_email_address:

Verifying Email Addresses
=========================

Mailsac has two API endpoints for confirming the validity of email addresses. A single address or bulk addresses can be checked. This allows verification of an address or group of addresses without sending a mail. It helps avoid bounces.

Email validation is a useful tool for keeping invalid signups from invading your mailing list. If you run software-as-a-service, it can be used to keep users from signing up with anonymous or disposable email addresses.

Unlike our competitors, Mailsac has few limitations or costs for verifying email. You can verify single email addresses, or up to 50 at a time (more coming soon - contact support). We don't charge extra for these types of API requests.


Prerequisites
-------------
* `Node.js <https://nodejs.org/en/download/>`_
* `Mailsac API Key <https://mailsac.com/api-keys>`_

Setup
-----
Choose a folder to work in, and navigate to the folder in your terminal.

Configure the npm package.json:

.. code-block:: bash

   npm init -y
   npm install --save request request-promise-native

Single Address Validation
-------------------------

Here is an example for validating a single email address using Node.js:

.. code-block:: javascript

   const requestp = require('request-promise-native')

   const MAILSAC_API_KEY = 'YOUR API KEY GOES HERE';
   const address = process.argv[2];

   requestp(`https://mailsac.com/api/validations/addresses/${address}`, {
           json: true,
           headers: {
               'Mailsac-Key': MAILSAC_API_KEY
           },
       })
       .then((results) => {
           console.log(results[0]);
       })
       .catch((err) => {
           console.error('Something broke!', err.message, err.stack);
       });

Running it will produce output like this:

.. code-block:: bash

   $ node validate-single-email.js greg@spam.netpirates.net
   { email: 'greg@spam.netpirates.net',
     validFormat: true,
     local: 'greg',
     domain: 'spam.netpirates.net',
     isDisposable: true,
     disposableDomains: [ 'mailinator.com' ],
     aliases: [ 'mailinator.com' ] }

Bulk Address Validation
-----------------------

The bulk address validation endpoint can be used to validate up to 50 email addresses at a time. Here is an example script

.. code-block:: javascript
   
   const requestp = require('request-promise-native')

   const MAILSAC_API_KEY = 'YOUR API KEY GOES HERE';
   const addresses = process.argv.slice(2);

   requestp.post(`https://mailsac.com/api/validations/addresses`, {
           json: true,
           body: {
               emails: addresses
           },
           headers: {
               'Mailsac-Key': MAILSAC_API_KEY
           },
       })
       .then((results) => {
           console.log(results);
       })
       .catch((err) => {
           console.error('Something broke!', err.message, err.stack);
       });

Running it will produce the following output:

.. code-block:: bash

   $ node validate-multiple-emails.js greg@spam.netpirates.net jim@mailsac.com
   [ { email: 'greg@spam.netpirates.net',
       validFormat: true,
       local: 'greg',
       domain: 'spam.netpirates.net',
       isDisposable: true,
       disposableDomains: [ 'mailinator.com' ],
       aliases: [ 'mailinator.com' ] },
     { email: 'jim@mailsac.com',
       validFormat: true,
       local: 'jim',
       domain: 'mailsac.com',
       isDisposable: true,
       disposableDomains: [ 'mailsac.com', 'sanstr.com', 'totalvista.com' ],
       aliases: [ 'mailsac.com', 'sanstr.com', 'totalvista.com', '45.76.28.175' ] } ]
