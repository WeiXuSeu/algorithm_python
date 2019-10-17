import unittest


def partition_sort(list_int, start, end):
    if list_int is None:
        return
    if start == end:
        return start
    little_right = start
    for index in range(start+1, end+1):
        if list_int[index] < list_int[start]:
            little_right += 1
            if index != little_right:
                list_int[index], list_int[little_right] = list_int[little_right], list_int[index]
    list_int[start], list_int[little_right] = list_int[little_right], list_int[start]
    return little_right


def quick_sort(list_int, start, end):
    if list_int is None or start is None or end is None or end <= start:
        return
    partition_index = partition_sort(list_int, start, end)
    quick_sort(list_int, start, partition_index-1)
    quick_sort(list_int, partition_index+1, end)


class QuickSort(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        quick_sort(list_int, None, None)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        quick_sort(list_int, 0, 0)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [4, 3, 5, 2, 7, 1]
        quick_sort(list_int, 0, 5)
        self.assertListEqual(list_int, [1, 2, 3, 4, 5, 7])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        quick_sort(list_int, 0, 3)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        quick_sort(list_int, 0, 3)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()