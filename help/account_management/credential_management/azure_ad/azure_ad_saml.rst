
.. _doc_azure_ad_saml_configuration:

Configuring SAML SSO Between Mailsac and Microsoft Azure Active Directory
===========================================================================

Before we start, you need to ensure that you have admin rights on both Mailsac and Azure AD.

Configuring Azure AD
--------------------

1. Sign in to the Azure portal.

2. Search for and select "Azure Active Directory".

3. From the left-hand menu, choose "Enterprise applications".

   .. figure:: enterprise_applications_sidebar.png
      :align: center
      :width: 400px

      Select "Enterprise Applications" from the left-hand menu.

4. Click "New application".

   .. figure:: new_application.png
      :align: center
      :width: 400px

      Click "New application".

5. In the section page titled "Browse Azure AD Gallery" select
   "Create your own application".

   .. figure:: create_your_own_application.png
      :align: center
      :width: 400px

      Select "Create your own application".

5. In the "Add your own app" section, click on "Non-gallery application".

6. Enter a name for the application (for example, "Mailsac SSO") and click "Add".

7. On the left-hand menu of your new application, click "Single sign-on".

8. From the single sign-on method page, click "SAML".

9. The "Set up Single Sign-On with SAML" page appears. In the "Basic SAML Configuration" section, click "Edit" to open the settings. You'll need to add Mailsac's service provider (SP) URL here. This is usually something like `https://mailsac.com/sso/saml` (please verify this with Mailsac's documentation).

10. In the "User Attributes & Claims" section, you can define what user data to send to Mailsac during authentication. For example, you might want to send the user's email.

11. Save your settings.

12. In the "SAML Signing Certificate" section, download the Federation Metadata XML. We'll need this in the next step.

Configuring Mailsac
-------------------

1. Sign in to Mailsac.

2. Navigate to the SAML settings page.

3. Upload the Federation Metadata XML that you downloaded from Azure AD.

4. Save your settings.

Now, Mailsac and Azure AD should be set up for SAML SSO. Users will be able to sign in to Mailsac using their Azure AD credentials.

.. note::

   This is a simplified, high-level guide. The exact steps may vary slightly depending on the specifics of Mailsac and Azure AD's SAML support. Always refer to the official documentation for the most accurate information.

Remember to test this configuration thoroughly before deploying it to a production environment.
