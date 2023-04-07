class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        Hash = defaultdict(int)

        for edge in edges:
            print(edge[1])
            Hash[edge[1]] += 1
            Hash[edge[0]] += 1

        for key in Hash:
            if Hash[key] == len(edges):
                return key
        return 0