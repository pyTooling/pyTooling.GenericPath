.. _dependency:

Dependencies
############

.. |img-pyGenericPath-lib-status| image:: https://img.shields.io/librariesio/release/pypi/pyGenericPath
   :alt: Libraries.io status for latest release
   :height: 22
   :target: https://libraries.io/github/pyTooling/pyTooling.GenericPath
.. |img-pyGenericPath-req-status| image:: https://img.shields.io/requires/github/pyTooling/pyTooling.GenericPath
   :alt: Requires.io
   :height: 22
   :target: https://requires.io/github/pyTooling/pyTooling.GenericPath/requirements/?branch=master

+------------------------------------------+------------------------------------------+
| `Libraries.io <https://libraries.io/>`_  | `Requires.io <https://requires.io/>`_    |
+==========================================+==========================================+
| |img-pyGenericPath-lib-status|           | |img-pyGenericPath-req-status|           |
+------------------------------------------+------------------------------------------+

.. _dependency-package:

pyGenericPath Package (Mandatory)
*********************************

.. rubric:: Manually Installing Package Requirements

Use the :file:`requirements.txt` file to install all dependencies via ``pip3``
or install the package directly from PyPI (see :ref:`installation`).

.. code-block:: shell

   pip3 install -U -r requirements.txt


.. rubric:: Dependency List

+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Package**                                              | **Version** | **License**                                                                               | **Dependencies**                                                                                                                                                     |
+==========================================================+=============+===========================================================================================+======================================================================================================================================================================+
| `py-flags <https://GitHub.com/pasztorpisti/py-flags>`__  | ≥1.1.4      | `MIT <https://GitHub.com/pasztorpisti/py-flags/blob/master/LICENSE.txt>`__                | * `dictionaries <https://GitHub.com/pasztorpisti/py-dictionaries>`__ (`MIT <https://GitHub.com/pasztorpisti/py-dictionaries/blob/master/LICENSE.txt>`__)             |
+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pyTooling <https://GitHub.com/pyTooling/pyTooling>`__   | ≥1.4.4      | `Apache License, 2.0 <https://GitHub.com/pyTooling/pyTooling/blob/master/LICENSE.txt>`__  | *None*                                                                                                                          |
+----------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+


.. _dependency-testing:

Unit Testing / Coverage (Optional)
**********************************

Additional Python packages needed for testing and code coverage collection.
These packages are only needed for developers or on a CI server, thus
sub-dependencies are not evaluated further.


.. rubric:: Manually Installing Test Requirements

Use the :file:`tests/requirements.txt` file to install all dependencies via
``pip3``. The file will recursively install the mandatory dependencies too.

.. code-block:: shell

   pip3 install -U -r tests/requirements.txt


.. rubric:: Dependency List

+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| **Package**                                               | **Version** | **License**                                                                            | **Dependencies**     |
+===========================================================+=============+========================================================================================+======================+
| `pytest <https://GitHub.com/pytest-dev/pytest>`__         | ≥6.2.5      | `MIT <https://GitHub.com/pytest-dev/pytest/blob/master/LICENSE>`__                     | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `pytest-cov <https://GitHub.com/pytest-dev/pytest-cov>`__ | ≥3.0.0      | `MIT <https://GitHub.com/pytest-dev/pytest-cov/blob/master/LICENSE>`__                 | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `Coverage <https://GitHub.com/nedbat/coveragepy>`__       | ≥6.1        | `Apache License, 2.0 <https://GitHub.com/nedbat/coveragepy/blob/master/LICENSE.txt>`__ | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `mypy <https://GitHub.com/python/mypy>`__                 | ≥0.910      | `MIT <https://GitHub.com/python/mypy/blob/master/LICENSE>`__                           | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+
| `lxml <https://GitHub.com/lxml/lxml>`__                   | ≥4.6.4      | `BSD 3-Clause <https://GitHub.com/lxml/lxml/blob/master/LICENSE.txt>`__                | *Not yet evaluated.* |
+-----------------------------------------------------------+-------------+----------------------------------------------------------------------------------------+----------------------+


.. _dependency-documentation:

Sphinx Documentation (Optional)
*******************************

Additional Python packages needed for documentation generation. These packages
are only needed for developers or on a CI server, thus sub-dependencies are not
evaluated further.


.. rubric:: Manually Installing Documentation Requirements

Use the :file:`doc/requirements.txt` file to install all dependencies via
``pip3``. The file will recursively install the mandatory dependencies too.

.. code-block:: shell

   pip3 install -U -r doc/requirements.txt


.. rubric:: Dependency List

+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| **Package**                                                                                     | **Version**  | **License**                                                                                              | **Dependencies**     |
+=================================================================================================+==============+==========================================================================================================+======================+
| `Sphinx <https://GitHub.com/sphinx-doc/sphinx>`__                                               | ≥4.3.0       | `BSD 3-Clause <https://GitHub.com/sphinx-doc/sphinx/blob/master/LICENSE>`__                              | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_btd_theme <https://GitHub.com/buildthedocs/sphinx.theme>`__                             | ≥0.5.2       | `MIT <https://GitHub.com/buildthedocs/sphinx.theme/blob/master/LICENSE>`__                               | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| !! `sphinx_fontawesome <https://GitHub.com/fraoustin/sphinx_fontawesome>`__                     | ≥0.0.6       | `GPL 2.0 <https://GitHub.com/fraoustin/sphinx_fontawesome/blob/master/LICENSE>`__                        | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
| `sphinx_autodoc_typehints <https://GitHub.com/agronholm/sphinx-autodoc-typehints>`__            | ≥1.12.0      | `MIT <https://GitHub.com/agronholm/sphinx-autodoc-typehints/blob/master/LICENSE>`__                      | *Not yet evaluated.* |
+-------------------------------------------------------------------------------------------------+--------------+----------------------------------------------------------------------------------------------------------+----------------------+
