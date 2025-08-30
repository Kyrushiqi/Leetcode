# Question: https://leetcode.com/problems/valid-anagram/
# Submission: https://leetcode.com/problems/valid-anagram/submissions/1753805957
# Neetcode Submission: https://neetcode.io/problems/is-anagram?list=neetcode250 

# Completed in 1hr 7mins due to being unfamiliar with Python Syntax :'D
# Better Solution: Sort the Strings and compare them.

# Understand: 
# Determine if Strings are a valid anagram. 
# Return type: Boolean, true if the characters match one another. 
# Order of characters can be different.

# Plan: 
# 1) Create 2 Dictionaries to store the strings s and t.
#       - Dictionary (String, int)
# 2) Compare the 2 dictionaries to see if characters match up.

class Solution: # O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False

        # Not in vs is Not --> The Problem
        for char in s: 
            if char not in sDict: 
                sDict[char] = 1
            else: # if char is in the dictionary, append 1
                sDict[char] += 1
        
        for char in t: 
            if char not in tDict: 
                tDict[char] = 1
            else: # if char is in the dictionary, append 1
                tDict[char] += 1

        for ch in sDict: # Compare the 2 dictionaries,
            # Doesn't work here for some reason...
            # if sDict.get(char) != tDict.get(char):
            #     return False
            
            # My solution also works:
            if not (ch in tDict and sDict[ch] == tDict[ch]):
                return False
            

        # s - b:2, c:2
        # t - c:3, b:1

        return True
