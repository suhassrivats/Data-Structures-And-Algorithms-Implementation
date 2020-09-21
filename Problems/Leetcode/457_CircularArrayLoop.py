class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        Time Complexity:
            The above algorithm will have a time complexity of O(N^2) where ‘N’
        is the number of elements in the array. This complexity is due to the
        fact that we are iterating all elements of the array and trying to find
        a cycle for each element.

        Space Complexity:
            The algorithm runs in constant space O(1).
        """

        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            slow = fast = i
            is_forward = nums[i] >= 0  # if we are moving forward or not

            while True:
                # move one step for slow pointer
                slow = self.find_next_index(nums, is_forward, slow)
                # move one step for fast pointer
                fast = self.find_next_index(nums, is_forward, fast)
                if fast != -1:
                    # move another step for fast pointer
                    fast = self.find_next_index(nums, is_forward, fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break

            if slow != -1 and slow == fast:
                return True

        return False

    def find_next_index(self, nums, is_forward, current_index):
        direction = nums[current_index] >= 0

        # change in direction, return -1
        if direction != is_forward:
            return -1

        next_index = (current_index + nums[current_index]) % len(nums)

        if next_index == current_index:
            return -1

        return next_index
