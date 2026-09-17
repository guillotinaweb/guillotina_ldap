# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


# Pins align with guillotina 7.x test extras (pytest-asyncio must stay <0.22).
test_reqs = [
    "pytest>=7.4.0,<8.0.0",
    "pytest-asyncio>=0.21.0,<0.22.0",
    "pytest-docker-fixtures==1.4.2",
    "pytest-aiohttp>=0.3.0",
    "async-asgi-testclient<2.0.0",
    "coverage>=4.0.3",
    "pytest-cov",
    "psycopg2-binary",
    # email_validation / mailer / templates used by the test fixtures
    "jinja2",
    "html2text>=2018.1.9",
    "aiosmtplib>=1.0.6",
    "pytz",
]


setup(
    name="guillotina_ldap",
    version=open("VERSION").read().strip(),
    description="guillotina ldap auth support",
    long_description=(open("README.rst").read() + "\n" + open("CHANGELOG.rst").read()),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author="Ramon Navarro Bosch",
    author_email="ramon@plone.org",
    keywords="guillotina async ldap",
    url="https://pypi.python.org/pypi/guillotina_ldap",
    license="GPL version 3",
    setup_requires=[
        "pytest-runner",
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=["ez_setup"]),
    package_data={"": ["*.txt", "*.rst"], "guillotina_ldap": ["py.typed"]},
    install_requires=["setuptools", "guillotina>=6.0", "bonsai", "retry"],
    extras_require={"test": test_reqs},
    tests_require=test_reqs,
    entry_points={
        "guillotina": [
            "include = guillotina_ldap",
        ]
    },
)
