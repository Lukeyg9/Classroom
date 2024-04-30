# pylint: disable=invalid-name

def fact(x):

    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():

    # Test with 0
    assert fact(0) == 1, "Factorial of 0 should be 1"
    
    assert fact(5) == 120, "Factorial of 5 should be 120"
    
    try:
        fact(-5)
    except ValueError:
        pass
    else:
        assert False, "Factorial of a negative number should raise a ValueError"


test_fact()

# pylint Factorial_Pylint.py
