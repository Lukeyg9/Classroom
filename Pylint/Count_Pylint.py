# pylint: disable=invalid-name

def count(sequence, item):
    """
    Count the occurrences of 'item' in 'sequence'.
    """
    total_count = 0
    for element in sequence:
        if element == item:
            total_count += 1
    return total_count

def test_count_with_integers():
    """
    Test count function with a list of integers.
    """
    sequence = [1, 2, 3, 4, 5, 2, 2]
    item = 2
    assert count(sequence, item) == 3, "Counting integers failed"

def test_count_with_strings():
    """
    Test count function with a list of strings.
    """
    sequence = ["apple", "banana", "orange", "apple", "grape"]
    item = "apple"
    assert count(sequence, item) == 2, "Counting strings failed"


test_count_with_integers()
test_count_with_strings()

# pylint Count_Pylint.py
