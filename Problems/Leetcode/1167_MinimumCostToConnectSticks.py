import heapq


class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """

    def MinimumCost(self, sticks):
        """
        Time complexity:
            Given ‘N’ ropes, we need O(N*logN) to insert all the ropes in the
        heap. In each step, while processing the heap, we take out two elements
        from the heap and insert one. This means we will have a total of ‘N’
        steps, having a total time complexity of O(N*logN).

        Space complexity:
            The space complexity will be O(N) because we need to store all the
        ropes in the heap.
        """

        min_heap = []

        for stick_len in sticks:
            heapq.heappush(min_heap, stick_len)

        result, temp = 0, 0
        while len(min_heap) > 1:
            temp = heapq.heappop(min_heap) + heapq.heappop(min_heap)
            result += temp
            heapq.heappush(min_heap, temp)

        return result
