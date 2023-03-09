# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def trackNode(root):
            if not root:
                return [0 , 0]
            
            l =  trackNode(root.left) 
            r =  trackNode(root.right) 
            # print(root.val)
            avg = ((l[0] + r[0] + root.val) //(l[1] + r[1] + 1) )
            if avg == root.val:
                self.ans += 1 

            val = root.val +l[0] + r[0]
            num = r[1] + l[1] +1
            return [val , num]

        trackNode(root)
        return self.ans