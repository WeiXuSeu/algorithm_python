import unittest


def heap_down(place, list_int, list_len):
    parent = place
    while parent < len(list_int):
        left_child = 2 * parent + 1
        if left_child < list_len and left_child + 1 < list_len:
            if list_int[left_child] < list_int[left_child+1]:
                max_child_index = left_child + 1
            else:
                max_child_index = left_child
        elif left_child < list_len:
            max_child_index = left_child
        else:
            break
        if list_int[max_child_index] > list_int[parent]:
            list_int[max_child_index], list_int[parent] = list_int[parent], list_int[max_child_index]
        else:
            break
        parent = max_child_index


def build_heap(list_int):
    if list_int is None or len(list_int) <= 1:
        return list_int
    first_parent_index = (len(list_int) - 1)/2
    for index in range(first_parent_index, -1, -1):
        heap_down(index, list_int, len(list_int))
        pass


def heap_sort(list_int):
    if list_int is None or len(list_int) <= 1:
        return list_int
    build_heap(list_int)
    for index in range(len(list_int)-1, 0, -1):
        list_int[index], list_int[0] = list_int[0], list_int[index]
        heap_down(0, list_int, index)


class HeapSortTest(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        heap_sort(list_int)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        heap_sort(list_int)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [2, 1, 3]
        heap_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        heap_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        heap_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
