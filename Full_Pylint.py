"""
This module contains a function to count the occurrences of an item in a sequence.
"""

def count(sequence, item):
    """
    Count the occurrences of 'item' in 'sequence'.
    """
    count_result = 0
    for element in sequence:
        if element == item:
            count_result += 1
    return count_result

# Testing the count function
def test_count():
    """
    Test the count function with different inputs.
    """
    # Test with a list of integers
    assert count([1, 2, 3, 2, 2, 4, 2], 2) == 4, "Failed integer count test"

    # Test with a list of strings
    assert count(["apple", "banana", "apple", "orange", "apple"], "apple") == 3, "Failed string count test"

    # Test with an empty list
    assert count([], 5) == 0, "Failed empty list count test"

# Run the tests
test_count()
