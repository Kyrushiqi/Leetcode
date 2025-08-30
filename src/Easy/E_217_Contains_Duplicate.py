# Question: https://leetcode.com/problems/contains-duplicate/
# Submission: https://leetcode.com/problems/contains-duplicate/submissions/1753847361
# Neetcode Submission: https://neetcode.io/problems/duplicate-integer?list=neetcode150

# Understand: 
# If a value appears more than once, return True. False otherwise

# Plan: 
# Store values in a dictionary: int, int
# If the value already exists in dictionary then return True
# Otherwise if the value doesn't exist return False.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictInt = {}

        for num in nums: # Iterate through nums
            if num not in dictInt: # If the num is not in the dictionary, add it in
                dictInt[num] = 1
            else: # If num is in dictionary that means there's a duplicate. Return True
                return True

        return False