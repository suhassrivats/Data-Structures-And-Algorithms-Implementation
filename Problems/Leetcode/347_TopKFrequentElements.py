import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity #
            The time complexity of the above algorithm is O(N+N*logK).

        Space complexity #
            The space complexity will be O(N). Even though we are storing only
        ‘K’ numbers in the heap. For the frequency map, however, we need to
        store all the ‘N’ numbers.
        """

        min_heap = []
        num_frequency_map = {}
        results = []

        # find the frequency of each number
        for num in nums:
            num_frequency_map[num] = num_frequency_map.get(num, 0) + 1

        # go through all numbers of the numFrequencyMap and push them in the
        # minHeap, which will have top k frequent numbers. If the heap size is
        # more than k, we remove the smallest(top) number
        for num, freq in num_frequency_map.items():
            # compare frequencies instead of numbers (freq, num)
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # create a list of top k numbers
        for _ in range(k):
            results.append(heapq.heappop(min_heap)[1])

        return results
