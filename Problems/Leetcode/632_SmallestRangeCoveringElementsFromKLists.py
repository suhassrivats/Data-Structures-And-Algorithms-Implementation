import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Time complexity:
            Since, at most, we’ll be going through all the elements of all the
        arrays and will remove/add one element in the heap in each step, the
        time complexity of the above algorithm will be O(N*logM) where ‘N’ is
        the total number of elements in all the ‘M’ input arrays.

        Space complexity:
            The space complexity will be O(M) because, at any time, our min-heap
        will be store one number from all the ‘M’ input arrays.
        """

        min_heap = []
        current_max = float('-inf')
        range_start, range_end = 0, float('inf')

        # put the 1st element of each array in the max heap
        for arr in nums:
            heapq.heappush(min_heap, (arr[0], 0, arr))
            current_max = max(current_max, arr[0])

        # take the smallest(top) element form the min heap, if it gives us
        # smaller range, update the ranges if the array of the top element has
        # more elements, insert the next element in the heap
        while len(min_heap) == len(nums):
            num, i, arr = heapq.heappop(min_heap)
            range_diff = range_end - range_start
            if range_diff > current_max - num:
                range_start, range_end = num, current_max

            if len(arr) > i+1:
                # insert the next element in the heap
                heapq.heappush(min_heap, (arr[i+1], i+1, arr))
                current_max = max(current_max, arr[i+1])

        return [range_start, range_end]
