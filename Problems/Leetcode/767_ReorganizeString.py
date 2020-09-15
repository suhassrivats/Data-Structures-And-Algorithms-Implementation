import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        Time complexity:
            Since we need to put all the numbers in a min-heap, the time
        complexity of the above algorithm will be O(N*logN) where ‘N’ is the
        total input numbers.

        Space complexity:
            The space complexity will be O(N), as we need to store all the ‘N’
        numbers in the heap.
        """

        max_heap = []
        char_frequency_map = {}
        results = []

        for char in S:
            char_frequency_map[char] = char_frequency_map.get(char, 0) + 1

        # add all characters to the max heap
        for char, frequency in char_frequency_map.items():
            heappush(max_heap, (-frequency, char))

        previous_char, previous_freq = None, 0
        while max_heap:
            frequency, char = heapq.heappop(max_heap)
            # add the previous entry back in the heap if its frequency is greater than zero
            if previous_char and -previous_freq > 0:
                heapq.heappush(max_heap, (previous_freq, previous_char))
            # append the current character to the result string and decrement its count
            results.append(char)
            previous_char = char
            previous_freq = frequency+1  # decrement the frequency

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(results) if len(results) == len(S) else ""
