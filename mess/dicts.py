def groupby(iterable, key=None):
    """
    Group items from iterable by key and return a dictionary where values are
    the lists of items from the iterable having the same key.

    :param key: function to apply to each element of the iterable.
      If not specified or is None key defaults to identity function and
      returns the element unchanged.

    :Example:
    >>> groupby([0, 1, 2, 3], key=lambda x: x % 2 == 0)
    {True: [0, 2], False: [1, 3]}
    """
    groups = {}
    for item in iterable:
        if key is None:
            key_value = item
        else:
            key_value = key(item)
        groups.setdefault(key_value, []).append(item)
    return groups
