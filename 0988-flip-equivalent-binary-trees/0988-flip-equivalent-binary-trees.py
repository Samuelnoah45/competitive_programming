# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.isPartialFlip(root1, root2)

    def isPartialFlip(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if self.isSameNode(n1, n2):
            if not n1 and not n2:
                return True
            p1 = self.isPartialFlip(n1.left, n2.left) and self.isPartialFlip(n1.right, n2.right)
            p2 = self.isPartialFlip(
                n1.left, n2.right) and self.isPartialFlip(n1.right, n2.left)
            return p1 or p2

        return False

    def isSameNode(self, n1: TreeNode, n2: TreeNode) -> bool:
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val == n2.val