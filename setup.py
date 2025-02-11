from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

VERSION = '1.0.0'

setup(
    name='rugcheck',
    version=VERSION,
    description='Python wrapper for RugCheck API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ccan23/rugcheck',
    author='ccan23',
    author_email='dev.ccanb@protonmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': [
            'pytest',
            'twine',
            'build',
            'rich',
            'wheel',
        ]
    },
    entry_points={
        'console_scripts': [
            'rugcheck=rugcheck.cli:rugcheck_cli',
        ],
    },
    keywords=['python', 'rugcheck', 'crypto', 'scam-detection', 'dex', 'liquidity', 'rugpull', 'scam'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)