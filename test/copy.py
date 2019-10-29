def sub_fun(str1, list1):
    print id(str1), id(list1)


def fun():
    str1 = "abc"
    list1 = ["abc", "def"]
    print id(str1), id(list1)
    sub_fun(str1, list1)


if __name__ == "__main__":
    fun()