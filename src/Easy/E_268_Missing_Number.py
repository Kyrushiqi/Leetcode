# Question: https://leetcode.com/problems/missing-number/
# Submission: https://leetcode.com/problems/missing-number/submissions/1911721472/ 
# Neetcode Submission: https://neetcode.io/problems/missing-number/history 
'''
Understand: 
Given array (nums) 
Find what is the missing number

Plan: 
- sort the nums array O(n)
- iterate over the sorted array and if i == a certain #, return i

Edge case: 
- [] return -- always guarantee

- n == nums.length
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort() # O(n)
        print(nums)
        
        for i in range(len(nums) + 1): # 0, 2
            if i not in nums:
                return i
