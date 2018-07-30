.. _docs_download_all_inbox_attachments:

Download All Inbox Attachments
==============================

This is a step by step coding guide for downloading all of the attachments in a Mailsac email inbox.

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

Create a file:

.. code-block:: bash

   touch download-inbox-attachments.js


Now open the .js file and put the following code in. Change the string value of MAILSAC_API_KEY from ‘YOUR API KEY GOES HERE’ to your actual API key.

.. literalinclude:: download_all_attachments.js
   :language: javascript

The script can be run in the terminal like this:

.. code-block:: bash

   node download-inbox-attachments.js address@mailsac.com

This Node script does a few things:

#. Takes takes the email address ‘address@mailsac.com’ as an input argument. You can change this to any email address.
#. It fetches the metadata for all messages in the inbox address@mailsac.com.
#. It loops through the list of messages and prints part of the subject, the unique message identifier, and how many attachments it has.
#. When messages have attachments, the attachment is downloaded into the current folder, using it’s MD5 checksum as an identifier.

That’s it! Read more about `message attachment APIs in the docs. <https://mailsac.com/docs/api/#list-attachments-on-a-message>`_

