import unittest


def bubble_sort(list_int=None):
    """
    description: bubble sort
        in each loop, make sure the largest one pop up from the  left list;
    :param list_int:
    :return:
    """
    if list_int is None:
        return
    for i in range(0, len(list_int) - 1):
        for j in range(0, len(list_int)-1-i):
            if list_int[j] > list_int[j+1]:
                list_int[j], list_int[j+1] = list_int[j+1], list_int[j]


class BubbleSortTestCase(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        bubble_sort(list_int)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        bubble_sort(list_int)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [2, 1, 3]
        bubble_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        bubble_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        bubble_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

