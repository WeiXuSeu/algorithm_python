"""
(1, 2, 3, 4)
{}
{}
fun
()
{'y': 2, 'x': 1}
{}
fun
(1, 2)
{'y': 'y', 'x': 'x'}
{}
fun
('a', 1, None)
{'y': 'y', 'x': 'x'}
{}
fun
"""


def fun(*args, **kwargs):
    print args
    print kwargs
    print fun.__dict__
    print fun.__name__
    pass


def fun_test():
    # args
    fun(1, 2, 3, 4)
    # kws
    fun(x=1, y=2)
    # args + kws
    fun(1, 2, x="x", y="y")
    fun("a", 1, None, x="x", y="y")


if __name__ == "__main__":
    fun_test()
    pass
