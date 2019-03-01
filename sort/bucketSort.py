import unittest
from insertSort import insert_sort


def bucket_sort(list_int, bucket_num):
    default_bucket_num = 3
    if list_int is None:
        return
    real_bucket_num = bucket_num if bucket_num is not None else default_bucket_num
    bucket_list = [[] for i in range(real_bucket_num)]
    min_value = max_value = list_int[0]
    for item in list_int:
        if item > max_value:
            max_value = item
        elif item < min_value:
            min_value = item
    gap = (max_value - min_value + 1) / real_bucket_num
    for item in list_int:
        bucket_index = (item-min_value)/gap
        bucket_list[bucket_index].append(item)
    for bucket in bucket_list:
        insert_sort(bucket)
    index = 0
    for bucket in bucket_list:
        for item in bucket:
            list_int[index] = item
            index += 1


class BucketSort(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        bucket_sort(list_int, 1)
        self.assertEquals(list_int, None)

    def test_list_one(self):
        list_int = [1]
        bucket_sort(list_int, 1)
        self.assertListEqual(list_int, [1])

    def test_input_unsort(self):
        list_int = [4, 3, 5, 2, 7, 1]
        bucket_sort(list_int, 7)
        self.assertListEqual(list_int, [1, 2, 3, 4, 5, 7])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        bucket_sort(list_int, 4)
        self.assertListEqual(list_int, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        bucket_sort(list_int, 4)
        self.assertListEqual(list_int, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()




