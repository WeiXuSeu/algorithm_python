#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
import logging


"""
step1: no function wraps 
"""


def my_decorator(func):
    print "before wrapper"
    def wrapper(*args, **kwargs):
        """decorator"""
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Docstring"""
    print('Called example function')

# fun: example = my_decorator(example)


print(example.__name__, example.__doc__)   # output --> ('wrapper', 'decorator')


example()   # Calling decorated function, Called example function

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

# example = my_decorator(example)


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


# foo = use_logging(level)(foo)

"""
multi decorator layer
"""


def first_decorator(func):
    print('--first--')

    def first_wrapper(*args, **kwargs):
        print('------first---%s---' % func.__name__)
        return func(*args, **kwargs)
    return first_wrapper


def second_decorator(func):
    print('--second--')

    def second_wrapper(*args, **kwargs):
        print('------second---%s---' % func.__name__)
        return func(*args, **kwargs)
    return second_wrapper


@first_decorator
@second_decorator
def test_func_1():
    import inspect
    print('excute %s' % inspect.stack()[0][3])


test_func_1()


"""

test_func_1 = first_decorator(second_decorator(test_func_1))
(1) 构造的时候，从内往外，从下往上进行构造
    构造的过程中，就会先调用每个函数之上的语句
    --second--
    --first--

(2) 调用的时候，test_func_1()
    构造过程中执行完的语句，现在可以忽略构造过程中执行的语句
    执行，从外向内执行
    ------first---second_wrapper---
    ------second---test_func_1---
    excute test_func_1
    

--second--
--first--
------first---second_wrapper---
------second---test_func_1---
excute test_func_1
"""