class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        monotonic_stack = []
        dict_of_greater_number = {}
        for cur_number in nums2:
    
            while monotonic_stack and cur_number > monotonic_stack[-1]:
                pop_out_number = monotonic_stack.pop()
                dict_of_greater_number[pop_out_number] = cur_number
            
            monotonic_stack.append(cur_number)
        next_greater_element = []
    
        for x in nums1:
            
            if x in dict_of_greater_number:
                next_greater_element.append( dict_of_greater_number[x] )
                
            else:
                next_greater_element.append(-1)
                
        return next_greater_element