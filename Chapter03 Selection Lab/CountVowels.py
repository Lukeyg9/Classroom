word = input("Enter a word: ")

vowel_count = 0

for char in word:
    if char.lower() in 'aeiou':
        vowel_count += 1

print("The number of vowels in the word '{}' is: {}".format(word, vowel_count))
