# Question: https://leetcode.com/problems/contains-duplicate-ii/
# Submission: https://leetcode.com/problems/contains-duplicate-ii/submissions/1889245809/
'''
Understand: 
Given integer array - nums and integer - k
Goal: 
Find 2 different indices from nums that satisfy 2 conditions: 
1) The values of the indices are equal
2) abs(i-j) <= k

Example Walkthroughs:
i = 0
j = 3
|0-3| = 3, 3 <= 3 -- True

i = 0
j = 2
|0-2| = 2, 2 <= 1 -- False
i = 0
j = 3
|0-3| = 3, 3 <= 1 -- False
i = 2 
j = 3
|2-3| = 1, 1 <= 1 -- True

i = 0
j = 3
|0-3| = 3, 3 <= 2 -- False
i = 1 
j = 4
|1-4| = 3, 3<= 2 -- False
i = 2
j = 5
|2-5| = 3, 3 <= 2 -- False

Plan: 
1) Create an empty dictionary to store seen keys. (Keys - elements from num, Values - index)
2) Iterate through nums list by index using for loop. 
    If key is new, add it to the map. If key is in map, check abs condition. 
    If abs condition true, return True. Else, replace the value at that key to the current index. 

'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seenDict = {} 
        for index in range(len(nums)): 
            if nums[index] not in seenDict: 
                seenDict[nums[index]] = index
            else:
                # i = index in the map, j = current index whose value is a duplicate
                if abs(seenDict[nums[index]] - index) <= k: 
                    return True
                else: 
                    seenDict[nums[index]] = index
        return False

# [1, 0, 1, 1], k = 1
# The brute force method is to compare every single duplicate value with one another. 
# For example, index 0 with index 2 THEN index 0 with index 3. 
# But what is the point of checking the other values when the first comparison doesn't work already, the distance is greater for the second comparison. 
# EX: the distance of index 0 to index 2 is 2 which is already above the k value. The distance of index 0 to index 3 is 3 which is even higher than the 
# first comparison and is ofc above the k value as well since the first smaller comparison doesn't return True. So it is unecessary to check the further indexes.
# Instead we should replace the current i, index 0, to the current j, index 2. 