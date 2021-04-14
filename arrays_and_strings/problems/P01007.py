"""
Question 1.8
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
"""

from utils.test_utils import test_cases_iterator

NUM_CHARS = 128
CHAR_SET = {chr(i) for i in range(NUM_CHARS)}
TEST_CASE = [
    (
        {
            "array_string": """1 2 3 4 6 0 5 0 3
            2 1 5 5 1 2 2 2 2
            0 4 6 0 1 0 8 0 0"""
        },
        """0 0 0 0 0 0 0 0 0
        0 1 5 0 1 0 2 0 0
        0 0 0 0 0 0 0 0 0"""
    ),
]


def transform_array_string(array_as_string) -> list:
    lines = [[int(item) for item in line.split()] for line in array_as_string.split("\n")]
    num = None
    for line in lines:
        if num is None:
            num = len(line)
        else:
            assert num == len(line) , f"{num} vs {line}"
    return lines


def transform_array(array):
    return "\n".join([" ".join([str(i) for i in line]) for line in array])


def zero_matrix(array_string) -> str:
    array = transform_array_string(array_string)
    dim_0 = len(array)
    dim_1 = len(array[0])
    row_set = set({})
    col_set = set({})
    for row in range(dim_0):
        for col in range(dim_1):
            if array[row][col] == 0:
                row_set.add(row)
                col_set.add(col)
    for row in row_set:
        for col in range(dim_1):
            array[row][col] = 0
    for col in col_set:
        for row in range(dim_0):
            array[row][col] = 0

    return transform_array(array)


if __name__ == '__main__':
    test_cases_iterator(zero_matrix, TEST_CASE, transform_array_string)
