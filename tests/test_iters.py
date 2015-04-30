from mess import iters


def test_pairs():
    assert list(iters.pairs([1, 2, 3, 4])) == [(1, 2), (2, 3), (3, 4)]


def test_pairs_empty():
    assert list(iters.pairs([])) == []


def test_pairs_not_enough_items():
    assert list(iters.pairs([1])) == []


def test_lines():
    assert list(iters.lines(['a\n', 'b\n', 'c'])) == ['a', 'b', 'c']


def test_length():
    assert iters.length(iter([0, 1])) == 2


def test_length_empty():
    assert iters.length(iter([])) == 0


def test_length_list():
    assert iters.length([0, 1]) == 2