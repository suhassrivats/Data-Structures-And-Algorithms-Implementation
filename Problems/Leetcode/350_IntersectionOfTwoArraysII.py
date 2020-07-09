class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time Complexity: O(n + m)
        Space Complexity (auxiliary): O(n + m) // when there is no intersection
        """
        counts = {}
        result = []

        # Add all the elements of nums1 to counts dict. Where key is the element
        # itself and value is its frequency
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        for num in nums2:
            if num in counts and counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result
