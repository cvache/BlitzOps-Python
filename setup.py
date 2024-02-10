from setuptools import setup, find_packages

setup(
    name='BlitzOps_Python',
    version='0.0.1',
    packages=find_packages(),
    description='Python Package for BlitzOps',
    long_description=open('README.md').read(),
    license='Apache License 2.0',
    author='Carson Vache',
    author_email='carsonvache@gmail.com',
    url='https://github.com/cvache/BlitzOps-Python',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)