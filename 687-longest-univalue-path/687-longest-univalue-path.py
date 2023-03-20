# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0 
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.recur(root)
        return self.ans


    def recur (self ,root):
        if root == None:
            return [0 ,0]
        
        l = self.recur(root.left)
        r = self.recur(root.right)

        if root.val == l[0] and  root.val == r[0]:
            self.ans = max(self.ans ,l[1]+r[1])
    
            return [root.val , max(l[1] ,r[1])+1]
        elif root.val == l[0]:
            self.ans = max(self.ans ,l[1])
            return [root.val , l[1]+1]
        
        elif root.val == r[0]:
            self.ans = max(self.ans ,r[1])
            return [root.val , r[1]+1]
        else:
            return [root.val , 1]




        


      
        
        
        

       