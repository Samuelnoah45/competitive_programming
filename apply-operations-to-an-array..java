class Solution:
	def applyOperations(self, nums: List[int]) -> List[int]:


		for index in range(len(nums)-1):

			if nums[index] == nums[index + 1]:

				nums[index] = nums[index] * 2
				nums[index + 1] = 0

		result = []
		count_zero = 0

		for num in nums:
			if num != 0:
				result.append(num)
			else:
				count_zero = count_zero + 1

		result = result + [0] * count_zero

		return result