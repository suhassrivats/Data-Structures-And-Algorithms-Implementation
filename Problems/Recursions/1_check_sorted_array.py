"""
Check if the array is sorted
"""

def check_sorted_array(nums):
	

	def helper(index):
		if index == len(nums) - 1:
			return True
		return nums[index] < nums[index+1] and helper(index+1)

	print(helper(0))



# Inovke function call
nums = [1, 2, 3, 6, 4, 5]
check_sorted_array(nums)