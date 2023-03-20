class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def predict(l ,r , t ):

            if l > r:
                return 0
            
            if t:
                return max(nums[l] + predict(l+1 , r , not t) ,nums[r]+ predict(l , r -1 , not t))
            else:
                return min(-nums[l]+ predict(l + 1 , r, not t) , -nums[r]+ predict(l , r - 1, not t))
                
        return predict(0 , len(nums) - 1 , True) >= 0 
        
        
        

           