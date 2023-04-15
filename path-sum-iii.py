# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        counterSum = defaultdict(int)
        counterSum[0] = 1
        count = 0

        def calcSum(root , counterSum , prefixSum):
            nonlocal count
            if root:
                prefixSum += root.val

                if (prefixSum - targetSum) in counterSum:
                    count += counterSum[prefixSum - targetSum]

                counterSum[prefixSum] += 1

                calcSum(root.left , counterSum , prefixSum)
                calcSum(root.right , counterSum , prefixSum)

                counterSum[prefixSum] -= 1

        calcSum(root , counterSum , 0)
        return  count