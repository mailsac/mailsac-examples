.. _doc_attachments:

Email Attachments
=================

For security, and to ensure the Mailsac website is not marked as a distributor of viruses, attachments are not publicly accessible on the web.

Getting Attachments as Files
----------------------------

There are several ways to download attachments when authenticated to the Mailsac service

1. By clicking the Download button on any public message, you can open it locally in an email client and view the attachements.
2. For enhanced addresses, attachments can be downloaded in a web browser using the `Unified Inbox app <https://mailsac.com/app>`_.
3. Attachments can be downloaded using the MD5 hash of the attachment,
   `using the common-attachments API <https://mailsac.com/docs/api#tag/Email-Message-Attachments/paths/~1addresses~1{email}~1messages~1{messageId}~1attachments~1{attachmentIdentifier}/get>`_.
4. Attachments can be parsed out of the `raw` message using the `API <https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1raw~1{email}~1{messageId}/get>`_.

Additional information on reading mail, including code examples, can be found
in :ref:`Reading Email <doc_reading_mail>`.
