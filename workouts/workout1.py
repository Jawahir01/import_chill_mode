# Algorithms: The "Anagram Grouper"
# 
# The Challenge: 
# Write a function that takes a list of strings and groups anagrams together
# .Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
# Key Concept: Use a dictionary where the key is a sorted version of the string
# or a character count tuple to achieve
# '
# \(O(n\cdot k\log k)\) or \(O(n\cdot k)\) time complexity.
# ' 

from ast import Return
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the string to create a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strs))



# Explanation:
# 1. 
# We import defaultdict(list) which automatically creates an empty list when a new key is accessed, 
# so we don’t need to check if the key exists.
# 2. 
# We define a function that takes a list of strings as input.
# 3. 
# We Create dictionary
#     anagrams = defaultdict(list)
# This will store:
#     key   → list of words
# Where the key represents the sorted letters of a word.
# 4.
# We iterate through each string in the input list.
# 5.
# We create a key using sorted letters
#     key = ''.join(sorted(s))

# | Word | Sorted | Key   |
# | ---- | ------ | ----- |
# | eat  | aet    | "aet" |
# | tea  | aet    | "aet" |
# | tan  | ant    | "ant" |
# | ate  | aet    | "aet" |
# | nat  | ant    | "ant" |
# | bat  | abt    | "abt" |
#     *note*: All anagrams produce the same key.
# 6.
# Store the word under its key
# anagrams[key].append(s)


# Groups words that share the same sorted key.

# Dictionary becomes:

# {
#   "aet": ["eat", "tea", "ate"],
#   "ant": ["tan", "nat"],
#   "abt": ["bat"]
# }

# 7. 
# Return the grouped lists
#     return list(anagrams.values())
# Returns only the groups, not the keys.