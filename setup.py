from setuptools import setup

setup(
    name="SECEdgarPy",
    version="0.0.1",
    description="A simple to work with library to interact and get information from the SEC edgar Data",
    install_requires=[
        'os',
        'pandas',
        'requests',
        'bs4'
    ],
)