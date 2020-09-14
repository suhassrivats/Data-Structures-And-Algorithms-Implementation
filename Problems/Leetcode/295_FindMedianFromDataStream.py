import heapq


class MedianFinder:
    """
    Time complexity:
        The time complexity of the insertNum() will be O(logN) due to the
    insertion in the heap. The time complexity of the findMedian() will be O(1)
    as we can find the median from the top elements of the heaps.

    Space complexity:
        The space complexity will be O(N) because, as at any time, we will be
    storing all the numbers.
    """

    def __init__(self):
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # We balance both heaps. Either both the heaps will have equal number
        # of elements or max-heap will have one more element than the min-heap
        if len(self.max_heap) > len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        median = 0.0
        if len(self.max_heap) == len(self.min_heap):
            # we have even number of elements, take the average of middle two elements
            median = (-self.max_heap[0] + self.min_heap[0]) / 2.0
            return median

        return -self.max_heap[0]/1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
