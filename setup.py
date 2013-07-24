from distutils.core import setup

setup(name='pyserialfc',
      version='1.0.0',
      packages=['serialfc'],
      requires=['serial', 'win32'],
      )