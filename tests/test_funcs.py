from mess.funcs import call
from mess import iters


def test_call():
    assert iters.length(filter(call.isdigit, ['1', 'b', '2'])) == 2