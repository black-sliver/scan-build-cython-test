from setuptools import setup
from Cython.Build import cythonize


setup(name='test',
      author='black-sliver',
      version='0.0.1',
      ext_modules=cythonize("test.pyx"),
      python_requires='>=3')
