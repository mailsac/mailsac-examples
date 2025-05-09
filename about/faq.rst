.. _`REST API`: https://mailsac.com/api
.. _`Unified Inbox`: https://mailsac.com/app
.. _`pricing`: https://mailsac.com/pricing
.. _api_key_login: https://mailsac.com/login-api-key
.. _`Mailsac Forum`: https://forum.mailsac.com
.. _faq:

Frequently Asked Questions
==========================

Do email addresses expire?
--------------------------

Email addresses do not expire. An address can be made private through
:ref:`Enhanced Addresses <doc_private_addresses>`. If the address is no
longer owned by a customer, it becomes a public address.

Messages have a :ref:`different retention policy <faq_message_storage>` than email addresses.

How do I delete an email address?
--------------------------------

Non-enhanced email addresses cannot be deleted. The addresses don’t exist as
separate entities within our system. Instead, we process and store individual
email messages that are sent to any address under any domain using mailsac for
their mail server. When you view what seems to be an “inbox” for an address,
it’s actually a view of the messages that were sent to that particular address.


Where are my email attachments?
-------------------------------

Email attachments are not viewable for public addresses from the Website.
Attachments must be downloaded using `REST API`_.

Attachments on emails sent to :ref:`Enhanced Addresses <doc_private_addresses>`
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

* as a developer, to test that your application is sending email
* avoid spam by keeping your real email address private
* create an account on a website without disclosing your real email address
* give it out to strangers
* use it as a shared email address
* send mail to Mailsac for QA testing purposes
* use it when you (legally) want to receive email without disclosing your identity
* send to an email address or multiple email addresses without needing to
  create them

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
2. Large message size. The max message size is 2.5MB
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

.. _faq_message_storage:

How long is email saved?
------------------------

Email messages that are sent to public domains ( ie `mailsac.com`) are retained
for 4 days and have a max number of 6 messages per inbox.

*Message storage* prevents emails from being recycled.

1. If you star a message, it will not be recycled until you unstar it.
2. Messages in enhanced addresses will not be recycled, up to your storage limit.
3. Messages on custom domains will not be recycled, up to your storage limit.

Can other people see messages that I starred?
---------------------------------------------
Nope. Only you can see them when you are logged in.


How do I reply to my Mailsac emails?
------------------------------------

Mailsac is a receive-only service.

You can use `POP3 <https://mailsac.com/docs/fetch-messages-with-pop3>`_ to
download messages on enhanced addresses or custom domains. Responses can be sent
from non-mailsac accounts you have configured your email client to use.

When does Ops/Operations/API Call Usage Reset?
-----------------------------------------------

:ref:`doc_api_calls` usage resets on the first of the Month UTC.

How can my team members see email in our private domain?
--------------------------------------------------------

For `plans <pricing_>`_ that support multiple API keys. You can
:ref:`create API keys <sec_api_key_management>` for your team members. These
name API keys can be used for API access and
`website authentication <api_key_login_>`_.

Where Can I Ask a Question About Mailsac?
-----------------------------------------

The `Mailsac Forum`_ is available to all customers, on both free and
paid plans. Questions asked of our sales and support staff are often
answered on the forums.
