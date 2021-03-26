"""
Question 1.2
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
"""

from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    ({"s1": "abcd", "s2": "dbac"}, True),
    ({"s1": "aaa", "s2": "abc"}, False),
    ({"s1": "abcd", "s2": "dbac"}, True),
    ({"s1": "abcdefghijk", "s2": "fhjdbacegik"}, True),
    ({"s1": "abcdefghijk", "s2": "fhjdbacegi"}, False),
    ({"s1": "abcdefghijk", "s2": "fhjdbacegia"}, False)
]


def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    else:
        _map = {}
        for ch in s1:
            _map.update({ch: (_map.get(ch) if _map.get(ch) else 0) + 1})
        for ch in s2:
            if _map.get(ch) is None:
                return False
            else:
                _map.update({ch: _map.get(ch) - 1})
        for k in _map:
            if _map[k] != 0:
                return False
        return True


if __name__ == '__main__':
    test_cases_iterator(check_permutation, TEST_CASE)
