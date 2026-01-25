# Data Structures: LRU Cache ImplementationThe Challenge: 
# Implement a Least Recently Used (LRU) Cache class with get and put methods.
# Constraints: Both operations must run in \(O(1)\) average time complexity.
# Hint: 
# You will need to combine a hash map (dictionary) for fast lookups with a doubly 
# linked list to track the order of use. Alternatively, explore how collections.
# OrderedDict can be used to solve this efficiently.

from collections import OrderedDict

