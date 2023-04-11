class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        Hash = defaultdict(set)
        ans = 0
        for  road in roads:
            Hash[road[0]].add(road[1])
            Hash[road[1]].add(road[0])

        for key in Hash:
            for key2 in Hash:
               if key!= key2:
                    print(key , key2)
                    if key in Hash[key2] : 

                       ans = max(ans , (len(Hash[key]) + len(Hash[key2]) - 1))
                    else:
                        ans = max(ans , (len(Hash[key]) + len(Hash[key2]) ))
        return ans