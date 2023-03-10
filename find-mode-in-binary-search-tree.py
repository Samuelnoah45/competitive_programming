# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnts = defaultdict(int)
        mv = 0
        
        def helper(node):
            nonlocal mv
            if not node:
                return
            cnts[node.val] += 1
            mv = max(mv, cnts[node.val])
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return [k for k,v in cnts.items() if v == mv]