from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# requirements = open(path.join(here, 'requirements.txt'), encoding='utf-8').readlines()
# requirements.append('ss_query_api')
# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='mididim',
    version='0.0.1',
    packages=find_packages(exclude=['contib', 'docs', 'test*', 'notebooks']),
    url='',
    license='',
    author='stephen j zabel',
    author_email='sjzabel@gmail.com',
    description='',
    long_description=long_description,
    zip_safe=False,
)

