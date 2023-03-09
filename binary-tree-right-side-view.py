# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hash=  defaultdict(list)
        def levelSearch(k,root):

            if not root:
                return 
            hash[k] = root.val
            l =levelSearch(k+1, root.left) 
            r = levelSearch(k+1, root.right) 
        
        levelSearch( 0,root)
    
        return list(hash.values())