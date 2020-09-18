import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Intuition:
            I found it helpful to visualize the input as an m×n matrix of sums,
        for example for nums1=[1,7,11], and nums2=[2,4,6]:

              2   4   6
           +------------
         1 |  3   5   7
         7 |  9  11  13
        11 | 13  15  17

        Of course the smallest pair overall is in the top left corner, the one
        with sum 3. We don't even need to look anywhere else. After including
        that pair in the output, the next-smaller pair must be the next on the
        right (sum=5) or the next below (sum=9). We can keep a "horizon" of
        possible candidates, implemented as a heap / priority-queue, and roughly
        speaking we'll grow from the top left corner towards the right/bottom.

        Time Complexity:
            The complexity of this algorithm is O(k*logk) if k<n, because we
        repeat k times, and each time we do a O(logk) heappush.

        Space Complexity:
            The space complexity will be O(k) because, at any time, our MinHeap
        will be storing ‘K’ smallest pairs.
        """

        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        output = []

        # Add the smallest element to the heap and mark its position as visited
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        visited.append((0, 0))

        while len(output) < k and heap:

            # Pop the smallest (top) element
            total, i, j = heapq.heappop(heap)
            output.append((nums1[i], nums2[j]))

            # Next smallest element must be in right or at the bottom of the smallest total
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                visited.append((i+1, j))

            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
                visited.append((i, j+1))

        return output
