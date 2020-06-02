class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Using extra space.
        Time complexity: O(n)
        Space complexity (auxiliary): O(n)
        """
        temp = k
        l = len(nums)
        rot_nums = [None] * len(nums)

        # Reverse last n elements and append
        for i, n in enumerate(nums[-k:]):
            rot_nums[i] = n
            k -= 1

        for i, n in enumerate(nums[:temp+1]):
            rot_nums[temp] = n
            temp += 1

        return rot_nums


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Time complexity: O(n)
        Space complexity (auxiliary): O(1)

        In this approach, we firstly reverse all the elements of the array.
        Then, reversing the first k elements followed by reversing the rest
        n-kn−k elements gives us the required result.

        Let n = 7n=7 and k = 3k=3.

        Original List                   : 1 2 3 4 5 6 7
        After reversing all numbers     : 7 6 5 4 3 2 1
        After reversing first k numbers : 5 6 7 4 3 2 1
        After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
        """

        def num_reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k, n = k % len(nums), len(nums)
        if k:
            # Reverse all elements of the array
            num_reverse(0, n-1)

            # Reverse first k elements
            num_reverse(0, k-1)

            # Reverse rest of the elements
            num_reverse(k, n-1)
