# Question: 1929. Concatenation of Array
# Submission: https://leetcode.com/problems/concatenation-of-array/submissions/1911721472/ 
# Neetcode: https://neetcode.io/problems/concatenation-of-array/history?submissionIndex=1
'''
Understand: 
int array nums (length of n)
ans = concatenation of 2 nums arrays.

Plan: 
Space: O(n)
- Create empty array -- ans (length of 2n)
- for loop iterate through nums once --> O(n)
    - ans[i] == nums[i]
    - ans[i + n] == nums[i]
- Return ans
'''

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for j in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans
