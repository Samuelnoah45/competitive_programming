"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        def dfs(node ,count):
            nonlocal ans
            if not node:
                return 
            if   not node.children:
                ans = max(ans ,count +1)
                return
            count += 1
            for child in node.children:
                dfs(child ,count)

        dfs(root ,0)

        return ans