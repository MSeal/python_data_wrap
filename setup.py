import os
import shutil
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Cleanup builds so changes don't persist into setup
builddir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'build'))
distdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dist'))
if (os.path.isdir(builddir)):
    shutil.rmtree(builddir)
if (os.path.isdir(distdir)):
    shutil.rmtree(distdir)

setup(
    name = "PyDataWrap",
    version = "1.1.2",
    author = "Matthew Seal",
    author_email = "mseal@delphi.us",
    description = ("Tools for wrapping data and manipulating it in efficient ways"),
    install_requires=['xlrd'],
    packages=['datawrap'],
    test_suite = 'tests',
    zip_safe = False,
    long_description=read('README.md'),
)
