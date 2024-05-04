from setuptools import setup
from gmrd_api import __version__


setup(
   name='gmrd-api',
   version=__version__,
   description='multi function api',
   author='Galih Mrd',
   author_email='driveme177@gmail.com',
   packages=['gmrd_api'],  #same as name
   url='https://github.com/galihmrd',
   license='MIT',
   install_requires=[
      # -*- Extra requirements: -*-
   ],
)
