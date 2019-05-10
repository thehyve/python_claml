=============================
ClaML reader
=============================

|Build status| |codecov| |pypi| |downloads|

.. |Build status| image:: https://travis-ci.org/thehyve/python_claml.svg?branch=master
   :alt: Build status
   :target: https://travis-ci.org/thehyve/python_claml/branches
.. |codecov| image:: https://codecov.io/gh/thehyve/python_claml/branch/master/graph/badge.svg
   :alt: codecov
   :target: https://codecov.io/gh/thehyve/python_claml
.. |pypi| image:: https://img.shields.io/pypi/v/python-claml.svg
   :alt: PyPI
   :target: https://pypi.org/project/python-claml/
.. |downloads| image:: https://img.shields.io/pypi/dm/python-claml.svg
   :alt: PyPI - Downloads
   :target: https://pypi.org/project/python-claml/


A ClaML reader for Python.
Generated from the ClaML.dtd file from the DIMDI_, using PyXB_.


Features
--------

Reads classification files in ClaML format (XML) into Python objects.
See `<examples/test1.py>`_ for a usage example.


Resources
---------
- van der Haring EJ, Broënhorst S, ten Napel H, Weber S, Schopen M, Zanstra PE. `ClaML: a standard for the electronic publication of classification coding schemes`_
- `ISO 13120:2013`_ Health informatics -- Syntax to represent the content of healthcare classification systems -- Classification Markup Language (ClaML),
  now superseded by `ISO 13120:2019`_.
- DIMDI_ (Deutsche Institut für Medizinische Dokumentation und Information) `ICD-10-GM`_ download: icd10gm2019syst-claml.zip_

.. _`ISO 13120:2013`: https://www.iso.org/standard/52952.html
.. _`ISO 13120:2019`: https://www.iso.org/standard/69318.html
.. _`ClaML: a standard for the electronic publication of classification coding schemes`: https://www.ncbi.nlm.nih.gov/pubmed/17108612
.. _DIMDI: https://www.dimdi.de
.. _`ICD-10-GM`: https://www.dimdi.de/dynamic/de/klassifikationen/downloads/?dir=icd-10-gm
.. _icd10gm2019syst-claml.zip: https://www.dimdi.de/dynamic/.downloads/klassifikationen/icd-10-gm/version2019/icd10gm2019syst-claml.zip

.. _PyXB: http://pyxb.sourceforge.net


Usage
-----

To use ClaML reader in a project:

.. code-block:: python

  import python_claml


Example
^^^^^^^

Read and parse the contents of a ClaML file and print all class codes:

.. code-block:: python

    with open(file_name, 'r') as input_file:
        # Read file contents
        contents = input_file.read()
        # Parse ClaML document
        classification: ClaML = claml.CreateFromDocument(contents)
        for cls in classification.Class:
            print(cls.code)


Development
-----------

The code was generated using the following commands:

.. code-block:: bash

  pyxbgen --schema-root=../resources -u ClaML.xsd -m python_claml.claml


Install
^^^^^^^

From the package index:

.. code-block:: bash

  pip install python-claml

or from source:

.. code-block:: bash

  git clone https://github.com/thehyve/python_claml.git
  cd python_claml
  pip install .


Test
^^^^

.. code-block:: bash

  python setup.py test


License
-------

Copyright (c) 2019 The Hyve B.V.

The ClaML reader is licensed under the MIT License. See the file `<LICENSE>`_.
