from heapq import *


class Solution:
    def findClosestElements(self, arr: List[int], K: int, X: int) -> List[int]:
        """
        Time complexity:
            The time complexity of the above algorithm is O(logN + K*logK). We
        need O(logN) for Binary Search and O(K*logK) to insert the numbers in
        the Min Heap, as well as to sort the output array.

        Space complexity:
            The space complexity will be O(K), as we need to put a maximum of
        2K numbers in the heap.
        """

        index = self.binary_search(arr, X)
        low, high = index - K, index + K

        low = max(low, 0)  # 'low' should not be less than zero
        # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)

        minHeap = []
        # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i] - X), arr[i]))

        # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(K):
            result.append(heappop(minHeap)[1])

        result.sort()
        return result

    def binary_search(self, arr,  target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if low > 0:
            return low - 1
        return low
