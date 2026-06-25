.. _`Mailsac SAML`: https://mailsac.com/v2/saml
.. _`API Keys and Users`: https://mailsac.com/api-keys
.. _`Entra Admin Center`: https://entra.microsoft.com/

.. _doc_azure_ad_saml_configuration:

Configuring SAML SSO Between Mailsac and Microsoft Entra
========================================================

Before we start, ensure that you have admin rights on both Mailsac and
Microsoft Entra.

Configuring Microsoft Entra
---------------------------

#. Sign in to the Entra Admin Center at `Entra Admin Center`_.

#. From the left-hand menu, choose "Enterprise apps".

   .. figure:: enterprise_applications_sidebar.png
      :align: center
      :width: 400px

      Select "Enterprise Apps" from the left-hand menu.

#. Click "New application".

   .. figure:: new_application.png
      :align: center
      :width: 400px

      Click "New application".

#. In the section page titled "Browse Microsoft Entra Gallery" select
   "Create your own application".

   .. figure:: create_your_own_application.png
      :align: center
      :width: 400px

      Select "Create your own application".

#. In the "Add your own app" section, click on "Non-gallery application".
   Enter a name for the application (for example, "Mailsac SSO") and click "Create".

   .. figure:: name_of_application.png
      :align: center
      :width: 400px

      Click "Non-gallery application".

#. On the left-hand menu of your new application, click "Single sign-on".
   From the single sign-on method page, click "SAML".

   .. figure:: sso_saml_method.png
      :align: center
      :width: 400px

      Click "Single sign-on" then "SAML".

#. The "Set up Single Sign-On with SAML" page appears. In the "Basic SAML
   Configuration" section, click "Edit" to open the settings. You'll need to
   add Mailsac's Entity ID (Identifier) and Reply URL (Assert URL), which are
   available on the `Mailsac SAML`_ page.

   .. figure:: basic_saml_configuration.png
      :align: center
      :width: 400px

      Click "Edit" in the "Basic SAML Configuration" section then add the
      Entity ID and Reply URL.

#. In the "Attributes & Claims" section, you will need to send
   the Unique User Identifier (Name ID) to Mailsac. The default for this should be
   acceptable.

   .. figure:: user_attributes_and_claims.png
      :align: center
      :width: 400px

      Click "Edit" in the "Attributes & Claims" section then add the
      Unique User Identifier (Name ID).

#. In the "SAML Certificate" section, download the SAML Certificate (Base64).
   We'll need this when configuring the Mailsac side of things.

   .. figure:: saml_certificate.png
      :align: center
      :width: 400px

      Click "Download" in the "SAML Certificate" section.

#. In the "Set up {Your Enterprise Application Name}" section, copy the
"Login URL" and "Microsoft Entra Identifier" values. We'll need these when
configuring the Mailsac to work with Entra.

   .. figure:: setup_mailsac_sso.png
      :align: center
      :width: 400px

      Copy the "Login URL" and "Microsoft Entra Identifier" values.

#. In the "Users and Groups" item in the sidebar, you can add users and groups
   that will be able to sign in to Mailsac using Microsoft Entra.

   .. figure:: users_and_groups.png
      :align: center
      :width: 400px

      Click "Users and Groups" in the sidebar.


Configuring Mailsac
-------------------

#. Sign in to Mailsac.

#. Navigate to the `Mailsac SAML`_ page.

#. Copy and paste the SAML Certificate (Base64), that you downloaded from Microsoft Entra,
   into the "Identity Provider Certs" field.

   .. figure:: identity_provider_certs.png
      :align: center
      :width: 400px

      Paste the SAML Certificate (Base64) into the "Identity Provider Certs" field.

#. Set "Name ID Format" to "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress".

   .. figure:: name_id_format.png
      :align: center
      :width: 400px

      Set "Name ID Format" to "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress".

#. In the "Identity Provider Settings", paste the "Entity ID" and "Login URL"
   from Microsoft Entra.

   .. figure:: identity_provider_settings.png
      :align: center
      :width: 400px

      Paste the "Entity ID" and "Login URL" from Microsoft Entra into the
      "Identity Provider Settings" section.

#. The final step is to add a :ref:`team user<sec_sub_account_user>`
   to Mailsac. Open the `API Keys and Users`_ page and click "Manage Users".
   Add a user with the same name as their Microsoft Entra email address.

   .. figure:: add_sub_account.png
      :align: center
      :width: 400px

      Click "Manage Users" and add a team user with the same name as their
      Microsoft Entra email address.

Now, Mailsac and Entra are configured for SAML SSO. Users will be able to
sign in to Mailsac using their Microsoft Entra credentials.
