"""
Implement different sorting algorithms, namely
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
"""

import copy
import random


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def ascending(a, b):
    return a < b


def descending(a, b):
    return a > b


def bubble_sort(array, f):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N^2)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    arr = copy.deepcopy(array)
    size = len(arr)
    counter = 0
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(size - 1):
            counter += 1
            _current = arr[i]
            _next = arr[i + 1]
            if not (f(_current, _next) or _current == _next):
                is_sorted = False
                swap(arr, i, i + 1)

    return arr


def selection_sort(array, f):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N^2)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    arr = copy.deepcopy(array)
    size = len(arr)

    def recursive(remain, prefix=None):
        _size = len(remain)
        if prefix is None:
            prefix = []
        if _size == 1:
            return prefix + remain
        else:
            swap(remain, 0, find_min_index(remain))
            return recursive(remain[1:], prefix + remain[:1])

    def find_min_index(l):
        _size = len(l)
        _min_index = None
        _min_value = None
        for pos in range(_size):
            current = l[pos]
            if _min_index is None or f(current, _min_value):
                _min_index = pos
                _min_value = current

        return _min_index

    if size < 900:
        return recursive(arr)
    else:
        for pos in range(size - 1):
            swap(arr, pos, find_min_index(arr[pos:]) + pos)
        return arr


def insertion_sort(array, f):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N^2)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    def insert_k(a, k):
        for i in range(len(a)):
            current = a[i]
            if not f(current, k) or current == k:
                return a[:i] + list([k]) + a[i:]
        return a + list([k])

    def insertion_sort_impl(a, sorted_prefix):
        return insert_k(sorted_prefix, a[0]) if len(a) == 1 else insertion_sort_impl(a[1:],
                                                                                     insert_k(sorted_prefix, a[0]))

    size = len(array)
    if size < 900:
        return insertion_sort_impl(array, [])
    else:
        sorted_prefix = []
        for i in range(size):
            current = array[i]
            sorted_prefix = insert_k(sorted_prefix, current)
        return sorted_prefix


def merge_sort(array, f):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N log N)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    def sort_two_lists(list_a, list_b):
        result = list([])
        size_a = len(list_a)
        size_b = len(list_b)
        counter_a = 0
        counter_b = 0

        while True:
            if counter_a == size_a:
                return result + list_b[counter_b:]
            elif counter_b == size_b:
                return result + list_a[counter_a:]
            else:
                current_a = list_a[counter_a]
                current_b = list_b[counter_b]
                if f(current_a, current_b) or current_a == current_b:
                    counter_a += 1
                    result.append(current_a)
                else:
                    counter_b += 1
                    result.append(current_b)

    size = len(array)
    mid = int(size / 2)
    return array if size <= 1 else sort_two_lists(merge_sort(array[:mid], f), merge_sort(array[mid:], f))


def quick_sort(array, f, inplace=True):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N log N)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :param inplace: if True, sort array inplace else return a copy of sorted array
    :type inplace: bool
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    def quick_sort_impl(arr, first, last):

        if last <= first:
            pass
        else:
            i_before = first
            i_pivot = last
            pivot = arr[i_pivot]

            while i_before < i_pivot:
                while not f(arr[i_before], pivot) and i_pivot > i_before:
                    swap(arr, i_before, i_pivot)
                    swap(arr, i_before, i_pivot - 1)
                    i_pivot -= 1
                i_before += 1
                if not f(arr[i_pivot - 1], pivot) and i_pivot > i_before:
                    swap(arr, i_pivot, i_pivot - 1)
                    i_pivot -= 1

            quick_sort_impl(arr, first, i_pivot - 1)
            quick_sort_impl(arr, (i_pivot + 1), last)

    random.shuffle(array)
    a = array if inplace else copy.deepcopy(array)
    size = len(a)
    quick_sort_impl(a, 0, size - 1)
    if not inplace:
        return a


def merge_sort_2(arr, f):
    size = len(arr)
    if size == 1:
        return arr
    else:
        mid_index = size // 2
        first_half = merge_sort_2(arr[:mid_index], f)
        first_len = mid_index
        latter_half = merge_sort_2(arr[mid_index:], f)
        latter_len = size - mid_index
        first_index = 0
        latter_index = 0
        output = []
        for _ in range(size):
            if first_index < first_len and (
                    not latter_index < latter_len or f(first_half[first_index], latter_half[latter_index])):
                output.append(first_half[first_index])
                first_index += 1
            else:
                output.append(latter_half[latter_index])
                latter_index += 1
        return output


count = 0


def quick_sort_2(arr, f, start=None, finish=None):
    start = start or 0
    finish = finish or len(arr)
    if finish - start == 1:
        pass
    else:
        front_index = start + 1
        back_index = finish - 1
        pivot_index = start
        pivot = arr[pivot_index]

        while front_index <= back_index:
            if f(arr[front_index], pivot):
                arr[front_index], arr[pivot_index] = arr[pivot_index], arr[front_index]
                front_index += 1
                pivot_index += 1
            else:
                arr[front_index], arr[back_index] = arr[back_index], arr[front_index]
                back_index -= 1

        quick_sort_2(arr, f, min(start, pivot_index + 1), max(start, pivot_index + 1))
        quick_sort_2(arr, f, min(pivot_index + 1, finish), max(pivot_index + 1, finish))


def is_sorted(arr, f):
    compared = arr[0] == arr[1] or f(arr[0], arr[1])
    return compared if len(arr) == 2 else (compared and is_sorted(arr[1:], f))


if __name__ == '__main__':
    pass
