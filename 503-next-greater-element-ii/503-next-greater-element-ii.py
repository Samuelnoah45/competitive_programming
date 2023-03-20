from collections import defaultdict, deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        next_greater_dict = defaultdict( deque )

        monotonic_stack = []
        
        def helper( arr: List):
            
            for cur_number in arr:
                
                while monotonic_stack and cur_number > monotonic_stack[-1]:

                    pop_out_number = monotonic_stack.pop()
                    next_greater_dict[ pop_out_number ].append( cur_number )
                
                monotonic_stack.append( cur_number )
                
  
        helper( nums  )
        
        helper( nums[ :-1] )
        
        
        next_greater_number = []
        
        for x in nums:
            
            if x in next_greater_dict:
                
                next_greater_number.append( next_greater_dict[x].popleft() ) 
            
            else:
                
                next_greater_number.append( -1 )
                
        return next_greater_number