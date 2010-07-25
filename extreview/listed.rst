Listed Extensions
=================

This list contains extensions that passed listing.  This means the
extension is on the list of extensions on the website.  It does not
contain extensions that are approved.


Flask-CouchDB
-------------

:Last-Review: 2010-07-25
:Reviewed version: 0.2

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-CouchDBKit
----------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-Creole
------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".  Furthermore the README
file is empty.


flask-csrf
----------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2

Will not be approved because this is functionality that should be handled
in the form handling systems which is for Flask-WTF already the case.
Also, this implementation only supports one open tab with forms.

Name is not following Flask extension naming rules.

Considered for unlisting.


Flask-Genshi
------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.3

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".  Furthermore the long
description is empty.  The zip_safe flag is not set to False which is a
requirement for approved extensions.


flask-lesscss
-------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.9.1

Broken package description, nonconforming package name, does not follow
standard API rules (init_lesscss instead of lesscss).

Considered for unlisting, improved version should release as
"Flask-LessCSS" with a conforming API and fixed packages indices, as well
as a testsuite.


flask-mail
----------

:Last-Review: 2010-07-25
:Reviewed Version: 0.3.1

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".  Furthermore the long
description in the package index is a little bit too short.

Package name should be changed to Flask-Mail with the approval to be
consistent, this might also be the change to improve the API if necessary,
but I don't see any big design problems there.


Flask-OAuth
-----------

:Last-Review: 2010-07-25
:Reviewed Version: 0.9

Short long description, missing tests.


Flask-OpenID
------------

:Last-Review: 2010-07-25
:Reviewed Version: 1.0.1

Short long description, missing tests.


Flask-Script
------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".

The upcoming 0.3 release looks promising, could need a longer "long
description" in the package index though.


Flask-Testing
-------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-Themes
------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.1

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-Uploads
-------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.1

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-WTF
---------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2.1

Would be fine for approval, but the test suite is not part of the sdist
package (missing entry in MANIFEST.in) and the test suite does not respond
to either "make test" or "python setup.py test".


Flask-XML-RPC
-------------

:Last-Review: 2010-07-25
:Reviewed Version: 0.2.1

Missing tests, API wise it would be fine for approval.
