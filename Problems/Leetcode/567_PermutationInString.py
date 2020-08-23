class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = s1
        string = s2

        window_start, matched = 0, 0
        char_frequency = {}

        for chr in pattern:
            char_frequency[chr] = char_frequency.get(chr, 0) + 1

        # our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char in char_frequency:
                # decrement the frequency of matched character
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            # shrink the window by one character
            if window_end >= len(pattern) - 1:
                left_char = string[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return False
