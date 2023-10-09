# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        
        def dfs(node, subSum, subPaths, res):
            if not node:
                return []
            if not node.left and not node.right and subSum == 0:
                res.append(subPaths)
            if node.left:
                dfs(node.left, subSum - node.left.val, subPaths + [node.left.val], res)
            if node.right:
                dfs(node.right, subSum - node.right.val, subPaths + [node.right.val], res)
        
        dfs(root, sum - root.val, [root.val], res)
        
        return res