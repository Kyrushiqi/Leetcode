# Same Tree: https://leetcode.com/problems/same-tree/
# Completed Successfully within 28 mins! :DD (Part of Codepath TIP102 Mock Interview with Peer)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Understand: 
# Given 2 binary trees represented as lists p and q
# Considered same if they are structurally identical and nodes have same value.
# Return type: boolean

# Plan: (More efficient)
# Traverse through both trees 
# Recursive approach using pre-order traversal: root left right
# Base case: if the tree is None. 

# Edge cases: 
# 1) p does not exist while q exists -- return false
# 2) p and q don't exist -- return true 
# 3) p and q both exist and equal to one another -- return true

# Plan 2: 
# Create a list of each binary tree and compare the lists at the end.
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # My initial solution!
        if p and q is None:
            return False 
        if p is None and q is None:
            return True
        if p and q: 
            if p.val == q.val: # root
                if self.isSameTree(p.left, q.left): # left
                    if self.isSameTree(p.right, q.right): # right
                        return True
        return False

        # Reformatting Suggestion from partner:
        # if p and q is None:
        #     return False 
        # if p is None and q is None:
        #     return True
        # if p and q and p.val == q.val: # root
        #     if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right): # left 
        #         return True
        # return False
        