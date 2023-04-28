# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que = deque([root])
        ans  = []
        while que:
            level = []
            for _ in  range(len(que)):
                node  = que.popleft()
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            if level:
                ans.append(sum(level)/len(level))
        return ans