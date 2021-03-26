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

    def recursive(remain, prefix=list([])):
        _size = len(remain)
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


def quick_sort(array, f, shuffle=True):
    """
    Sort the input array and return the new object. Average runtime complexity ~O(N log N)

    :param array: list of items to sort
    :type array: list[ITEM]
    :param f: f(A, B) both of type ITEM, return True when A should be sorted before B and vice versa False
    :type f: f[(ITEM, ITEM), bool]
    :param shuffle: to shuffle the input before sort or not (need only highest recursive call)
    :type shuffle: bool
    :return: list of sorted items
    :rtype: list[ITEM]
    """

    size = len(array)
    if size <= 1:
        return array
    else:
        arr = copy.deepcopy(array)
        if shuffle:
            random.shuffle(arr)
        i_before = 0
        i_pivot = size - 1
        pivot = arr[i_pivot]

        while i_before < i_pivot:
            while not f(arr[i_before], pivot) and i_pivot > 0:
                swap(arr, i_before, i_pivot)
                swap(arr, i_before, i_pivot - 1)
                i_pivot -= 1
            i_before += 1
            if not f(arr[i_pivot - 1], pivot) and i_pivot > 0:
                swap(arr, i_pivot, i_pivot - 1)
                i_pivot -= 1
        return quick_sort(arr[:i_pivot], f, False) + list([pivot]) + quick_sort(arr[(i_pivot + 1):], f, False)
