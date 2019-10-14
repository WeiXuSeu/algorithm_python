class SingletonNew(object):
    _instant = None

    def __new__(cls, *args, **kws):
        if not cls._instant:
            cls._instant = super(SingletonNew, cls).__new__(cls, *args, **kws)
        return cls._instant


class TestClass(SingletonNew):
    hello = "world"


if __name__ == "__main__":
    inst1 = TestClass()
    print id(inst1)
    inst2 = TestClass()
    print id(inst2)