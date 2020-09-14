import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Time complexity:
            The time complexity of the above algorithm is O(D*logD) where ‘D’
        is the number of distinct characters in the input string. This means,
        in the worst case, when all characters are unique the time complexity
        of the algorithm will be O(N*logN) where ‘N’ is the total number of
        characters in the string.

        Space complexity:
            The space complexity will be O(N), as in the worst case, we need to
        store all the ‘N’ characters in the HashMap.
        """

        max_heap = []
        char_frequency_map = {}
        sorted_chars_by_frequency = []

        # Put all characters and its frequency in a dictionary
        for c in s:
            char_frequency_map[c] = char_frequency_map.get(c, 0) + 1

        # Add all characters to max_heap based on its frequency
        for char, frequency in char_frequency_map.items():
            heapq.heappush(max_heap, (-frequency, char))

        while max_heap:
            frequency, char = heapq.heappop(max_heap)
            for _ in range(-frequency):
                sorted_chars_by_frequency.append(char)

        return ''.join(sorted_chars_by_frequency)
