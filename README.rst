============================
Protein Data Bank Parameters
============================

A Python package hosting the static parameters for the Protein Data Bank file formats.

.. start-badges

.. image:: https://img.shields.io/travis/joaomcteixeira/python-project-skeleton/latest?label=TravisCI
    :target: https://travis-ci.org/joaomcteixeira/python-project-skeleton
    :alt: Travis-CI latest branch

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/latest?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Read the Docs (latest)

.. image:: https://img.shields.io/pypi/wheel/taurenmd.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/taurenmd

.. image:: https://img.shields.io/pypi/pyversions/taurenmd.svg
    :alt: Supported versions
    :target: https://pypi.org/project/taurenmd

.. image:: https://img.shields.io/pypi/dm/taurenmd?label=PyPI%20Downloads
    :alt: PyPI - Downloads
    :target: https://pypistats.org/packages/taurenmd

.. end-badges

Motivation
==========

Handling Protein Data Bank data through Python requires a constantly retyping of the PDB format static parameters,
such as, line parsing slices, atoms names, residue names, etc. This package hosts all those static parameters
required to handle ``.pdb`` files.

Installation
============

```bash
pip install --upgrade pdbparams
```

Usage
=====

**Protein Data Bank Parameters** library is organized in different thematic modules.

For example, to access the ``slice`` objects required to slice ``PDB`` `ATOM`_ lines:

.. code-block: python

    from pdbparams.slicing import atom as atom_slice


    atom_line = "ATOM     32  N  AARG A  -3      11.281  86.699  94.383  0.50 35.88           N  "

    resseq = atom_line[atom_slice.resseq]
    
    print(resseq)
    # this prints '  -3' 

.. _ATOM: http://www.wwpdb.org/documentation/file-format-content/format33/sect9.html#ATOM 
