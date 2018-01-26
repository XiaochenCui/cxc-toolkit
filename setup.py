from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

# Get the version number from VERSION file
with open(path.join(here, 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read().strip()

setup(
    name='cxc-toolkit',
    version=version,
    description='Toolbox contains a lot of utility functions',
    long_description=long_description,
    url='https://github.com/XiaochenCui/cxc-toolkit',
    author='Xiaochen Cui',
    author_email='jcnlcxc.new@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='toolkit',
    packages=find_packages(),
)
