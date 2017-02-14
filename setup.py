"""Setup."""

from setuptools import find_packages, setup

setup(
    name='crimereports',
    version='1.0.0',
    description='Provides basic API to crimereports.com.',
    url='https://github.com/happyleavesaoc/python-crimereports/',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=find_packages(),
    install_requires=['requests==2.12.4'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
