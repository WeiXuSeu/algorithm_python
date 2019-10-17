import unittest

"""
>>> sys.maxint
2147483647
"""


def counting_sort(list_int, max_value):
    """
    assumption: all input item (>=0)
    :param list_int:
    :param max_value:
    :return:
    """
    if list_int is None or len(list_int) <= 1:
        return
    counting_arr = [0] * (max_value + 1)
    for item in list_int:
        counting_arr[item] += 1
    list_index = 0
    for index in range(0, max_value+1):
        while counting_arr[index] > 0:
            list_int[list_index] = index
            counting_arr[index] -= 1
            list_index += 1


class CountingSort(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        counting_sort(list_int, 1)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        counting_sort(list_int, 1)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [4, 3, 5, 2, 7, 1]
        counting_sort(list_int, 7)
        self.assertListEqual(list_int, [1, 2, 3, 4, 5, 7])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        counting_sort(list_int, 4)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        counting_sort(list_int, 4)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()