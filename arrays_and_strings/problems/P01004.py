"""
Question 1.4
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)
"""

from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    ({"string": "abcdefg"}, False),
    ({"string": "aabbccddeeffg"}, True),
    ({"string": "aabbccddeeff"}, True),
    ({"string": "aAbBcCdDeEfF"}, True),
    ({"string": "Tact Coa"}, True),
    ({"string": "Tact Coach"}, False)
]


def palindrome_permutation(string: str) -> bool:
    string_lower = string.lower()
    _map = {}
    for ch in string_lower:
        if ch != " ":
            _map.update({ch: (_map.get(ch) if _map.get(ch) else 0) + 1})
    already_odd = False
    for k in _map:
        if _map[k] % 2 == 1:
            if not already_odd:
                already_odd = True
            else:
                return False
    return True


if __name__ == '__main__':
    test_cases_iterator(palindrome_permutation, TEST_CASE)
