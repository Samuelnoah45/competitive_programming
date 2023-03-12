# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash = defaultdict(lambda: defaultdict(list))

        def recur(row,col , root):

            if not root:
                return 
                     
            hash[col][row].append(root.val)

            recur(row + 1,col -1  ,root.left)
            recur(row + 1,col + 1  ,root.right)
        recur(0,0 ,root)

        ans = defaultdict(list)
        for col in hash:
           for row in sorted(hash[col]):
            sortedCol=sorted(hash[col][row])
            ans[col] += sortedCol
        ans = dict(sorted(ans.items()))
        return list(ans.values())
