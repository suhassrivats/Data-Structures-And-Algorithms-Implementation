import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Time complexity:
            The time complexity of this algorithm is (N*logK) as we iterating
        all points and pushing them into the heap.

        Space complexity:
            The space complexity will be O(K) because we need to store ‘K’
        point in the heap.
        """

        max_heap = []
        results = []

        for point in points:
            dist = point[0]**2+point[1]**2
            if len(max_heap) < K:
                heapq.heappush(max_heap, (-dist, point))
            else:
                if max_heap[0][0] < -dist:
                    heapq.heapreplace(max_heap, (-dist, point))

        for i in range(K):
            results.append(heapq.heappop(max_heap)[1])

        return results
