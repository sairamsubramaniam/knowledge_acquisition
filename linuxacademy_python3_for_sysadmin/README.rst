msqbackup
==========

CLI for backing up remote MySQL databases locally

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/msqbackup``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 example w/ bucket name:

::
    $ msqbackup mysql://root@127.0.0.1:3306/linuxacademy --driver s3 backups

Local example w/ local path:

::
    $ msqbackup mysql://root@127.0.0.1:3306/linuxacademy --driver local /var/local/trials/backups

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::
    $ make

If virtualenv isn't active then use:

::
    $ pipenv run make
