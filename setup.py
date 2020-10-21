from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print('This Python is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))


setup(name='BHER',
      packages=[package for package in find_packages()
                if package.startswith('BHER')],
      install_requires=[
          'scipy',
          'tqdm',
          'joblib',
          'zmq',
          'dill',
          'progressbar2',
          'mpi4py',
          'cloudpickle',
          'click',
      ],
      description='This package is based on OpenAI baselines 0.1.5',
      author='xx',
      version='1.0')
