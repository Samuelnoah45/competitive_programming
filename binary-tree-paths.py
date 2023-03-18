# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        arr = []
        p = ""
        def inorder(root ,arr , p):
            if not root:
                return 
            if not root.left and not root.right:
                arr.append(p+str(root.val))
            p = p+str(root.val) + "->"
            
            inorder(root.left , arr ,p)
            inorder(root.right , arr ,p)
        inorder(root ,arr ,p)

        return arr

            

            
            
            
            
            
            
            
            
         




        return []