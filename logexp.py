
class DefaultHandler: 
    @staticmethod
    def apply(data, exp, op):
        key, value = exp[0]
        return data.has_key(key) and op(data[key], value)

class LogExp:

    def __init__(self, exps, op, leaf=False):

        self.exps = exps
        self.op = op
        self.undefined = leaf

        if not self.undefined:
            ok = reduce(lambda x, y: x and y, map(lambda x: isinstance(x, LogExp), self.exps))
            if not ok:
                return ValueError

    def eval(self, data, handler=DefaultHandler): 

        if self.undefined:
            return handler.apply(data, self.exps, self.op)

        return reduce(lambda x, y: self.op(x, y), map(lambda x: x.eval(data, handler), self.exps))


