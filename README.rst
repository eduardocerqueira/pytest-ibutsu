Ibutsu pytest Plugin
====================

This is a plugin that will report test rests from pytest to an Ibutsu server.

Requirements
------------

Python 2.7 and 3.6+

Installation
------------

Install the plugin via ``pip``::

    pip install pytest-ibutsu

If you're developing this plugin, you can create an editable installation::

    pip install -e .

Getting Started
---------------

To push your results to the Ibutsu server, use the ``--ibutsu`` option with the URL to your server::

    pytest --ibutsu http://ibutsu/


Alternatively, pytest-ibutsu can upload the test artifact to S3 bucket::

    pytest --ibutsu s3

just remember to load AWS environment variables before using s3 method::

    export AWS_ACCESS_KEY_ID=************
    export AWS_SECRET_ACCESS_KEY=************
    export AWS_DEFAULT_REGION=************
    export AWS_S3_SECURE_CONNECTION=True

Authentication
--------------

To authenticate against your Ibutsu server, use the ``--ibutsu-token`` option with a token from your
Ibutsu server. Go to your profile page, select tokens, and generate a token there. Copy and paste
the JWT token generated into this option::

    pytest --ibutsu http://ibutsu/ --ibutsu-token eyJhbGci.......CA1opEQ

More Options
------------

To set the source for the test results, use the ``--ibutsu-source`` option::

    pytest --ibutsu http://ibutsu/ --ibutsu-source my-test-run

If you want to add metadata to each result's metadata, you can use the ``--ibutsu-data`` option::

    pytest --ibutsu http://ibutsu/ --ibutsu-data key=value

You can specify multiple of this option::

    pytest --ibutsu http://ibutsu/ --ibutsu-data key1=value1 --ibutsu-data key2=value2

You can also specify sub-keys via dotted notation::

    pytest --ibutsu http://ibutsu/ --ibutsu-data key.subkey.susbsub=value

Set Project
-----------

If your Ibutsu server requires a project set, you can do that with the ``--ibutsu-project`` option::

    pytest --ibutsu http://ibutsu/ --ibutsu-project 5eb1aff37c274bcd20002476

You can also use the project ``name`` field::

    pytest --ibutsu http://ibutsu/ --ibutsu-project my-project

Offline Usage
-------------

If you want to still store your results, but can't upload immediately, the Ibutsu plugin can create
an archive which you can upload later. Use ``archive`` with the ``--ibutsu`` option::

    pytest --ibutsu archive

The Ibutsu plugin will save the archive in your current directory, and will print out the location.

Usage
-----

With this plugin installed, and the configuration set up, your test results will automatically be
sent to the Ibutsu server.


Hooks
-----

The plugin has its own hooks. They are defined in ``newhooks.py``.
