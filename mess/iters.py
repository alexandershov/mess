import itertools

from six.moves import zip


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