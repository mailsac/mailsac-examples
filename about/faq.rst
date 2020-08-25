.. _`REST API`: https://mailsac.com/api
.. _`Unified Inbox`: https://mailsac.com/app

.. _faq:

Frequently Asked Questions
==========================

Where are my email attachments?
-------------------------------

Email attachments are not viewable for public addresses from the Website.
Attachments must be downloaded using `REST API`_.

Attachments on emails sent to :ref:`Private Addresses <doc_private_addresses>`
can be viewed in the `Unified Inbox`_ or in an email client using
:ref:`POP3 <sec_reading_mail_pop3>`.

:ref:`Read more about email attachments at Mailsac
<sec_reading_mail_attachments>`.

Why would I use Mailsac?
------------------------
Any time you need a temporary email address, just make one `up@mailsac.com`.

If you need to test your email system, send it to mailsac.com - even for a
custom domain.

Other uses:

* avoid spam by keeping your real email address private
* create an account on a website without disclosing your real email address
* give it out to strangers
* use it as a shared email address
* send mail to Mailsac for QA testing purposes
* use it when you (legally) want to receive email without disclosing your identity
* send to an email address or multiple email addresses without needing to
  create them
* as a developer, to test that your application is sending email

.. _faq-messages-not-received:

Why weren't my messages received?
---------------------------------

There are many reasons messages may not be received or displayed by Mailsac.

The :ref:`doc_missingmail` page provides detailed explanations about why
messages are not received.

Most often, the following happens:

1. The sender blocks traffic to disposable email providers like Mailsac. This
   is common with email signups or email verifications. People running websites
   do not want a bunch of spam accounts.
2. Large message size. Mailsac only supports messages up to about 2 MB.
3. Fast recycling. Without enough message storage, your inbound emails may be
   deleted quickly.
4. Throttling. Non-paying customers can be throttled for sending too much. We
   are happy to lift this for paying customers.
   `Custom Domain <https://mailsac.com/domains>`_ are not throttled.

The Mailsac Team is highly responsive to `forum <https://forum.mailsac.com>`_
and support emails. Contact us and we will resolve your issue.

.. tip::
  https://forum.mailsac.com

  support@team.mailsac.com

Can I use Mailsac for testing purposes?
---------------------------------------
Absolutely!

We love to hear from developers that use Mailsac - contact us anytime.

Throttling may occur when sending. Avoid throttling by using a
`Custom Domain <https://mailsac.com/domains>`_


How long is email saved?
------------------------

Email messages that are sent to public domains ( ie `mailsac.com`) are retained
for 4 days and have a max number of messages per inbox of 6 days.

*Message storage* prevents emails from being recycled.

1. If you star a message, it will not be recycled until you unstar it.
2. Private addresses will not be recycled, up to your storage limit.
3. Messages on custom domains will not be recycled, up to your storage limit.

Can other people see messages that I starred?
---------------------------------------------
Nope. Only you can see them when you are logged in.


How do I reply to my Mailsac emails?
------------------------------------

You must `create an account <https://mailsac.com/register>`_ to reply to
emails. New accounts have 5 sending credits. Additional credits can be
`purchased <https://mailsac.com/pricing>_`.

You can use `POP3 <https://mailsac.com/docs/fetch-messages-with-pop3>`_ to
download messages on a private address or custom domain. Responses can be sent
from non-mailsac accounts you have configured your email client to use.
