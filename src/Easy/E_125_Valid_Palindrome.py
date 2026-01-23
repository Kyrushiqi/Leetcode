# Question: https://leetcode.com/problems/valid-palindrome/
# Submission: https://leetcode.com/problems/valid-palindrome/submissions/1894659100/
# Neetcode Submission: https://neetcode.io/problems/is-palindrome/history

# Understand: 
# Given string s, determine if it is a palindrome
# Return type: Boolean

# Plan: 
# 1) Remove any non alphanumerical characters using Regex Expression. 
# 2) Remove all whitespace in between the strings and convert all characters to lowercase.
# 3) Use 2 pointer technique. Pointer 1 at beginning of string, the other at the end of the string. 
# 4) while the 2 pointers don't cross each other, continuously check: 
#       a) if the characters are the same, move both pointers 1 step inwards
#       b) if the characters aren't the same, return false

# Edge Case: 
# Do we consider the whitespace? No, only alphanumerical characters
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s) # Regex Expression
        s = s.lower().replace(" ", "")
        print(s)
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2: 
            if s[p1] != s[p2]: 
                return False
            elif s[p1] == s[p2]: 
                p1 += 1
                p2 -= 1

        return True