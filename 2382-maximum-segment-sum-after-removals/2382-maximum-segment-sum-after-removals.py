class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = [i for i in range(n+1)]
        Hash = defaultdict(list)
        rank = {i:nums[i]  for i in range(n)}
        maxVal = 0
        def find(x):
            if x == parent[x]:
                return x
            r = find(parent[x])
            parent[x] = r
            return r
            
        
        def union(x, y ):
            rep_x = find(x)
            rep_y = find(y)
            if rep_x != rep_y:
                if rank[rep_x] > rank[rep_y]:
                    parent[rep_y] = rep_x
                    rank[rep_x] += rank[rep_y]
                    return rank[rep_x]
                else:
                    parent[rep_x] = rep_y
                    rank[rep_y] += rank[rep_x]
                    return rank[rep_y] 
            else:
                return rank[rep_y]


        build = [0]*(n+1)
        ans = [0]
        for i in range(n-1 , -1 ,-1):
            rmIdx = removeQueries[i]
            val = 0
            if build[rmIdx + 1] != 0 and build[rmIdx - 1] != 0:
                build[rmIdx] = nums[rmIdx]
                union(rmIdx ,rmIdx+1)
                val = union(rmIdx ,rmIdx-1)
            elif  build[rmIdx + 1] != 0:
                build[rmIdx] = nums[rmIdx]
                val = union(rmIdx ,rmIdx+1)
            elif build[rmIdx - 1] != 0:
                build[rmIdx] = nums[rmIdx]
                val =union(rmIdx ,rmIdx-1)
            else:
                build[rmIdx] = nums[rmIdx]
                val = union(rmIdx ,rmIdx)
            maxVal = max(maxVal ,val)
            ans.append(maxVal)
        return  reversed(ans[:n])
                



        

        