from setuptools import setup

setup(
    author="David Navarro Alvarez",
    author_email="me@davengeo.com",
    description="messagehandler interface",
    url="https://github.com/davengeo/messagehandler-ifn.git",
    name="messagehandler-ifn",
    version='0.2.0',
    packages=[
        'messagehandler'
    ],
    install_requires=[
        'kombu'
    ],
    package_data={
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Systems Administration',
    ]
)
