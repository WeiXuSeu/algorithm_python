# -*- utf-8 -*-
from functools import wraps
import logging


def log_decorator(fun):
    @wraps(fun)
    def decorator(*args, **kwargs):
        print args
        print kwargs
        print fun.__dict__
        print fun.__name__
        print "start run function"
        fun(*args, **kwargs)
    return decorator


@log_decorator
def fun(*args, **kwargs):
    print args
    print kwargs
    print fun.__dict__
    print fun.__name__
    pass


##############################
def use_logging(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s, func name: %s" % (name, foo.__name__))


def fun_test():
    fun(1, 2, 3, 4)
    fun(x=1, y=2)
    fun(1, 2, x="x", y="y")
    fun("a", 1, None, x="x", y="y")


if __name__ == "__main__":
    # fun_test()
    foo()
