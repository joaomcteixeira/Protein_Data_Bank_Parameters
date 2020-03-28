#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Setup dot py."""
from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    """Read description files."""
    path = join(dirname(__file__), *names)
    with io.open(path, encoding=kwargs.get('encoding', 'utf8')) as fh:
        return fh.read()


long_description = '{}\n{}'.format(
    re.compile(
        '^.. start-badges.*^.. end-badges',
        re.M | re.S,
        ).sub(
            '',
            read('README.rst'),
            ),
    re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read(join('docs', 'CHANGELOG.rst')))
    )

setup(
    name='pdbparams',
    version='0.0.0',
    description='A Python package hosting the static parameters for the Protein Data Bank file formats.',
    long_description=long_description,
    author='Joao Miguel Correia Teixeira',
    author_email='joaomcteixeira@gmail.com',
    url='https://github.com/joaomcteixeira/Protein_Data_Bank_Parameters',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(i))[0] for i in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        ],
    project_urls={
        'webpage': 'https://github.com/joaomcteixeira/Protein_Data_Bank_Parameters',
        'Documentation': 'https://protein-data-bank-parameters.readthedocs.io/en/latest/',
        'Changelog': 'https://github.com/joaomcteixeira/protein-data-bank-parameters/blob/latest/docs/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/joaomcteixeira/protein-data-bank-parameters/issues',
        },
    keywords=[
        'Protein Data Bank',
        'Proteins',
        'Structural Biology',
        'Biochemistry',
        ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=[],
    extras_require={},
    setup_requires=[],
    entry_points={},
    )
