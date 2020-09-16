import heapq


class FreqStack:
    """
    Time complexity:
        The time complexity of push() and pop() is O(logN) where ‘N’ is the
    current number of elements in the heap.

    Space complexity:
        We will need O(N) space for the heap and the map, so the overall space
    complexity of the algorithm is O(N).
    """

    def __init__(self):
        self.num_freq_map = {}
        self.max_heap = []
        self.index = -1

    def push(self, x: int) -> None:
        self.index += 1
        self.num_freq_map[x] = self.num_freq_map.get(x, 0) + 1
        heapq.heappush(self.max_heap, (-self.num_freq_map[x], -self.index, x))

    def pop(self) -> int:
        freq, index, x = heapq.heappop(self.max_heap)
        self.num_freq_map[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
