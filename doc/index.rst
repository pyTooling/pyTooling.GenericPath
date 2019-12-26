.. code-block::

                  ____                      _      ____       _   _
     _ __  _   _ / ___| ___ _ __   ___ _ __(_) ___|  _ \ __ _| |_| |__
    | '_ \| | | | |  _ / _ \ '_ \ / _ \ '__| |/ __| |_) / _` | __| '_ \
    | |_) | |_| | |_| |  __/ | | |  __/ |  | | (__|  __/ (_| | |_| | | |
    | .__/ \__, |\____|\___|_| |_|\___|_|  |_|\___|_|   \__,_|\__|_| |_|
    |_|    |___/

pyGenericPath Documentation
###########################

A generic path implementation to derive domain specific path libraries.

In many environments a path notation is needed or wished to identify resources
in a hierarchy of elements. Such a hierarchy usually consists of a root element
and path elements in one or multiple levels. Depending on the use case (domain)
different path element delimiter signs might be used: e.g. ``\`` in Windows paths,
``/`` in Linux paths or URLs, ``.`` in object-oriented-programming, etc.

This package defines a generic implementation of paths and common operations like
list elements (a.k.a ``dir``, ``ls``, ...).

On top of the generic path elements, domain specific paths can be created like
URLs with :class:`~pyGenericPath.URL.URL`.

.. admonition:: Path Hierarchy

   Write how to plan and implement a user-defined path hierarchy.

.. #
   inheritance-diagram:: Path hierarchy
   :top-classes: modA.clsA modB.clsB
   :parts: 1



Contributors
************

* `Patrick Lehmann <https://github.com/Paebbels>`_ (Maintainer)



License
*******

This library is licensed under **Apache License 2.0**.

------------------------------------

.. |docdate| date:: %b %d, %Y - %H:%M

.. only:: html

   This document was generated on |docdate|.

.. toctree::
   :caption: Overview
   :hidden:

   Installation
   Dependencies

.. toctree::
   :caption: Generic Classes
   :hidden:

   pyGenericPath

.. toctree::
   :caption: Domain Specific Paths
   :hidden:

   URL

.. toctree::
   :caption: Appendix
   :hidden:

   License
   genindex

.. #
   py-modindex
