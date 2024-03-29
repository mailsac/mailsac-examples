.. _doc_mailredirect:
.. _message_data: https://mailsac.com/docs/api#tag/Email-Messages-API/paths/~1addresses~1{email}~1messages~1{messageId}/get

Mail Redirection
================

Mailsac offers two types of mail redirection or aliasing.

- :ref:`sec_alternate_addressing`
- :ref:`sec_plus_addressing`

.. _sec_alternate_addressing:

Alternate Addressing
====================

One of the downsides of public disposable email is that when you give out the
address, and people know it is disposable, they might know they can view your
mail!

But there’s a way around that. You can still keep your inbox private.

The 'redirect' or 'alternate' Address
-------------------------------------

Underneath each email address, on the main inbox page, is a special redirect
address.

The alternate email address begins with“**inbox**-“ and has a long string of
characters after it.

Any mail sent to the alternate/redirect address will be delivered to the actual address on the page.

**Redirect emails work for custom domains** as well. The alternate address will
always display the domain as “@mailsac.com” – which will work – **but you can
also change the domain to your custom domain (or any domain** that receives
mail at Mailsac).

For example, if the alternate address for your email, dude@example.com is
inbox-55443445kk4Knxns@mailsac.com, you can use that one, or replace the domain
with your own. It would be inbox-55443445kk4Knxns@example.com.

Of course, Mailsac offers private inboxes, too. If you `create an account
<https://mailsac.com/register>`_,
you’ll be able to see the options for getting private mail. Then you can give
out your actual email address without worrying whether people know it is
public.

.. _sec_plus_addressing:

Plus-addressing
---------------

When you send email to any mailsac hosted domain, if a :code:`+` plus
symbol is included in the local-part of the address, it is removed as
well as anything up to the the :code:`@` symbol.

For example:

.. code-block:: bash

   jeff+12345asdf@mailsac.com

will be delivered to

.. code-block:: bash

   jeff@mailsac.com

The original :code:`To` email address is stored in the property
:code:`originalInbox` and is accessible using the
`Message Data REST API endpoint <message_data_>`_.

Many email services including Gmail, iCloud and Fastmail support
stripping the + plus symbol and everything after it in the local-part of
the address (everything before the :code:`@` symbol).
