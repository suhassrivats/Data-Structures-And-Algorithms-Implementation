class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Idea:
            - Have two pointers.
            - Move right pointer until odd_count == 3
                - Move left pointer to right, reduce odd count along the way
                - See how many sub arrays can be formed
        
        T: O(N)
        S: O(1)
        """
        left, right = 0, 0
        cur_sub_count = 0
        odd_count = 0
        result = 0

        for right in range(len(nums)):

            if nums[right] % 2 == 1:
                odd_count += 1
                cur_sub_count = 0

            while odd_count == k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                cur_sub_count += 1
                left += 1

            result += cur_sub_count

        return result
