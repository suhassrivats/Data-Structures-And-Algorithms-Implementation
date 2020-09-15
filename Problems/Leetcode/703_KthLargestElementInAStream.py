import heapq


class KthLargest:
    """
    Algorithm:
    - Create a pq - keep it only having the k-largest elements by popping off
    small elements.
    - With only k elements, the smallest item (self.pool[0]) will always be the
    kth largest.
    - If a new value is bigger than the smallest, it should be added into your
    heap.
    - If it's bigger than the smallest (that are already the kth largest), it
    will certainly be within the kth largest of the stream.

    Time and Space Complexity:
    A data-structure and/or class and its methods can each have very different
    performance characteristics. Heapfication is O(log n) time and O(n)
    space -- during initialization it appears to be O(log N) time and O(log N)
    space, but for add, it's O(log K) + O(1) time and O(k) space as the heap
    size is constrained to K (NOT N where N is the input nums). The O(1) comes
    from having to read from the top of the heap to return the value which is
    constant-time.
    """

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(nums)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
