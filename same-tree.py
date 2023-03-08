# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkSimilarity(root1 ,root2):
            if not root1 and not root2:
                return True
            if not root1:
                return False
            if not root2:
                return False
            if root2.val != root1.val:
                return False
            r = checkSimilarity(root1.right ,root2.right)
            l = checkSimilarity(root1.left ,root2.left)
        
            return l and r

        return  checkSimilarity(p,q)