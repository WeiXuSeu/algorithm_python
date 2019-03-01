import unittest


def radix_sort(list_int, max_digit):
    if list_int is None or max_digit is None or max_digit < 1 or len(list_int) <= 1:
        return
    base = 1
    for index in range(1, max_digit+1):
        bucket_list = [[] for i in range(10)]
        for item in list_int:
            bucket_index = (item/base) % 10
            bucket_list[bucket_index].append(item)
        base *= 10
        list_int_index = 0
        for bucket in bucket_list:
            for item in bucket:
                list_int[list_int_index] = item
                list_int_index += 1


class RadixSort(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        radix_sort(list_int, None)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        radix_sort(list_int, 1)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [4, 3, 10, 23, 1000, 54, 100, 101]
        radix_sort(list_int, 4)
        self.assertListEqual(list_int, [3, 4, 10, 23, 54, 100, 101, 1000])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        radix_sort(list_int, 1)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        radix_sort(list_int, 1)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()