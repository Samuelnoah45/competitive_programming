# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validation(root):
            arr = []
            if root == None:
                return  []
        
            arr.extend(validation(root.left))
            arr.append(root.val)
            arr.extend(validation(root.right))
            return arr

        newArr = validation(root)
        for i in range(len(newArr)-1):
            if newArr[i] >= newArr[i+1]:
                return False

        return True

            
            
            
            
            