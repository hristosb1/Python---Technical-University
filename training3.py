# Given a nested list, flatten it into a single list.
from collections import Counter, defaultdict

nested_list = [
    [1, 2, [3, 4]],
    [5, 6],
    [7, [8, 9, [10]]]
]
def flat (l):
    return_list = []
    for item in l:
        if isinstance(item, list):
            return_list.extend(flat(item))
        else:
            return_list.append(item)
    return return_list

# You are given a list of words. Count how many times each word appears in the list.
words_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
# TODO: Create a dictionary that maps each word to its count.
# Example Output: {'apple': 3, 'banana': 2, 'orange': 1}
dictionary1 = dict(Counter(words_list))
dictionary2 = {word: words_list.count(word) for word in set(words_list)}


# Given a list of strings, remove all vowels from each string.
string_list = ["hello", "world", "python", "is", "fun"]
# TODO: Create a new list where each string has had its vowels removed.
# Example Output: ['hll', 'wrld', 'pythn', 's', 'fn']
vowels = 'aeiou'
no_vowel_list = [''.join(char for char in string if char.lower() not in vowels) for string in string_list]

# Given a list of words, group them by anagrams.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# TODO: Create a list of lists, where each sublist contains words that are anagrams of each other.
# Example Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Create a default dictionary to hold lists of anagrams
anagrams = defaultdict(list)

# Group words by sorted tuple of characters
for word in words:
    sorted_word = ''.join(sorted(word))  # Sort the characters of the word
    anagrams[sorted_word].append(word)    # Append the word to the list of its anagrams

# Convert the dictionary values to a list
grouped_anagrams = list(anagrams.values())

# Output the grouped anagrams
print(grouped_anagrams)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# You are given a list of numbers. Find the second-largest number in the list.
numbers = [10, 20, 4, 45, 99, 99]
# TODO: Write a function to return the second largest number.
# Example Output: 45
secondLargest = sorted(list(set(numbers)))[-2]
