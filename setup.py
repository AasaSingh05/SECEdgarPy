from setuptools import setup

setup(
    name="SECEdgar-Python",
    version="0.0.2",
    description="A simple library to interact with and retrieve information from the SEC Edgar Data.",
    install_requires=[
        'os>=2.1.4',
        'pandas>=2.2.3',
        'requests>=2.32.3',
        'bs4>=0.0.2'
    ]
)