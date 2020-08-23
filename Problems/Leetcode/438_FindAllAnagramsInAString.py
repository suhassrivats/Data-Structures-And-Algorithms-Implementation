class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Time Complexity: The time complexity of the above algorithm will be
            O(N + M) where ‘N’ and ‘M’ are the number of characters in the
            input string and the pattern respectively.

        Space Complexity: The space complexity of the algorithm is O(M) since
            in the worst case, the whole pattern can have distinct characters
            which will go into the HashMap. In the worst case, we also need
            O(N) space for the result list, this will happen when the pattern
            has only one character and the string contains only that character.
        """

        window_start, matched = 0, 0
        char_frequency = {}
        result_indices = []

        for c in p:
            char_frequency[c] = char_frequency.get(c, 0) + 1

        # Our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
                # Decrement the frequency of matched character
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            # Have we found an anagram?
            if matched == len(char_frequency):
                result_indices.append(window_start)

            # shriking the sliding window
            if window_end >= len(p)-1:
                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1  # Before putting the character back, decrement the matched count
                    char_frequency[left_char] += 1  # Put the character back

        return result_indices
