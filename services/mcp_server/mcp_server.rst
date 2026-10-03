.. meta::
   :description: The official Mailsac MCP server gives AI coding agents such as Claude Code,
      Cursor and VS Code disposable test inboxes: create an address, wait for the email,
      read its links and one-time codes.

.. _npm package: https://www.npmjs.com/package/@mailsac/mcp
.. _GitHub repository: https://github.com/mailsac/mailsac-mcp
.. _Model Context Protocol: https://modelcontextprotocol.io
.. _API keys page: https://mailsac.com/api-keys
.. _domains page: https://mailsac.com/domains
.. _pricing: https://mailsac.com/pricing

.. _doc_mcp_server:

MCP Server for AI Coding Agents
===============================

The official Mailsac MCP server (`npm package`_, `GitHub repository`_, MIT license)
connects Mailsac to AI coding agents that speak the `Model Context Protocol`_:
Claude Code, Cursor, VS Code, Claude Desktop and others. It gives the agent
disposable test inboxes, so it can check the email your application sends:
sign-up confirmations, password resets, magic links and one-time codes.

A typical request to the agent:

   Sign up for a new account on http://localhost:3000 and confirm it by email.

The agent creates a unique address, fills in the sign-up form, waits for the
confirmation email, follows the link or types the code, and reports what it found.
The same tools help it write and debug end-to-end tests for those flows.

Tools
-----

.. list-table::
   :header-rows: 1
   :widths: 25 55 20

   * - Tool
     - What it does
     - Operations used
   * - ``create_test_address``
     - Returns a new unique address, for example
       ``signup-mf3k2a1b-9c41d2@mailsac.com``. It can receive mail immediately;
       there is nothing to create first.
     - none
   * - ``wait_for_email``
     - Waits until a matching email arrives (optionally by subject, sender or
       time), then returns the subject, text, links, the most likely
       confirm/reset/login link (``actionLink``) and candidate one-time codes.
     - 1 per check, plus 1 to read
   * - ``list_emails``
     - Lists the emails stored at an address, newest first.
     - 1
   * - ``read_email``
     - Reads one email as text (with links and codes), HTML, raw MIME or headers.
     - 1
   * - ``delete_emails``
     - Deletes one email, or all emails at an address.
     - 1 per call or message
   * - ``list_domains``
     - Lists the account's private domains, for use with ``create_test_address``.
     - 1

Setup
-----

You need a Mailsac API key. The free plan works: create an account, then create
a key on the `API keys page`_. The server runs over stdio with ``npx``; Node.js 18
or newer is required.

.. tabs::
   .. tab:: Claude Code

      .. code-block:: bash

         claude mcp add mailsac -e MAILSAC_API_KEY=your-key -- npx -y @mailsac/mcp

   .. tab:: Cursor and Claude Desktop

      Cursor reads ``.cursor/mcp.json`` in the project; Claude Desktop reads
      ``claude_desktop_config.json``. Other clients that use the same format work
      the same way.

      .. code-block:: json

         {
           "mcpServers": {
             "mailsac": {
               "command": "npx",
               "args": ["-y", "@mailsac/mcp"],
               "env": { "MAILSAC_API_KEY": "your-key" }
             }
           }
         }

   .. tab:: VS Code

      Add the server to ``.vscode/mcp.json``.

      .. code-block:: json

         {
           "servers": {
             "mailsac": {
               "type": "stdio",
               "command": "npx",
               "args": ["-y", "@mailsac/mcp"],
               "env": { "MAILSAC_API_KEY": "your-key" }
             }
           }
         }

Settings
--------

.. list-table::
   :header-rows: 1
   :widths: 25 30 45

   * - Variable
     - Default
     - Purpose
   * - ``MAILSAC_API_KEY``
     - (required)
     - Your Mailsac API key.
   * - ``MAILSAC_DOMAIN``
     - ``mailsac.com``
     - Domain for new test addresses. Set it to one of your private domains.
   * - ``MAILSAC_API_URL``
     - ``https://mailsac.com/api``
     - API base URL.

Public addresses and private domains
------------------------------------

Addresses at ``@mailsac.com`` are public: anyone who guesses an address can read
its mail. They are ideal for made-up test data and need no setup, which is why the
server uses them by default. For anything real, such as a staging environment that
sends real customer names, use a :ref:`Custom Domain <doc_custom_domains>` (your
own subdomain, or a zero-setup ``yourteam.msdc.co`` subdomain from the
`domains page`_). Set ``MAILSAC_DOMAIN`` and every new address uses it. Mail to a
private domain is visible only to your account.

Operations and limits
---------------------

Each API call uses one Mailsac operation (see `pricing`_). ``wait_for_email``
checks every three seconds by default, so an email that arrives within a few
seconds costs about two to five operations. Creating an address costs nothing.
The free plan includes 1,500 operations a month; paid plans start at 25,000.

Requests from the server carry a ``Mailsac-Client: mcp`` header and a
``mailsac-mcp/<version>`` user agent. Mailsac counts these in aggregate to see how
many people use Mailsac through AI agents; email content is never part of that
count.
