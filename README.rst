What is it?
===========
Python utilities everyone wrote but were afraid to upload to PyPI.

Install
=======

.. code-block:: shell

   git clone https://github.com/alexandershov/mess && python setup.py install

Usage
=====

.. code-block:: pycon

   >>> from mess import iters
   # iterate by pairs
   >>> list(iters.pairs([1, 2, 3, 4]))
   [(1, 2), (2, 3), (3, 4)]

   # iterate by lines (with stripped trailing newline)
   >>> list(iters.lines(['a\n', 'b\n', 'c']))
   ['a', 'b', 'c']



