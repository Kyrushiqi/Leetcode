# Leetcode: https://leetcode.com/problems/majority-element/submissions/2125752384/
# Neetcode: https://neetcode.io/problems/majority-element/history

'''
Understand: 
Given: array of ints (nums), size = n
Return: int -- a number from the nums array that appears more than n/2 (half of the array)
Always assume there is a majority element

Plan:
- Edge Case: [3, 3, 2, 2] -- if same number of majority elemnts then return the first majority element that's available

Plan 1: O(n)
- Create a dictionary (key - ints, value - ints(frequency)) -- O(1)
- using a for loop, iterate through nums until n (nums.length) -- O(n)
    - While iterating, update the dictionary with the frequency of elements O(1)
- another for loop iterates using items() -- O(n)
    - create maxFreq variable, majority variable
    - update the maxFreq variable whenever value > maxFreq
    - if max > n/2: update majority variable to associated key
- return majority

Edge Case: 
- Can there be 2 majority elements? Lets assume no.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = {}
        for keyElement in nums: 
            if keyElement not in majority_dict: 
                majority_dict[keyElement] = 1
            else: 
                majority_dict[keyElement] += 1

        maxFreq = -1
        majorityKey = -1
        for key, val in majority_dict.items():
            if val > maxFreq: 
                maxFreq = val
                if maxFreq > len(nums)/2: 
                    majorityKey = key

        return majorityKey

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2]
    