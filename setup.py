import os
try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

here = os.path.abspath( os.path.dirname( __file__ ) )
README = open(os.path.join( here, 'README.rst' ) ).read()

setup(
    name='mudskipper',
    version='1.1',
    description='',
    long_description=README,
    license='',
    author='',
    author_email='',
    packages=[ 'mudskipper' ],
    install_requires=['requests<=2.19.1', 'zeep==2.4.0'],
    dependency_links=[],
    classifiers=[
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Programming Language :: Python',
    ])
