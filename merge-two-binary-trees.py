# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.merge(root1, root2)

    def  merge(self ,root1 , root2):

        if not root1 and not root2:
            return 
        if not root1:
            return root2
        if not root2:
            return root1
        root2.val = root1.val + root2.val

        r = self.merge(root1.right ,root2.right)
        l = self.merge(root1.left ,root2.left)

        root2.right = r
        root2.left = l

        return root2