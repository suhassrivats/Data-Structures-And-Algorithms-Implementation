import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time complexity:
            Since we’ll be going through at most ‘K’ elements among all the
        arrays, and we will remove/add one element in the heap in each step,
        the time complexity of the above algorithm will be O(K*logM) where ‘M’
        is the total number of input arrays.

        Space complexity:
            The space complexity will be O(M) because, at any time, our min-heap
        will be storing one number from all the ‘M’ input arrays.
        """

        min_heap = []

        # put the 1st element of each list in the min heap
        for i in range(len(matrix)):
            # We want to push the next number in the heap. We need to know what the
            # index of the current number in the current array was.
            heapq.heappush(min_heap, (matrix[i][0], 0, matrix[i]))

        # take the smallest(top) element form the min heap, if the running count is equal to k return the number
        number_count, number = 0, 0
        while min_heap:
            number, i, array = heapq.heappop(min_heap)
            number_count += 1
            if number_count == k:
                break
            # if the array of the top element has more elements, add the next element to the heap
            if len(array) > i+1:
                heapq.heappush(min_heap, (array[i+1], i+1, array))

        return number
