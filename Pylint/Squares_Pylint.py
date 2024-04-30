# pylint: disable=invalid-name

def list_of_squares(n):

    result = {}
    for i in range(1, n + 1):
        result[i] = i * i
    return result

def test_list_of_squares():

    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, "Incorrect squares"

    assert list_of_squares(0) == {}, "Empty dictionary expected for n = 0"

    try:
        list_of_squares(-5)
    except ValueError:
        pass
    else:
        assert False, "list_of_squares with negative n should raise a ValueError"


test_list_of_squares()

#pylint Squares_Pylint.py
