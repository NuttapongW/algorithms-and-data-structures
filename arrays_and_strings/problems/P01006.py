"""
Question 1.6
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3.
If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    ({"string": "abcdefg"}, "abcdefg"),
    ({"string": "aabbccddeeffg"}, "a2b2c2d2e2f2g1"),
    ({"string": "aabbccddeeff"}, "a2b2c2d2e2f2"),
    ({"string": "aAbBcCdDeEfF"}, "aAbBcCdDeEfF"),
    ({"string": "aabcccccaaa"}, "a2b1c5a3"),
    ({"string": "abcdefgfedcba"}, "abcdefgfedcba"),
    ({"string": "aabbccddeefffgg"}, "a2b2c2d2e2f3g2")
]


def string_compression(string: str) -> str:
    size = len(string)
    all_one = True
    cum_current = 0
    cum_string = []
    for i in range(size):
        current = string[i]
        cum_current += 1
        if i == size - 1 or current != string[i+1]:
            cum_string.extend([current, str(cum_current)])
            if all_one and cum_current > 1:
                all_one = False
            cum_current = 0
    return string if all_one else "".join(cum_string)


if __name__ == '__main__':
    test_cases_iterator(string_compression, TEST_CASE)
