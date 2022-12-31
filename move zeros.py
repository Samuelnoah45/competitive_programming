class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index ,value in enumerate(arr):
            if(value==0):
                left=index
                right=index
                while(right<len(arr)):
                    temp=arr[right]
                    arr[right]=arr[left]
                    arr[left]=temp
                    left+=1
                    right+=1
                    print(arr)
                    