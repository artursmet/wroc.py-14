#! /usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='helloworldtest',
    author='John Doe',
    author_email='john.doe@somecompany.com',
    description="My beautiful library",
    license='MIT',
    version='0.1.0',
    url='http://somecompany.com/',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.6.0'
    ],
    tests_require=[
        'mock'
    ],
    test_suite='helloworldtest.tests.suite',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
