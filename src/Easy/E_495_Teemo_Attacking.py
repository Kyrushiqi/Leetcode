# Question: https://leetcode.com/problems/teemo-attacking/
# Submission: https://leetcode.com/problems/teemo-attacking/submissions/1911721472/ 
'''
Teemo attacks Ashe. Ashe poisoned [duration] seconds.
t = time series => [t, t + duration - 1] --> poison effect time interval?
Teemo attacks Ashe again, before poison effect ends. timer is reset. poison effect will end [duration] seconds.

Given: non-decreasing int array (timeSeries) and integer (duration)
timeSeries[i] == at what second is Ashe poisoned
duration = how long Ashe is poisoned for

Return: int -> total number of seconds that Ashe is poisoned.

Plan: Time limit exceeded
- create an empty set to store the seconds that Ashe is poisoned.
- iterate through timeSeries by elements
    - add num into arr
    - for e in range(poison, duration): 
        add e into arr

- Return len(arr)

Plan 2: Incorrect
- countSeconds = 0
- p1 = 0
- p2 = 1
- iterate through timeSeries by index
    if index + 1 in range(poisonTimeStart, poisonTimeStart + duration): 
        countSeconds += 1
    else 
        countSeconds += duration

Plan 3: Works
- count = 0
- iterate through timeSeries by index
    - find the difference between the current element and the next element.
    - add the minimum of gap vs duration. (Duration is the maximum amount of seconds you can add to count. gap time is the amount of seconds that occurs between the overlapping attacks)

- add duration to count -- signifies the full duration of the last second in timeSeries.
- return count
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0

        for i in range(len(timeSeries)-1): 
            gap = timeSeries[i + 1] - timeSeries[i]
            count += min(gap, duration)
        
        count += duration # full duration of last attack
        return count

        
        # Plan 1: 
        # result = set()

        # for poisonTimeStart in timeSeries: 
        #     # print(f"PoisonTimeStart: {poisonTimeStart}")
        #     for e in range(poisonTimeStart, (poisonTimeStart + duration)): 
        #         result.add(e)
        #         # print(f"Current Result: {result}")

        # return len(result)