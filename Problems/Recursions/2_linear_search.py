def linear_search(nums, target):
    
    def helper(i):
        if i == len(nums):
            return False
        return nums[i] == target or helper(i+1)
      
    def helper_index(i):
        if i == len(nums):
            return -1
        if nums[i] == target:
            return i
        else:
            return helper_index(i+1)
    
    # print(helper(0))        
    print(helper_index(0))


# Invoke function
nums = [9, 8, 1, 6, 0]
target = 8
linear_search(nums, target)