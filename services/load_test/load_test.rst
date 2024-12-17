.. _pricing: https://mailsac.com/pricing

.. _load_test:

Load Test
=========

Overview
--------

The Load Testing feature is available to subscribers of our `Business
and Enterprise plans <pricing_>`_. This feature allows you to create a
temporary domain for sending and receiving emails, enabling you to test
the performance of your sending email service.

Key details:

* **Temporary Domain**: Your load test domain becomes valid 5 minutes after creation
  and remains active for 8 hours.
* **Email Handling**: You can send emails to any address within the domain.
  Emails are counted and displayed in your dashboard.
* **Operations Limit**: Each email received counts towards your monthly
  :ref:`Operations limit<doc_api_calls>`.

This service helps customers validate the throughput of their email systems
. In the past, we discouraged using Mailsac for load testing due to the
strain on our infrastructure. The Load Testing Emails feature is
specifically designed to handle high email volumes efficiently.

Instructions
------------

Follow these steps to use the Load Testing Emails feature:

1. **Upgrade to a Business or Enterprise Plan**:
   Ensure you are subscribed to a `Business or Enterprise plan <pricing_>`_
   to access this feature.

2. **Create a New Load Test**:

   - Log in to your Mailsac account.
   - Navigate to the **Load Testing** section in the dashboard.

     .. figure:: loadtest_create_new.png
        :align: center
        :width: 400px

   - Click the **New Load Test** button.
   - A unique temporary domain will be generated. The domain becomes active
     after 5 minutes.

3. **Send Emails to the Domain**:

   - Use your email service to send messages to any address within the
     created domain.
   - Example addresses: `test1@tst-sjyupk.loadtester.msdc.co`,
     `test2@tst-sjyupk.loadtester.msdc.co`.

4. **Monitor Email Counts**:

   - Emails received will be counted and displayed in your dashboard.
   - Each email contributes to your monthly :ref:`Operations limit<doc_api_calls>`.

     .. figure:: loadtest_results.png
        :align: center
        :width: 400px

5. **Domain Expiry**:

   - The domain will automatically expire after 8 hours. No further emails
     will be accepted beyond this timeframe.

Benefits
--------

* **Efficient Testing**: Assess the speed and reliability of your email
  service under load.
* **Scalable**: Test as many emails as your :ref:`Operations limit<doc_api_calls>`
  allows during the domain's active period.

Important Considerations
------------------------

* Ensure your monthly :ref:`Operations limit<doc_api_calls>` is sufficient
  for your planned tests.
* Expired domains cannot be reactivated. Create a new domain for additional
  testing.
* This feature is for load testing purposes only and should not be used for
  standard email processing.

Need Help?
----------

If you encounter issues or have questions about the Load Testing Emails
feature, please :ref:`contact <contact_and_support>` support team for assistance.
