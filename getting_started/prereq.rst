.. _doc_getting_started_prereq:

Prerequisites
=============

There are only two programs you need to get started:

* `curl <https://curl.haxx.se/>`_
* `jq <https://stedolan.github.io/jq/>`_

If you are using Linux or OS X curl is likely
already installed. The `jq download <https://stedolan.github.io/jq/download/>`_
page provides installation instructions for most operating systems.

.. code-block:: bash
   :caption: For operating systems using yum

   sudo yum install curl jq -y

.. code-block:: bash
   :caption: For operating system using apt

   sudo apt-get install jq curl -y

.. code-block:: bash
   :caption: For OS X

   brew install curl jq

.. code-block:: bash
   :caption: For Windows's Operating System using `Chocolately Nuget
       <https://chocolatey.org/>`_.

   chocolately install curl jq
