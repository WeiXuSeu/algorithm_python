import unittest


def select_sort(list_int = None):
    if list_int is None:
        return
    for i in range(0, len(list_int)-1):
        min_value = list_int[i]
        min_index = i
        for j in range(i+1, len(list_int)):
            if list_int[j] < min_value:
                min_value = list_int[j]
                min_index = j
        list_int[i], list_int[min_index] = list_int[min_index], list_int[i]


class SelectSortTest(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        select_sort(list_int)
        self.assertEquals(list_int, None)

    def test_input_one(self):
        list_int = [1]
        select_sort(list_int)
        self.assertListEqual(list_int, [1])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4, 5]
        select_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4, 5])

    def test_input_decrease(self):
        list_int = [5, 4, 3, 2, 1, -1]
        select_sort(list_int)
        self.assertListEqual(list_int, [-1, 1, 2, 3, 4, 5])

    def test_input_unsort(self):
        list_int = [4, 3, 5, 1, 2]
        select_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()