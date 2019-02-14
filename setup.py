#!/usr/bin/env python
"""
Package setup installation and metadata for lambdata
"""

import setuptools

REQUIRED = [
    'numpy', # You can put conditions here like 'numpy >= 2.3.0'
    'pandas',
    'minepy'
]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

# This is all the stuff we're telling pypi
setuptools.setup(
    name='lambdata-samirgadkari',
    version='0.0.6',  # We have to edit this if we changed code and are now
                      # pushing it.
    author='samirgadkari',
    description='A collection of data science helper functions.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/samirgadkari/lambdata',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ]
)
