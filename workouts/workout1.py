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


