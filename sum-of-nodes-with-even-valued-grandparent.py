# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def findParent(root):
            if not root:
                return 
            
            if root.val %2 == 0:
                calcu(root.left)
                calcu(root.right)
                print(root.val)

            findParent(root.left)
            findParent(root.right)

        def calcu(subRoot):
            nonlocal ans
            if not subRoot:
                return 
            if subRoot.left:
                ans += subRoot.left.val
            if subRoot.right:
                ans += subRoot.right.val

        findParent(root)  

        return ans