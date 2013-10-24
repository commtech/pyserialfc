import os
from distutils.core import setup

if os.name == 'nt':
    requirements = ['serial', 'win32']
else:
    requirements = ['serial']

setup(name='pyserialfc',
      version='1.3.0',
      py_modules=['serialfc'],
      requires=requirements,
      )
