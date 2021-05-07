
.. _Dashboard: https://mailsac.com/dashboard
.. _`Manage Account Details`: https://mailsac.com/account
.. _`REST API`: https://mailsac.com/api
.. _`API Keys and Users`: https://mailsac.com/api-keys
.. _`Sub-Account User Login`: https://mailsac.com/login-api-key
.. _`Standard Login`: https://mailsac.com/login
.. _`Pricing`: https://mailsac.com/pricing

.. _doc_credential_management:

Credential Management
=====================

There are different ways to authenticate to Mailsac services depending
on the service being consumed.

- `Standard Login`_: Used to authenticate to Mailsac.com Website
- `Sub-Account User Login`_: Used to authenticate to Mailsac.com
  (available to `Business and Enterprise Plans <Pricing_>`_)
- `API Key <API Keys and Users_>`_: Used to authenticate to the `REST API`_,
  :ref:`Email Capture <doc_email_capture>`, :ref:`SMTP <sec_sendingmail_smtp>`,
  :ref:`POP3 <sec_reading_mail_pop3>`.
- POP3 Password: Used to authenticate to :ref:`POP3 Service <sec_reading_mail_pop3>`

.. _sec_password_change:

Password Change
---------------

An account password can be changed on the Website under
`Manage Account Details`_. If you have forgotten your password use the
`Password Reset Form <https://mailsac.com/password-reset>`_ to send a password
reset email.

Sub-Account Users will need to contact the Primary Account Holder to :ref:`reset
their password <sec_sub_account_user_password_reset>`.

.. _sec_api_key_management:

API Key Management
------------------

API keys are used to authenticate to the `REST API`_,
:ref:`Email Capture <doc_email_capture>`, :ref:`SMTP <sec_sendingmail_smtp>`,
:ref:`POP3 <sec_reading_mail_pop3>`.

API Keys can be created and deleted in the `API Keys and Users`_ section of the
Dashboard_.

Multiple API Keys
^^^^^^^^^^^^^^^^^

For accounts on Business or Enterprise plans, multiple API keys may be
created, each with a unique name.

Having multiple API keys enables:

* restricted access control
* usage monitoring
* separate API Keys for different testing environments

To create an API key, go to `API Keys and Users`_ from the Dashboard_. Enter a
name for the API Key and select *Generate new API key*. API Keys may only be
viewed once and are not retrievable by the system. API Keys should be treated
with the same security considerations as a password.

.. figure:: add_named_key.png
   :align: center
   :width: 400px

   Create new API key

.. _sec_sub_account_user:

Sub-Account Users
-----------------

Sub-Account User accounts may access a subset of Mailsac functionality
- almost everything except managing the account, billing, and API keys or
user logins. This feature is available on Business and Enterprise Plans.

A Sub-Account User's password serves both as the password to the Mailsac.com
website and the `REST API`_

Create User Login
^^^^^^^^^^^^^^^^^

User accounts can be created from the Dashboard_ under
`API Keys and Users`_.


.. figure:: create_user_login.png
   :align: center
   :width: 400px

   Create User Login

The password for the user login is automatically created. It can only
be viewed once. The credential can be downloaded as a CSV file.

.. figure:: user_login_credentials.png
   :align: center
   :width: 400px

   User Login Credentials

When logged into the website using an user login, the user session
is restricted from:

- viewing and modifying payment information
- adding or removing API keys
- managing account features
- adding or removing custom domains

Login Using an Sub-Account User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the `Sub-Account User Login`_ to sign into Mailsac to login
user a Sub-Account User

- **Primary Account ID:** The primary account name used to sign up for Mailsac
- **User Name:** The name of the user login
- **Password:** The password for the user

.. figure:: login_using_sub_account_user.png
   :align: center
   :width: 400px

   Login using a Sub-Account User.

.. _sec_sub_account_user_password_reset:

Reset Sub-Account User Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sub-Account User passwords are generated automatically because they also
serve as an API key. In order to reset the Sub-Account password the user
can be deleted and recreated. This can be done from `API Keys and Users`_
