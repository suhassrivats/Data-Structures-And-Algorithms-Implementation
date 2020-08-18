# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         right = 0
#         left = 0
#         max_substring_length = 0
#         seen = set()
#
#         while right < len(s):
#             if s[right] not in seen:
#                 seen.add(s[right])
#                 right += 1
#                 max_substring_length = max(max_substring_length, len(seen))
#             else:
#                 seen.remove(s[left])
#                 left += 1
#
#         return max_substring_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity #
            The time complexity of the above algorithm will be O(N) where ‘N’
            is the number of characters in the input string.

        Space Complexity #
            The space complexity of the algorithm will be O(K) where K is the
            number of distinct characters in the input string. This also means
            K<=NK<=N, because in the worst case, the whole string might not
            have any repeating character so the entire string will be added to
            the HashMap. Having said that, since we can expect a fixed set of
            characters in the input string (e.g., 26 for English letters), we
            can say that the algorithm runs in fixed space O(1); in this 
            case, we can use a fixed-size array instead of the HashMap.
        """
        window_start = 0
        max_length = 0
        char_index_map = {}

        # try to extend the range [windowStart, windowEnd]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            # if the map already contains the 'right_char', shrink the window
            # from the beginning so that we have only one occurrence of 'right_char'
            if right_char in char_index_map:
                # this is tricky; in the current window, we will not have any
                # 'right_char' after its previous index and if 'window_start' is
                # already ahead of the last index of 'right_char', we'll keep
                # 'window_start'
                window_start = max(window_start, char_index_map[right_char] + 1)
            # insert the 'right_char' into the map
            char_index_map[right_char] = window_end
            # remember the maximum length so far
            max_length = max(max_length, window_end - window_start + 1)

        return max_length
