# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root1 , root2) -> List[int]:
            if not  root1 and not root2:
                return True
            if not root1:
                return False
            if not root2:
                return False 

            if root1.val != root2.val:
                print(root1.val)
                print(root1.val)
                return False

            l= inorderTraversal(root1.left , root2.right)
            r= inorderTraversal(root2.right , root1.left)
          
            return r and l

       
        return inorderTraversal(root,root)