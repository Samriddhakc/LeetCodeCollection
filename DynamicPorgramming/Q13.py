"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

"""


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):

        self.cache = {}

    def allPossibleFBT(self, n):

        if n == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        if n in self.cache:
            return self.cache[n]

        allBst = []

        for x in range(n):
            for l in self.allPossibleFBT(x):
                for r in self.allPossibleFBT(n - x - 1):
                    new_node = TreeNode(0)
                    new_node.left = l
                    new_node.right = r
                    allBst.append(new_node)

        self.cache[n] = allBst

        # Wihtout cache,
        # x = (1,....n )n c x = O ( 2 ^ n ) time. O(2^N) space.
        # O( )