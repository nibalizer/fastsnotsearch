fast-snot-search
================

A simple flask app to search snot very quickly


Components:
-----------

1) cron to sync local copy of snot with real snot, pull operation, not done yet

2) web app that wraps notmuch mail searcher


Getting started:
----------------

Prereqs:


    #  apt-get install python-notmuch notmuch-vim
    #  apt-get install python notmuch libnotmuch-dev apache2 libapache2-mod-wsgi python-flask

Development mode:

    $ python app.py

Production mode:

    # cp 020-fastsnotsearch /etc/apache2/sites-enabled
    # service apache2 restart

You will need to create a .htpasswd directory
