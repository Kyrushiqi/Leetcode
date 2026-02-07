# Question: https://leetcode.com/problems/two-sum/
# Submission: https://leetcode.com/problems/two-sum/submissions/1911721472/
# Neetcode Submission: https://neetcode.io/problems/two-integer-sum/history

'''
Understand: 
Given: array of ints (nums), integer (target)
Goal: Add 2 indices together to equal the target
Return: list of indices (ints), Return smaller index first.

Assumptions: 
- There's only 1 solution to the problem. Exactly one pair of i and j.

Plan: 
Brute Force: 
- 2 pointers
Pointer 1 stays at a certain index until Pointer 2 iterates to the end of the array. 
If the sum of Pointer 1 and Pointer 2 doesn't equal to target. Then move pointer1 to the right.
1) Declare 2 pointers: p1 = 0, p2 = p1+1
2) Iterate through the array, nums by index
3) if nums[p1] + nums[p2] = target:
    return [p1, p2]
   elif p2 == len(nums) - 1:
    p1 += 1
    p2 = p1 + 1

Dictionary: Keys: int (indices), Values: ints (values of the nums)
Target - nums[i] = nums[j]
1) Create an empty dictionary
2) Iterate through the list, nums. And input nums into a dictionary. 
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # [2, 5, 5, 11], [1, 2], target = 10
        #  0  1  2  3
        # [2, 5, 5, 11]
        # [-1, -2, -3, -4, -5], Target = -8, [2,4]
        
        p1 = 0 # 1
        p2 = p1 # 2

        while p1 != len(nums) - 1: # index: 3
            p2 += 1
            if nums[p1] + nums[p2] == target: 
                print(p1, p2)
                return [p1, p2]

            elif p2 == len(nums) - 1: # len = 3
                p1 += 1
                p2 = p1 + 1
                if nums[p1] + nums[p2] == target: 
                    return [p1, p2]

        return []
        