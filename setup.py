import os
from distutils.core import setup

prjdir = os.path.dirname(__file__)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

setup(name='termprint',
      version='0.1',
      description='termcolor.py wrapper for simpler usage.',
      author='Marcos Lopez',
      license='MIT',
      py_modules=['termprint'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
          ]
      )
