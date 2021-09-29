'''
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
'''

def unique_subsets(nums):
    print([])
    print(nums)

    for i in range(0, len(nums)):
        print(nums[i])
        if i == len(nums)-1:
            break
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                continue
            else:
                print(nums[i], nums[j])
