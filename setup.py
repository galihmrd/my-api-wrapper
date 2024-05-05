import os

from setuptools import setup

from gmrd_api import __version__

os.system("pip3 install -r requirements.txt")
with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

setup(
    name="gmrd-api",
    version=__version__,
    description="multi function api",
    author="Galih Mrd",
    author_email="driveme177@gmail.com",
    packages=[],  # same as name
    url="https://github.com/galihmrd",
    license="MIT",
    install_requires=requires,
)
