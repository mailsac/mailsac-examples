.. _Dashboard: https://mailsac.com/dashboard
.. _`Verified Domains`: https://mailsac.com/domains
.. _amazon_dns: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html
.. _cloudflare_dns: https://support.cloudflare.com/hc/en-us/articles/360019093151
.. _namecheap_dns: https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain
.. _names_co_uk_dns: https://www.names.co.uk/support/1156-changing_your_domains_dns_settings.html
.. _wix_dns: https://support.wix.com/en/article/adding-or-updating-spf-records-in-your-wix-account

.. _doc_custom_domains:

Custom Domains
==============

Custom domains allow for receiving of email at any address within a
domain. Custom domains can be `purchased <https://mailsac.com/pricing>`_ as
an addon or as part of a plan.

Zero-Setup Subdomain
--------------------

The Zero-Setup Subdomain automatically creates a subdomain under msdc.co (eg
test123.msdc.co) that is ready to receive email with no additional setup. This
is the ideal option if you do not own a domain or do not have access to change
the DNS records for a domain.

`Zero-Setup Subdomain Configuration`_

BYODomain
---------

BYODomain (Bring Your Own Domain) allows you to easily receive email with a
domain or subdomain you already own. If you do not already own a domain you can
use our Zero-Setup Subdomain. Alternatively, you can purchase a domain from a
registrar (`Namecheap <https://namecheap.com>`__ or
`GoDaddy <https://godaddy.com>`_) and configure it for use with Mailsac.

`BYODomain Configuration`_

.. _section_zero_setup_subdomain:

Zero-Setup Subdomain Configuration
----------------------------------

Setting up a Zero-Setup domain only takes a few seconds.

#. From the Dashboard_, select `Verified Domains`_.

   .. image:: verified_domains.png
      :scale: 50%
      :align: center

#. Select "Setup a Custom Domain"

   .. image:: setup_custom_domain.png
      :width: 600px
      :align: center

#. Enter a subdomain name and select continue

   .. image:: enter_domain_name.png
      :width: 600px
      :align: center

#. Send a test email to any address at in the custom domain. There is no
   need to configure individual addresses. Sending an email to the address
   creates the address.

#. Enter the email address you sent the email to.

   .. image:: check_mail.png
      :scale: 50%
      :align: center

#. Verify the email was received.

   .. image:: verified_mail.png
      :width: 600px
      :align: center

.. _section_byod_configuration:

BYODomain Configuration
-----------------------

BYODomain configuration requires you to have access to modify DNS records on
your domain.

#. From the Dashboard_, select `Verified Domains`_.

   .. image:: verified_domains.png
      :width: 250px
      :align: center

#. Select "Setup a Custom Domain"

   .. image:: setup_custom_domain.png
      :width: 600px
      :align: center

#. Enter the fully qualified domain name of your domain

    .. image:: byod_enter_fqdn.png
       :width: 600px
       :align: center

#. Select the DNS Setup Tab to configure DNS

    .. image:: byod_select_dns.png
        :width: 600px
        :align: center

    .. note:: "Not Verified - Action Required" indicates DNS is not properly
               configured.

#. Configure TXT DNS record for DKIM

   Create a TXT record for DKIM with the hostname and value found on the DNS
   Setup page
   in the Mailsac Dashboard_.

   .. image:: byod_dkim.png
      :width: 600px
      :align: center

   .. note:: The adding of DNS records will depend on your DNS name server.
      Your IT department may be able to assist with this. If you use your domain
      registrar's name server they should have documentation on how to configure
      DNS (`Namecheap <https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain>`__
      , `Godaddy Documentation <https://www.godaddy.com/help/add-a-txt-record-19232>`_).

  =============== ==================
  DNS Provider    Documentation Link
  =============== ==================
  Amazon Route 53 `Creating Records Using the Amazon Route 53 Console <amazon_dns_>`_
  GoDaddy         `Add a TXT record <https://www.godaddy.com/help/add-a-txt-record-19232>`_
  Dreamhost       `How do I add custom DNS records <https://help.dreamhost.com/hc/en-us/articles/215414867-How-do-I-add-custom-DNS-records->`_
  Cloudflare      `Managing DNS records in CloudFlare <cloudflare_dns_>`_
  HostGator       `Manage DNS records <https://www.hostgator.com/help/article/manage-dns-records-with-hostgatorenom>`_
  Namecheap       `How do I add TXT/SPF/DKIM/DMARC records for my domain <namecheap_dns_>`_
  Names.co.uk     `Changing your domain's DNS settings <names_co_uk_dns_>`_
  Wix             `Adding or updating TXT Records in Your Wix account <wix_dns_>`_
  =============== ==================

#. Configure TXT DNS record for SPF

   Create a TXT record for SPF with the hostname and value found on the DNS
   Setup page in the Mailsac Dashboard_.

   .. image:: byod_spf.png
      :width: 600px
      :align: center

  =============== ==================
  DNS Provider    Documentation Link
  =============== ==================
  Amazon Route 53 `Creating Records Using the Amazon Route 53 Console <amazon_dns_>`_
  GoDaddy         `Adding an SPF record <https://www.godaddy.com/help/add-an-spf-record-19218>`_
  Dreamhost       `How do I add an SPF record <https://help.dreamhost.com/hc/en-us/articles/216106197-How-do-I-add-an-SPF-record->`_
  Cloudflare      `Managing DNS records in CloudFlare <cloudflare_dns_>`_
  HostGator       `SPF Records <https://www.hostgator.com/help/article/spf-records>`_
  Namecheap       `How do I add TXT/SPF/DKIM/DMARC records for my domain <namecheap_dns_>`_
  Names.co.uk     `Changing your domain's DNS settings <names_co_uk_dns_>`_
  Wix             `Adding or updating TXT Records in Your Wix account <wix_dns_>`_
  =============== ==================

#. Configure MX records to receive mail

   Create two MX records to receive mail with the hostname and value found on
   the DNS Setup page in the Mailsac Dashboard_.

   .. image:: byod_mx.png
      :width: 600px
      :align: center

   .. include:: ./mx_record_links.rst

#. Verify DNS Settings

   Click the "Query My DNS Settings Now" button to verify your DNS settings.

    .. image:: check_dns.png
       :width: 600px
       :align: center

    .. note:: DNS can take up to 24 hours to propagate

#. DNS Setup Complete

   DNS setup is complete when the status message changes to "We have verified
   that the DNS settings below were added correctly".

    .. image:: byod_dns_verified.png
       :width: 600px
       :align: center

Email can now be received and sent from your BYODomain!

