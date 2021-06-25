.. _Dashboard: https://mailsac.com/dashboard
.. _deny list: https://mailsac.com/docs/api#tag/Email-Stats-API/paths/~1mailstats~1blacklist/get
.. _Support Forum: https://forum.mailsac.com

.. _doc_missingmail:

Missing Email
=============

If you have sent email to a *@mailsac.com* address or a private domain hosted
at Mailsac and it was not received, this document will help you find out why.

@mailsac.com Address
--------------------

If the address you sent to ends in *@mailsac.com* and the message was not
received it could be because of:

* The sender has blocked sending to *@mailsac.com* addresses
* Large message size. The max message size is 2.5MB
* Throttling by Mailsac. If you are sending a large volume of email, we may
  throttle the rate of incoming messages
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address is on the
  `deny list`_

Zero-Setup Private Domain (@mydomain.msdc.co)
---------------------------------------------

The Zero-Setup Private Domains handle all MX record changes. You can start
receiving email with virtually no setup. If you are still have problems
receiving mail it could be because of:

* Large message size. The max message size is 2.5MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address is on the
  `deny list`_

Bring Your Own Domain (BYOD) Private Domain
-------------------------------------------

The BYOD Private Domain requires MX record changes. For assistance in
configuring the MX records see our :ref:`BYODomain Configuration
<section_byod_configuration>`.

* MX Records are incorrect or have no propagated
* Large message size. The max message size is 2.5MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address is on the
  `deny list`_

Custom Domain
-------------

If you have changed your MX records to use *in.mailsac.com* and
*alt.mailsac.com* and are not receiving mail. There are several potential
causes:

* MX Records are incorrect or have no propagated
* Large message size. The max message size is 2.5MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address is on the
  `deny list`_

Sender Limits
-------------
Some services place restrictions on the size, type, rate, and quantity of
email that can be sent.

GMail
^^^^^
GMail is not designed for sending bulk mail. The service places `limits
<https://support.google.com/mail/answer/22839?hl=en>`_ on the number of
emails sent per day and the number of recipients.

SendGrid
^^^^^^^^
Messages sent through SendGrid are often queued and may not be sent
immediately.

Mandrill
^^^^^^^^
Messages sent through Mandrall are often `queued <https://mandrill.zendesk.com/hc/en-us/articles/205582717-Why-does-a-delivered-message-say-queued->`_
and are not sent immediately.

Request Whitelist
-----------------

Whitelisting is only necessary if mail delivery is being slowed due to Mailsac
throttling. A whitelist request can be submitted using the `IP Whitelist Form
<https://mailsac.com/whitelist-request>`_ from the Dashboard_.

Whitelisting can be requested for:

- IP addresses or networks
- Sending domains
- Sending addresses
- Receiving domains
- Receiving addresses

Contacting Support
------------------

The `Support Forum`_ is available to all customers for assistance or
questions. Customers with email support included in their plan can contact
support@team.mailsac.com.

Including the following information will help us identify why you are not
receiving mail.

* the IP address of your sending server
* the email addresses you are sending to, and/or the domain you are sending TO
* the from email addresses, and/or the domain you are sending FROM
* Time frames when messages were lost. A ball park is ok, like,
  "from 8am - 9am on Dec 3rd GMT we sent 100 messages and only 85 were received"
  or just "I tried sending 5 messages from 8am - 9am GMT Dec 3rd and none of
  them went through"
