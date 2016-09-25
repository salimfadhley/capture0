from setuptools import setup

__VERSION__ = '0.1.21'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/capture0"
SHORT_DESCRIPTION = 'A tool for capturing data from the web.'

DESCRIPTION = SHORT_DESCRIPTION

GLOBAL_ENTRY_POINTS = {
    "console_scripts": ["capture0=capture0.main:main"]
}

setup(
    name="capture0",
    version=__VERSION__,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=["capture0", "capture0_data"],
    package_data={"capture0_static": ["dist", "dist/*"]},
    zip_safe=False,
    install_requires=['click', 'flask', 'cachetools', 'Flask-WTF', "markdown"],
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'coverage', 'unittest2'],
    entry_points=GLOBAL_ENTRY_POINTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT'
)
