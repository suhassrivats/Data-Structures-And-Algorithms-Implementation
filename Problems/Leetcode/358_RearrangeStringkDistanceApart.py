import heapq
from collections import deque


class Solution:
    def rearrangeString(self, words, k):
        """
        Time complexity:
            The time complexity of the above algorithm is O(N*logN) where ‘N’
        is the number of characters in the input string.

        Space complexity:
            The space complexity will be O(N), as in the worst case, we need to
        store all the ‘N’ characters in the HashMap.
        """

        if k <= 1:
            return words

        charFrequencyMap = {}
        for char in words:
            charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

        maxHeap = []
        # add all characters to the max heap
        for char, frequency in charFrequencyMap.items():
            heappush(maxHeap, (-frequency, char))

        queue = deque()
        resultString = []
        while maxHeap:
            frequency, char = heappop(maxHeap)
            # append the current character to the result string and decrement its count
            resultString.append(char)
            # decrement the frequency and append to the queue
            queue.append((char, frequency+1))
            if len(queue) == k:
                char, frequency = queue.popleft()
                if -frequency > 0:
                    heappush(maxHeap, (frequency, char))

        # if we were successful in appending all the characters to the result string, return it
        return ''.join(resultString) if len(resultString) == len(words) else ""
