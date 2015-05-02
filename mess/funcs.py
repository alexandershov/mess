import operator


# TODO: allow to pass extra args: e.g call.count.args('a')
class _Call(object):
    def __getattr__(self, method_name):
        """
        Return a callable object that calls the specified method name on its operand.
        """
        return operator.methodcaller(method_name)


call = _Call()