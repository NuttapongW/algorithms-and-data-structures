"""
Question 1.1
Is Unique: implement and algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

from utils.sort_utils import quick_sort
from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    ({"string": "abcdefghij"}, True),  # normal case
    ({"string": "a"}, True),  # single char case
    ({"string": "aaaaaaaaaa"}, False),  # normal duplicated case
    ({"string": "abab"}, False),  # normal duplicated case
    ({"string": "".join([chr(NUM_CHARS)])}, False)  # invalid char case
]


def if_all_unique(string: str, char_set=CHAR_SET) -> bool:
    char_set_size = len(char_set)
    if len(string) > char_set_size:
        return False
    else:
        seen = {}
        for ch in string:
            if seen.get(ch) is not None or not (ch in char_set):
                return False
            else:
                seen.update({ch: True})

        return True


def if_all_unique_mod(string: str, char_set=CHAR_SET) -> bool:
    def f(a, b):
        return a < b

    char_set_size = len(char_set)
    string_len = len(string)
    if string_len > char_set_size:
        return False
    else:
        sorted_string = quick_sort([ch for ch in string], f, False)
        for i in range(string_len):
            current = sorted_string[i]
            if (current not in char_set) or ((i != string_len - 1) and (current == sorted_string[i + 1])):
                return False
        return True


if __name__ == '__main__':
    test_cases_iterator(if_all_unique, TEST_CASE)
    test_cases_iterator(if_all_unique_mod, TEST_CASE)
