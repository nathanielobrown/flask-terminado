"""
Flask-Terminado
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Terminado',
    version='0.1',
    url='http://nathanielobrown.com',
    license='BSD',
    author='Nathaniel Brown',
    author_email='nathanielobrown@gmail.com',
    description=('Integrates terminado with flask to provide a web based CLI '
                 '(command line interface)'),
    long_description=__doc__,
    py_modules=['flask_sqlite3'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'terminado'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)