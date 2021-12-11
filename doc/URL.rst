Unified Resource Locator (URL)
##############################

Implements a *Unified Resource Locator* (URL).

.. code-block:: Python

   url = URL.Parse("http://paebbels:xxx@semaphore.plc2.de:5000/api/v1/semaphore?name=Riviera&foo=bar#page2")
   print(url.Scheme())      # HTTP
   print(url.User())        # paebbels
   print(url.Password())    # xxx
   print(url.Host())        # semaphore.plc2.de:5000
   print(url.Path())        # /api/v1/semaphore
   print(url.Query())       # name=Riviera&foo=bar
   print(url.Fragment())    # page2


Protocols
*********

.. autoclass:: pyTooling.GenericPath.URL.Protocols
   :show-inheritance:
   :members:
   :private-members:


Host
****

.. autoclass:: pyTooling.GenericPath.URL.Host
   :show-inheritance:
   :members:
   :private-members:


Element
*******

.. autoclass:: pyTooling.GenericPath.URL.Element
   :show-inheritance:
   :members:
   :private-members:


Path
****

.. autoclass:: pyTooling.GenericPath.URL.Path
   :show-inheritance:
   :members:
   :private-members:


URL
***

.. autoclass:: pyTooling.GenericPath.URL.URL
   :show-inheritance:
   :members:
   :private-members:
