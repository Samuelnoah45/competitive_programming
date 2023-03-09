# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(root):
            if not root:
                return None
            if root.val > p.val and root.val > q.val:
                return search(root.left)
            if  root.val < p.val and root.val < q.val:  
                  return search(root.right)  
            else:
                return root



        return search(root)