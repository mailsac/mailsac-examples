.. _doc_emailhosting:

Email Hosting
=============

Mailsac can host **free** disposable email for your existing custom domain. The email addresses
and messages will be public.

If you require a email messages to be private, or to setup forwarding of
all emails received to single address, you can `subscribe
<https://mailsac.com/pricing>`_ for those services.

.. _section_email_hosting:

Configure Email Hosting
-----------------------

In your domain's DNS configuration, you will need to create or modify the MX records (for public and private).

============     ========    ===============
**Priority**     **Host**    **Value**
1                @           in.mailsac.com
5                @           alt.mailsac.com
============     ========    ===============

Common DNS Provider Links
-------------------------

.. rst-class:: blockquote-noleftmargin
.. include:: ./custom_domains/mx_record_links.rst
