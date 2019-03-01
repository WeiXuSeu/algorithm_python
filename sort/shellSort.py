import unittest


def shell_sort(list_int=None):
    if list_int is None:
        return
    gap = len(list_int) / 2
    while gap > 0:
        for i in range(gap, len(list_int)):
            j = i
            while j >= gap and list_int[j] < list_int[j-gap]:
                list_int[j], list_int[j-gap] = list_int[j-gap], list_int[j]
                j -= gap
        gap = gap / 2


class ShellSortTest(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        shell_sort(list_int)
        self.assertEquals(list_int, None)

    def test_input_one(self):
        list_int = [1]
        shell_sort(list_int)
        self.assertListEqual(list_int, [1])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        shell_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        shell_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_unsort(self):
        list_int = [1, 7, 2, 4]
        shell_sort(list_int)
        self.assertListEqual(list_int, [1, 2, 4, 7])


if __name__ == "__main__":
    unittest.main()
