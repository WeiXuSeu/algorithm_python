def fun(*args, **kwargs):
    print args
    print kwargs
    print fun.__dict__
    print fun.__name__
    pass


def fun_test():
    fun(1, 2, 3, 4)
    fun(x=1, y=2)
    fun(1, 2, x="x", y="y")
    fun("a", 1, None, x="x", y="y")


if __name__ == "__main__":
    pass
