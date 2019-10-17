import unittest


def insert_sort(list_int=None):
    if list_int is None:
        return
    for i in range(1, len(list_int)):
        j = i
        while j > 0 and list_int[j] < list_int[j-1]:
            list_int[j], list_int[j-1] = list_int[j-1], list_int[j]
            j -= 1


class InsertSortTest(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        insert_sort(list_int)
        self.assertEquals(list_int, None)

    def test_input_one(self):
        list_int = [1]
        insert_sort(list_int)
        self.assertListEqual(list_int, [1])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        insert_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        insert_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_unsort(self):
        list_int = [1, 7, 2, 4]
        insert_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 4, 7])


if __name__ == "__main__":
    unittest.main()
