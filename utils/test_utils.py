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
    for input, expected in cases:
        result = f(**input)
        assert result == expected, f"Failed with input: {input}, expected: {expected} but got: {result}"
