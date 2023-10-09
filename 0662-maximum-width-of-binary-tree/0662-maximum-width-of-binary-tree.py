class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node, level, col):
            if node is None:
                return 
            else:
                if level in ans:
                    ans[level]['min'] = min(ans[level]['min'], col)
                    ans[level]['max'] = max(ans[level]['max'], col)
                else:
                    ans[level] = dict()
                    ans[level]['min'] = col
                    ans[level]['max'] = col
                helper(node.left, level+1, 2*col)
                helper(node.right, level+1, 2*col+1)
                
        ans = dict()
        helper(root, 0, 0)
        max_width=0
        for i in ans.keys():
            max_width = max(max_width, 1+ans[i]['max']-ans[i]['min'])
        return max_width    