=====
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

