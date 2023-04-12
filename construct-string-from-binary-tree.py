# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        def dfs(root):
            if not root:
                return ""
            return str(root.val) + "(" + dfs(root.left)+ ")" + "(" + dfs(root.right) + ")"
            
        newStr = dfs(root).replace("()()" ,"")
        newStr = newStr.replace(")()" ,")")
        return newStr