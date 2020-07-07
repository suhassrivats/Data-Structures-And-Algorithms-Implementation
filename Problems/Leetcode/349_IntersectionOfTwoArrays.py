class Solution:
    """
    Time complexity : O(n+m), where n and m are arrays' lengths. O(n) time is
    used to convert nums1 into set, O(m) time is used to convert nums2, and
    contains/in operations are O(1) in the average case.

    Space complexity (auxiliary): O(m+n) in the worst case when all elements in
    the arrays are different.
    """

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
