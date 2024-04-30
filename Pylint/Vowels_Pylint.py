# pylint: disable=invalid-name

def vowels(word):

    number_of_vowels = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in vowels_list:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels():

    assert vowels("aeiou") == 5, "Expected 5 vowels"

    assert vowels("xyz") == 0, "Expected 0 vowels"

    assert vowels("") == 0, "Expected 0 vowels for an empty string"

    assert vowels("aEiOu") == 5, "Expected 5 vowels including both upper and lower case"

# Run the tests
test_vowels()
