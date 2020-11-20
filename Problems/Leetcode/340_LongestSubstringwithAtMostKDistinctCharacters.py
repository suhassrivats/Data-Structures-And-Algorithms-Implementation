class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Time Complexity:
            The time complexity of the above algorithm will be O(N) where ‘N’ is
        the number of characters in the input string. The outer for loop runs for
        all characters and the inner while loop processes each character only once,
        therefore the time complexity of the algorithm will be O(N+N) which is
        asymptotically equivalent to O(N).

        Space Complexity:
            The space complexity of the algorithm is O(K), as we will be storing a
        maximum of ‘K+1’ characters in the HashMap.
        """

        window_start = 0
        max_length = 0
        char_frequency = {}

        # in the following loop we'll try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1

            # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1  # shrink the window
            # remember the maximum length so far
            max_length = max(max_length, window_end-window_start + 1)

        return max_length
