import os
from distutils.core import setup

if os.name == 'nt':
    requirements = ['serial', 'win32']
    data_files=[('DLLs', ['cserialfc.dll'])]
else:
    requirements = ['serial']
    data_files=[('DLLs', ['libcserialfc.so', 'libcserialfc.so.6'])]

setup(name='pyserialfc',
      version='1.4.0',
      packages = ['serialfc', 'serialfc.tools'],
      data_files=data_files,
      requires=requirements,
      )
