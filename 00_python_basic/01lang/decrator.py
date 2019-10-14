# -*- utf-8 -*-
from functools import wraps
import logging


"""
step1: no function  wraps 
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)   # output --> ('wrapper', 'decorator')


"""
step2: with function wraps
"""


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')


print(example.__name__, example.__doc__)  # ('example', 'Docstring')


"""
step3: decorator with parameters 
"""


def use_logging(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s, func name: %s" % (name, foo.__name__))
