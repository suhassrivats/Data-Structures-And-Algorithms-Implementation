class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = l + (r - l) // 2
            # Compare with next element to find slope
            if arr[mid] < arr[mid + 1]:
                # ascending slope, peak is to the right
                l = mid + 1
            else:
                # descending slope, peak is at mid or to the left
                r = mid
        return l
