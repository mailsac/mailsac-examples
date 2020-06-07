.. _faq:

Frequently Asked Questions
==========================

Where are my email attachments?
-------------------------------

For `private addresses, the Inbox App will allow you to download attachments <https://mailsac.com/app>`_. You can also `fetch private messages with POP3 <https://mailsac.com/docs/fetch-messages-with-pop3>`_ in your email client, such as Apple Mail or GMail.

When working with disposable email via the API, :ref:`you must download the message and parse attachments yourself <doc_attachments>`. Attachments cannot be hosted publicly for download because attachments often contain viruses and spam.

Why would I use Mailsac?
------------------------
Any time you need a temporary email address, just make one `up@mailsac.com`.

If you need to test your email system, send it to mailsac.com - even for a custom domain.

Other uses:

* if you need an email address, but do not want to receive spam in your personal inbox
* use it for sign ups on web sites that force you to login
* give it out to strangers
* use it to collaborate for projects
* send mail to Mailsac for QA testing purposes
* use it when you (legally) want to receive email without disclosing your identity
* it is perfect if you want an email address or multiple addresses and do not want to sign up for them
* comment on blogs without creating an account
* as a developer, to test that your application is sending email

.. _faq-messages-not-received:

Why weren't my messages received?
---------------------------------

There are many reasons messages may not be received or displayed by Mailsac.

The :ref:`doc_missingmail` page provides detailed explanations about why messages are not received.

Most often, the following happens:

1. The sender blocks traffic to disposable email providers like Mailsac. This is
   common with email signups or email verifications. People running websites do
   not want a bunch of spam accounts.
2. Large message size. Mailsac only supports messages up to about 2 MB.
3. Fast recycling. Without enough message storage, your inbound emails may be deleted quickly.
4. Throttling. Non-paying customers can be throttled for sending too much. We
   are happy to lift this for paying customers. Usually, it is easiest for us to
   lift it on your `Custom Domain <https://mailsac.com/domains>`_.

The Mailsac Team is highly responsive to `forum <https://forum.mailsac.com>`_ and support emails.
Contact us and we will resolve your issue.

.. tip::
  https://forum.mailsac.com

  support@team.mailsac.com

Can I use Mailsac for testing purposes?
---------------------------------------
Absolutely!

We love to hear from developers that use Mailsac - contact us anytime.


If you expect to send more than a few messages per minute, you might get throttled.


How long is email saved?
------------------------

Email messages are saved for somewhere between three days and 1 week or more, sometimes less. No guarantees!

*Message storage* prevents emails from being recycled.

1. If you star a message, it will not be recycled until you unstar it.
2. Private addresses will not be recycled, up to your storage limit.
3. Messages on custom domains will not be recycled, up to your storage limit.

Can other people see messages that I starred?
---------------------------------------------
Nope. Only you can see them when you are logged in.


How do I reply to my Mailsac emails?
------------------------------------

You must `create an account <https://mailsac.com/register>`_ to reply to emails. You'll get a few to start out, then can buy more as needed.

Or, you can use `POP3 <https://mailsac.com/docs/fetch-messages-with-pop3>`_ to download
messages on a private address or custom domain.
