"""
Question 1.4=5
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    ({"s1": "pale", "s2": "ple"}, True),
    ({"s1": "pales", "s2": "pale"}, True),
    ({"s1": "pale", "s2": "bale"}, True),
    ({"s1": "pale", "s2": "bake"}, False),
    ({"s1": "iiabcd", "s2": "iabcd"}, True),
    ({"s1": "iiabcd", "s2": "piabcd"}, True),
    ({"s1": "iiapcd", "s2": "piabcd"}, False)
]


def is_one_away(s1: str, s2: str) -> bool:
    size_s1 = len(s1)
    size_s2 = len(s2)
    cum_diff = 0
    max_diff = 1
    if size_s1 == size_s2:
        for i in range(size_s1):
            if s1[i] != s2[i]:
                cum_diff += 1
            if cum_diff > max_diff:
                return False
        return True
    else:
        if abs(size_s1 - size_s2) <= max_diff:
            cond = size_s1 < size_s2
            shorter = s1 if cond else s2
            longer = s2 if cond else s1
            index = 0
            for ch in shorter:
                while ch != longer[index] and cum_diff <= max_diff:
                    cum_diff += 1
                    index += 1
                if cum_diff > max_diff:
                    return False
                index += 1
            return True
        else:
            return False


if __name__ == '__main__':
    test_cases_iterator(is_one_away, TEST_CASE)
