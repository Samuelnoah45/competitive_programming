import itertools  
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Hash = defaultdict(int)

        subsets = list(map(lambda x: 
        list(itertools.combinations(nums, x)), range(1, len(nums)+1)))  
        result = [item for sublist in subsets for item in sublist]  
      
        for subset in result:
            ors = 0
            for num in subset:
                ors |= num
            Hash[ors] += 1
        
        return max(Hash.values())