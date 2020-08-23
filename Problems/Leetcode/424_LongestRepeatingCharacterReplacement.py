class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

        # Try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            frequency_map[right_char] = frequency_map.get(right_char, 0) + 1
            max_repeat_letter_count = max(max_repeat_letter_count,
                                          frequency_map[right_char])

            # Current window size is from window_start to window_end, overall we have a letter which is
            # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
            # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # if the remaining letters are more than 'k', it is the time to shrink the window as we
            # are not allowed to replace more than 'k' letters
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = s[window_start]
                frequency_map[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
