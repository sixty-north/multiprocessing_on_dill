Multiprocessing on Dill
=======================

**Authors**: Robert Smallshire (rob@sixty-north.com) (initial version), Juan Carlos Rocamonde (juancarlosrocamonde@gmail.com) (3.7 version).

This project is a friendly fork – for Python 3 – of the Python Standard Library `multiprocessing
<https://docs.python.org/3/library/multiprocessing.html>`_ module, which uses the third-party
`dill <https://pypi.python.org/pypi/dill>`_ serializer instead of the standard ``pickle`` serializer.  This overcomes
many shortcomings of ``pickle`` which prevent multiprocessing being used with lambdas, closures and other useful Python
objects.

The easiest way to use ``multiprocessing_on_dill`` in place of ``multiprocessing`` is simply to replace any import
statements like this::

    import multiprocessing

with::

    import multiprocessing_on_dill as multiprocessing

and import statements like this::

    from multiprocessing import Pool

with::

    from multiprocessing_on_dill import Pool

With such import changes in place, it will now be possible to use functions like ``Pool.map()`` with lambdas::

    pool = Pool(12)
    result = pool.map(lambda x: x*x, range(10000))

Everything else should be identical to the Python version.

You can determine from which version of the Python Standard Library ``multiprocessing_on_dill`` has been forked, by
examining the ``multiprocessing_on_dill.__version__`` attribute.


Future
======

It is our hope that one day the Python Standard Library ``pickle`` module will gain the additional capabilities of
``dill`` and there will no longer be a need for ``multiprocessing_on_dill`` to exist.
