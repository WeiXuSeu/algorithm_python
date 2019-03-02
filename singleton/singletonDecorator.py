from functools import wraps


def singleton_decorator(cls):
    instances = {}

    @wraps(cls)
    def get_singleton_inst(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_singleton_inst


@singleton_decorator
class TestClass(object):
    hello = "world"


if __name__ == "__main__":
    inst1 = TestClass()
    print id(inst1)
    inst2 = TestClass()
    print id(inst2)

