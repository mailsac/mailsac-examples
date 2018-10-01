.. _doc_emailhosting:

Email Hosting
=============

Mailsac will provide free email hosting for you domain. These email addresses
will be public. If you require a domain to be private or to setup forwarding of
all emails received to single address you can `sign up
<https://mailsac.com/pricing>`_ for these services.

Configure Email Hosting
-----------------------

In your domains DNS configuration you will need to create or modify the MX records.

============     ========    ===============
**Priority**     **Host**    **Value**
1                @           in.mailsac.com
5                @           alt.mailsac.com
============     ========    ===============
