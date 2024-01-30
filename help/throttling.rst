
.. _doc_smtp_throttling:

Email Throttling
================

Messages sent to custom domains and enhanced addresses, held by customers
on a paid plan, are throttled differently than messages sent to public
addresses in the mailsac.com domain.

Throttling of messages on custom domains and enhanced addresses will
likely be completely unnoticed by customers, with the exception of
customers who are sending messages at the rate of thousands per minute.

All emails received by Mailsac are subject to throttling to ensure system
availability for all customers, both paying and free.

Throttling on Public / Unowned Domains
--------------------------------------

Messages sent to public / unowned domains have a lower threshold for
throttling. This includes public @mailsac.com addresses and domains
that have been configured to deliver mail to Mailsac, but are :ref:`not
verified <doc_custom_domains>`.

To increase the throttling threshold an :ref:`Enhanced Address <doc_private_addresses>`
or :ref:`Verified Custom Domain <doc_custom_domains>` should be be used.

Throttling on Enhanced Addresses or Custom Domains
-------------------------------------------------

Most customers sending to :ref:`Enhanced Addresses <doc_private_addresses>`
or a :ref:`Verified Custom Domain <doc_custom_domains>` will never
experience throttling.

How do I know if I'm Being Throttled?
-------------------------------------
There are two stages to throttling.

1. Message deliver is slowed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During this stage messages are processed increasingly slower based on
the number of emails received. This stage is done without customer notification.

In a worse case scenario, this will result in messages being delayed
about 1 minute.

2. Mailsac SMTP server returns a 421 error message
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A 421 error message indicates the number of messages received has exceeding the
throttling limits and message delivery will need to be retried at a later time.
