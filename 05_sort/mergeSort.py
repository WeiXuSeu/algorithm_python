import unittest


def merge_core(sub_list1, sub_list2):
    sum_list = []
    index1 = 0
    index2 = 0
    if sub_list1 is None:
        return sub_list2
    if sub_list2 is None:
        return sub_list1
    while index1 < len(sub_list1) and index2 < len(sub_list2):
        if sub_list1[index1] <= sub_list2[index2]:
            sum_list.append(sub_list1[index1])
            index1 += 1
        else:
            sum_list.append(sub_list2[index2])
            index2 += 1
    while index1 < len(sub_list1):
        sum_list.append(sub_list1[index1])
        index1 += 1
    while index2 < len(sub_list2):
        sum_list.append(sub_list2[index2])
        index2 += 1
    return sum_list


def merge_sort(list_int):
    if list_int is None:
        return
    if len(list_int) <= 1:
        return list_int
    mid = len(list_int)/2
    sub_list_left = merge_sort(list_int[0:mid])
    sub_list_right = merge_sort(list_int[mid:len(list_int)])
    return merge_core(sub_list_left, sub_list_right)


class MergeSortTest(unittest.TestCase):
    def test_input_none(self):
        list_int = None
        out_put = merge_sort(list_int)
        self.assertEquals(out_put, None)

    def test_input_one(self):
        list_int = [1]
        out_put = merge_sort(list_int)
        self.assertListEqual(out_put, [1])

    def test_input_increase(self):
        list_int = [1, 2, 3, 4]
        out_put = merge_sort(list_int)
        self.assertListEqual(out_put, [1, 2, 3, 4])

    def test_input_decrease(self):
        list_int = [4, 3, 2, 1]
        out_put = merge_sort(list_int)
        self.assertListEqual(out_put, [1, 2, 3, 4])

    def test_input_unsort(self):
        list_int = [1, 7, 2, 4]
        out_put = merge_sort(list_int)
        self.assertListEqual(out_put, [1, 2, 4, 7])


if __name__ == "__main__":
    unittest.main()






