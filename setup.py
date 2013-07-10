import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'nokaut',
    'allegro'
    ]

links = ['https://github.com/pkrysiak/allegro_repo/archive/master.zip#egg=allegro',
         'https://github.com/pkrysiak/nokaut_repo/archive/master.zip#egg=nokaut']

setup(name='myapp',
      version='0.0',
      description='myapp',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      dependency_links = links,
      test_suite="pyramid_app",
      entry_points="""\
      [paste.app_factory]
      main = pyramid_app:main
      """,
      )
