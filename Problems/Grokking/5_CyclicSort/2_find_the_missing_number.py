class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time complexity:
            The time complexity of the above algorithm is O(n). In the while
        loop, although we are not incrementing the index i when swapping the
        numbers, this will result in more than ‘n’ iterations of the loop, but
        in the worst-case scenario, the while loop will swap a total of ‘n-1’
        numbers and once a number is at its correct index, we will move on to
        the next number by incrementing i. In the end, we iterate the input
        array again to find the first number missing from its index, so overall,
        our algorithm will take O(n) + O(n-1) + O(n) which is asymptotically
        equivalent to O(n).

        Space complexity:
            The algorithm runs in constant space O(1).
        """
        i, n = 0, len(nums)

        while i < n:
            j = nums[i]
            # number must be equal to its index value. If not swap.
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # find the first number missing from our index
        for i in range(n):
            if nums[i] != i:
                return i

        return n
