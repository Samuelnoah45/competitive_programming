# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        arr =  0
        def recur (root):
            if root == None:
                return 0
            
            return max( recur(root.left) ,recur(root.right)) + 1

        return recur(root)

        
        
        