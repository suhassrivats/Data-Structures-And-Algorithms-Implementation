import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        Time complexity:
            Since, at most, we’ll be going through all the elements of all the
        arrays and will remove/add one element in the heap in each step, the
        time complexity of the above algorithm will be O(N*logM) where ‘N’ is
        the total number of elements in all the ‘M’ input arrays.

        Space complexity:
            The space complexity will be O(M) because, at any time, our min-heap
        will be store one number from all the ‘M’ input arrays.
        """

        min_heap = []
        current_max = float('-inf')
        range_start, range_end = 0, float('inf')

        # put the 1st element of each array in the max heap
        for arr in nums:
            heapq.heappush(min_heap, (arr[0], 0, arr))
            current_max = max(current_max, arr[0])

        # take the smallest(top) element form the min heap, if it gives us
        # smaller range, update the ranges if the array of the top element has
        # more elements, insert the next element in the heap
        while len(min_heap) == len(nums):
            num, i, arr = heapq.heappop(min_heap)
            range_diff = range_end - range_start
            if range_diff > current_max - num:
                range_start, range_end = num, current_max

            if len(arr) > i+1:
                # insert the next element in the heap
                heapq.heappush(min_heap, (arr[i+1], i+1, arr))
                current_max = max(current_max, arr[i+1])

        return [range_start, range_end]

import heapq


class Element:
    def __init__(self, value, index, row, array_size):
        self.value = value
        self.index = index
        self.row = row
        self.array_size = array_size

    def __lt__(self, other):
        return self.value < other.value

class Solution:
    """
    [4,10,15,24,26]
    [0, 9,12,20]
    [5,18,22,30]
    """


    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        mn, mx = float('inf'), float('-inf')
        range_val = float('inf')
        low, high = 0, 0
        q = []

        # Initially push the first element of each row into a min-heap.
        for i in range(len(nums)):
            element = Element( nums[i][0], 0, i, len(nums[i]))
            heapq.heappush(q, (element.value, element))

            # Find min and max values of these items in the list.
            mn = min(mn, nums[i][0])
            mx = max(mx, nums[i][0])

        # To find if its the smallest range, we need to check all possibilities
        while q:
            # Pop the minimum element and check the range_value
            maybe_min, temp_element = heapq.heappop(q)

            if range_val > mx - maybe_min:
                mn = maybe_min
                range_val = mx - mn
                low, high = mn, mx

            if temp_element.index == temp_element.array_size - 1:
                break

            # Move to next minimum item (lists are sorted) in the same row as the popped item and push next item to heap
            temp_element.index += 1
            next_element = Element(
                nums[temp_element.row][temp_element.index],
                temp_element.index,
                temp_element.row,
                temp_element.array_size
            )
            heapq.heappush(q, (next_element.value, next_element))

            # Check if the newly added items is the new max
            mx = max(mx, nums[temp_element.row][temp_element.index])


        return [low, high]

