Contributing
============

Fork this repository
--------------------

`Fork this repository before contributing`_. It is a better practice, possibly even enforced, that only Pull Request from forks are accepted. In my opinion this creates a cleaner representation of the whole `contributions to the project`_.

Install for developers
----------------------

First, clone the repository as described in the :ref:`section above<Fork this repository>`.

Create a dedicated Python environment where to develop the project.

If you are using :code:`pip` follow the official instructions on `Installing packages using pip and virtual environments`_, most likely what you want is:

::

    python3 -m venv pdbparams
    source pyprojskel/bin/activate

If you are using `Anaconda`_ go for:

::

    conda create --name pyprojskel python=3.7
    conda activate pdbparams

Where :code:`pdbparams` is the name you wish to give to the environment dedicated to this project.

Either under *pip* or *conda*, install the package in :code:`develop` mode, and also :ref:`tox<Uniformed Tests>`.

::

    python setup.py develop
    # for pip
    pip install tox
    # for conda
    conda install tox -c conda-forge

Under this configuration the source you edit in the repository git folder is automatically reflected in the development installation.

Continue your implementation following the development guidelines described bellow.

Branch workflow
---------------

*The following applies to external contributors, yet main developers can also follow these guidelines.*

Branch workflow for development and contribution should follow the `Gitflow Workflow`_ guidelines. Please read careful through that guide. Here we highlight the general approach with some tasteful additions such as the ``--no-ff`` flag.

Clone your fork
~~~~~~~~~~~~~~~

Indeed the first thing to do is to clone your fork, and keep it `up to date with the upstream`_:

::

    git clone https://github.com/YOUR-USERNAME/Protein_Data_Bank_Parameters.git
    cd into/cloned/fork-repo
    git remote add upstream git://github.com/joaomcteixeira/Protein_Data_Bank_Parameters.git
    git fetch upstream
    git checkout latest
    git pull upstream latest
    git push origin latest  # to send updates to your forked repository

New feature
~~~~~~~~~~~

To work on a new feature, branch out from the ``latest`` branch:

::
    
    git checkout latest
    git checkout -b feature_branch

Develop the feature and keep regular pushes to your fork with comprehensible commit messages.

Push to latest
~~~~~~~~~~~~~~

To see your development accepted in the main project, you should create a `Pull Request`_ to the ``latest`` branch following the `PULLREQUEST.rst`_ guidelines.

**Before submitting a Pull Request, verify your development branch passes all tests as** :ref:`described bellow<Uniformed Tests>` **. If you are developing new code you should also implement new test cases.**

Uniformed Tests
---------------

Thanks to `Tox`_ we can have a uniform testing platform where all developers are forced to follow the same rules and, above all, all tests occur in a controlled Python environment.

With *Tox*, the testing setup can be defined in a configuration file, the `tox.ini`_, which contains all the operations that are performed during the test phase. Therefore, to run the unified test suite, developers just need to execute ``tox``, provided `tox is installed`_ in the Python environment in use.

::

    pip install tox
    # or
    conda install tox -c conda-forge

Before creating a Pull Request from your branch, certify that all the tests pass correctly by running:

::
    
    tox

These are exactly the same tests that will be performed in Travis-CI.

Also, you can run individual environments if you wish to test only specific functionalities, for example:

::
    
    tox -e check  # code style and file compatibility
    tox -e docs  # only builds the documentation
    tox -e py37  # runs tests for python=3.7


.. _tox.ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _tox is installed: https://tox.readthedocs.io/en/latest/install.html
.. _Fork this repository before contributing: https://github.com/joaomcteixeira/Protein_Data_Bank_Parameters/network/members
.. _up to date with the upstream: https://gist.github.com/CristinaSolana/1885435
.. _contributions to the project: https://github.com/joaomcteixeira/python-project-skeleton/network
.. _Gitflow Workflow: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
.. _Pull Request: https://github.com/joaomcteixeira/python-project-skeleton/pulls
.. _PULLREQUEST.rst: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/docs/PULLREQUEST.rst
.. _Installing packages using pip and virtual environments: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
.. _Anaconda: https://www.anaconda.com/
