import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time complexity #
            The time complexity of this algorithm is O(K*logK+(N-K)*logK),
        which is asymptotically equal to O(N*logK).

        Space complexity #
            The space complexity will be O(K) because we need to store ‘K’
        smallest numbers in the heap.
        """
        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for j in range(k, len(nums)):
            if min_heap[0] < nums[j]:
                heapq.heapreplace(min_heap, nums[j])

        return min_heap[0]
