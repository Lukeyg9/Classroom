# pylint: disable=invalid-name

def list_of_squares(n):
    """
    Generate a dictionary containing squares of numbers from 1 to n.
    """
    result = {}
    for i in range(1, n + 1):
        result[i] = i * i
    return result

def test_list_of_squares():
    """
    Test list_of_squares function with different inputs.
    """
    # Test with n = 5
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, "Incorrect squares"

    # Test with n = 0
    assert list_of_squares(0) == {}, "Empty dictionary expected for n = 0"

    # Test with n = -5 (this should raise a ValueError)
    try:
        list_of_squares(-5)
    except ValueError:
        pass
    else:
        assert False, "list_of_squares with negative n should raise a ValueError"

# Run the tests
test_list_of_squares()
