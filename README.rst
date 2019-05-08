=============================
ClaML reader
=============================

|Build status| |codecov|

.. |Build status| image:: https://travis-ci.org/thehyve/python_claml.svg?branch=master
   :target: https://travis-ci.org/thehyve/python_claml/branches
.. |codecov| image:: https://codecov.io/gh/thehyve/python_claml/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/thehyve/python_claml

A ClaML reader for Python.
Created from the ClaML.dtd file from the DIMDI_, using PyXB_.


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


Development
-----------

The code was generated using the following commands: ::

  pyxbgen --schema-root=../resources -u ClaML.xsd -m python_claml.claml

Build: ::

  pip install .

Test: ::

  python setup.py test


License
-------

Copyright (c) 2019 The Hyve B.V.

The ClaML reader is licensed under the MIT License. See the file `<LICENSE>`_.
