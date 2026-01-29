# LeetCode Problem: 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

# Example 2:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10

# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for i in accounts:
            sum_wealth = sum(i)
            if sum_wealth > max_wealth:
                max_wealth = sum_wealth
        return max_wealth
    

maximumWealth = Solution().maximumWealth
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

