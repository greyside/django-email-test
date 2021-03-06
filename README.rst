Django Email Test
=================

A simple app for sending test emails via Django's admin site.

Usage
-----

Put `django_email_test` in INSTALLED_APPS, then run syncdb.

In the admin site index, go down to where it says "Django Email Test" and add a TestEmail. When the model is saved for the first time, Django will attempt to send an email. If any errors occur when sending the email, they'll be stored on the model.

Contributing
------------

You can fork this project on GitHub: http://github.com/SeanHayes/django-email-test.

License
-------

This project is licensed under the BSD License: http://www.opensource.org/licenses/bsd-license.php

Links
-----

* https://github.com/SeanHayes/django-email-test
* http://pypi.python.org/pypi/django-email-test
