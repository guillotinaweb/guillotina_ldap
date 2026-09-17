GUILLOTINA_LDAP
===============

LDAP Auth backend for Guillotina.


Configuration
-------------

Add this to your Guillotina config file:

.. code-block:: json

    ...
    "applications": ["guillotina_ldap"],
    "ldap": {
        "host": "ldap://myldap.example.com",
        "tls": true,
        "attribute_users": "uid",
        "objecttype": "inetOrgPerson",
        "managerdn": "CM=MANAGER,DC=DOMAIN,DC=ORG",
        "managerpwd": "secret",
        "usersdn": "OU=USERS,DC=DOMAIN,DC=ORG",
        "managers": ["bob"]
    }


Development and testing
-----------------------

Requires Python 3.10 or newer (CI runs 3.10, 3.11 and 3.12). Docker is needed
for the OpenLDAP test fixture.

.. code-block:: bash

    python3 -m venv .
    ./bin/pip install -e ".[test]"
    ./bin/pip install pre-commit
    ./bin/pre-commit install
    ./bin/pytest --capture=no --tb=native -v guillotina_ldap


Formatting is enforced by pre-commit (black, isort, flake8) on every commit,
and by GitHub Actions on push. To run the checks manually:

.. code-block:: bash

    pre-commit run --all-files
