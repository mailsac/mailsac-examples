.. _doc_emailhosting:

Email Hosting
=============

Mailsac will provide free email hosting for you domain. These email addresses
will be public. If you require a domain to be private or to setup forwarding of
all emails received to single address you can `sign up
<https://mailsac.com/pricing>`_ for those services.

Configure Email Hosting
-----------------------

In your domain's DNS configuration, you will need to create or modify the MX records.

============     ========    ===============
**Priority**     **Host**    **Value**
1                @           in.mailsac.com
5                @           alt.mailsac.com
============     ========    ===============

.. include:: ./private_domains/mx_record_links.rst
   :tab-width: 10