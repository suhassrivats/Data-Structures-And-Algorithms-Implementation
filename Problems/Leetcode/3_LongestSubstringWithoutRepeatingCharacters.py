class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        max_substring_length = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                max_substring_length = max(max_substring_length, len(seen))
            else:
                seen.remove(s[left])
                left += 1

        return max_substring_length
