import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        pos1 = bisect.bisect_right(nums , target) -1
        if nums and pos1 <= 0 and nums[0] != target:
            return [-1 ,-1]
        pos2 = bisect.bisect_left(nums , target) 

        if pos2 >= len(nums) or nums[pos1] !=target:
            return [-1 ,-1]   
        
        return [pos2 ,pos1]