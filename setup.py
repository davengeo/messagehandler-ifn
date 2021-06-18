from setuptools import setup

setup(
    author="David Navarro Alvarez",
    author_email="me@davengeo.com",
    description="event-handler interface",
    url="https://github.com/davengeo/devops-tools",
    name="event-handler-interface",
    version='0.0.1',
    packages=[
        'src'
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
