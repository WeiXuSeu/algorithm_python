class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestClass(object):
    __metaclass__ = Singleton
    hello = "world"


if __name__ == "__main__":
    inst1 = TestClass()
    print id(inst1)
    print inst1.hello
    inst2 = TestClass()
    print id(inst2)
    print inst2.hello
    print dir(inst2)
    print dir(TestClass)
