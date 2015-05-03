from mess import dicts


def test_groupby():
    assert (dicts.groupby([0, 1, 2, 3], key=lambda n: n % 2 == 0)
            == {True: [0, 2], False: [1, 3]})


def test_groupby_no_key():
    assert dict(dicts.groupby([0, 1, 1, 0, 1])) == {0: [0, 0], 1: [1, 1, 1]}
