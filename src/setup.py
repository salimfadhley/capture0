import os
from setuptools import setup

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.5'
PROJECT_NAME = 'capture0'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/capture0"
SHORT_DESCRIPTION = 'A tool for capturing data from the web.'

DESCRIPTION = SHORT_DESCRIPTION

GLOBAL_ENTRY_POINTS = {
    "console_scripts": ["capture0=capture0.main:main"]
}

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    package="capture0",
    zip_safe=True,
    include_package_data=False,
    install_requires=['click', 'flask'],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage', 'unittest2'],
    entry_points=GLOBAL_ENTRY_POINTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT'
)
