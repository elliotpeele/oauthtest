import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'pyramid_oauth2_provider',
    ]

setup(name='oauthtest',
      version='0.0',
      description='oauthtest',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Elliot Peele',
      author_email='elliot@bentlogic.net',
      url='http://github.com/elliotpeele/oauthtest',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='oauthtest',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = oauthtest:main
      """,
      )
