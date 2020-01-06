.. _doc_missingmail:

Missing Mail
============

If you have sent email to a @mailsac.com address or a private domain hosted
at Mailsac and it was not received, this document will help you find out why.

@mailsac.com Address
--------------------

If the address you sent to ends in *@mailsac.com* and the message was not
received it could be because:

* The sender has blocked sending to *@mailsac.com* addresses
* The message size is over 2MB
* Throttling by Mailsac. If you are sending a large volume of email, we may
  throttle the rate of incoming messages
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address has been `blacklisted
  <https://mailsac.com/docs/api/#check-blacklist>`_

Zero-Setup Private Domain (@mydomain.msdc.co)
---------------------------------------------

The Zero-Setup Private Domains handle all MX record changes so you can start
receiving email with virtually no setup. If you are still have problems
receiving mail it could be because of:

* The message size is over 2MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address has been `blacklisted
  <https://mailsac.com/docs/api/#check-blacklist>`_

Bring Your Own Domain (BYOD) Private Domain
-------------------------------------------

The BYOD Private Domain requires MX record changes. For assistance in
configuring the MX records see our :ref:`BYODomain Configuration
<section_byod_configuration>`

* MX Records are incorrect or have no propagated
* The message size is over 2MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address has been `blacklisted
  <https://mailsac.com/docs/api/#check-blacklist>`_

Custom Domain
-------------

If you have changed your MX records to use *in.mailsac.com* and
*alt.mailsac.com* and are not receiving mail. There are several potential
causes:

* MX Records are incorrect or have no propagated
* The message size is over 2MB
* The sending SMTP service has a queue
* The sending domain, IP address, or receiving address has been `blacklisted
  <https://mailsac.com/docs/api/#check-blacklist>`_