class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        seen = set()
        p = set()
        for a, b in edges:

            seen.add(b)
            p.add(a)
        
        res = [e for e in p if e not in seen]
        return res