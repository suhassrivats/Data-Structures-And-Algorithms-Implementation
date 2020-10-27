# class Solution:
#     """
#     Time Complexity: O(N^2) where N is the number of elements in the list
#     Space Complexity: O(N)
#     """

#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = [None] * len(nums)
#         for i, num1 in enumerate(nums):
#             prod = 1
#             for j, num2 in enumerate(nums):
#                 if i != j:
#                     prod *= nums[j]
#             result[i] = prod
#         return result


# # Using divide approach
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         product = 1
#         for num in nums:
#             product *= num

#         # update the value of each item in nums by dividing product with num
#         for i, num in enumerate(nums):
#             if num != 0:
#                 nums[i] = product//num
#             else:
#                 nums[i] = product

#         return nums


# Left and right product lists
class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for storing left, right and answer arrays
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, answer = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        length = len(nums)

        # Left array
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]

        # Right array
        right[length-1] = 1
        for i in reversed(range(length-1)):
            right[i] = nums[i+1] * right[i+1]

        # Output array
        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer


# Optimize left and right product lists to in-place
class Solution:
    """
    Time complexity: O(N) where N represents the number of elements in the
        input array. We use one iteration to construct the array L, one to
        update the array answeranswer.
    Space complexity: O(1) since don't use any additional array for our
        computations. The problem statement mentions that using the answer
        array doesn't add to the space complexity.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i-1]*answer[i-1]

        right = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * right
            right *= nums[i]

        return answer
