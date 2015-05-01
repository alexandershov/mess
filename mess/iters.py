from collections import defaultdict
import itertools

from six.moves import zip
import six


def pairs(iterable):
    """
    :return: iterator yielding overlapping pairs from iterable

    :Example:

    >>> list(pairs([1, 2, 3, 4])
    [(1, 2), (2, 3), (3, 4)]
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def lines(strings):
    """
    :param strings: iterable yielding str/unicode objects
    :return: iterator yielding original strings with trailing newline (\n) stripped

    :Example:

    >>> list(lines(['a\n', 'b\n', 'c']))
    ['a', 'b', 'c']
    """
    for s in strings:
        yield s.rstrip('\n')


def length(iterable):
    """
    Return number of items in the iterable.
    Attention: this function consumes the whole iterable and
    can never return if iterable has infinite number of items.
    :Example:
    >>> length(iter([0, 1]))
    2
    >>> length([0, 1, 2])
    3
    """
    try:
        return len(iterable)
    except TypeError:
        return sum(1 for item in iterable)


# TODO: add a variant of this function: groupby_as_dict that returns a dictionary
def groupby(iterable, key=None):
    """
    Make an iterator that returns keys and groups (items having the same key) from the iterable.
    It's like itertools.groupby but:
     * doesn't require iterable to be sorted on the key function
     * consumes the whole iterable into memory
    :param key: function to apply to each element of the iterable.
      If not specified or is None key defaults to identity function and
      returns the element unchanged.

    :Example:
    >>> dict(groupby([0, 1, 2, 3], key=lambda x: x % 2 == 0)
    {True: [0, 2], False: [0, 1]}
    """
    groups = defaultdict(list)
    for item in iterable:
        if key is None:
            key_value = item
        else:
            key_value = key(item)
        groups[key_value].append(item)
    return six.viewitems(groups)