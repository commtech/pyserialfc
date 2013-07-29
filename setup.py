from distutils.core import setup

setup(name='pyserialfc',
      version='1.1.0',
      py_modules=['serialfc'],
      requires=['serial', 'win32'],
      )