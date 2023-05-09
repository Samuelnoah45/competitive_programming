# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        arr = []
        def appendNode(w, subRoot ,arr):
            if not subRoot or w < 0:
                return None
            l = appendNode(w-1,subRoot.left ,arr)
            r = appendNode(w-1,subRoot.right ,arr)
            if w == 0:
                arr.append(subRoot.val)
            print(w ,subRoot.val)
        
        def recur(root ,arr):
            if not root:
                return None
            if root.val == target.val:
                if k > 0:
                    appendNode(k - 1 ,root.left ,arr)
                    appendNode(k -1 ,root.right ,arr)
                if k == 0:
                     arr.append(root.val)
                return k - 1
            l = recur(root.left ,arr)
            r = recur(root.right ,arr)
            if l != None:
                if l > 0:
                    appendNode(l-1 ,root.right ,arr)
                if l == 0:
                    arr.append(root.val)
                return l - 1
            if r != None:
                if r > 0:
                    appendNode(r-1 ,root.left ,arr)
                if r == 0:
                     arr.append(root.val)
                return r - 1 
        recur(root ,arr)
        return arr