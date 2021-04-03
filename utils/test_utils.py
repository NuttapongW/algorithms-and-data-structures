from time import time


def test_cases_iterator(f, cases):
    """
    Iteratively test the cases with each respective expected output

    :param f: function of input -> output
    :type f: function[IN, OUT]
    :param cases: iterator of tuple of input(s) as keyword arguments and expected output
    :type cases: list[(IN, OUT)]
    :return: UNIT
    :rtype: UNIT
    """
    start = time()
    for inputs, expected in cases:
        result = f(**inputs)
        assert result == expected, f"Failed with inputs: {inputs}, expected: {expected} but got: {result}"
    print(f"Successfully test {len(cases)} cases in {round((time() - start) * 1000000)} us-> All passed")
