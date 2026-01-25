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


