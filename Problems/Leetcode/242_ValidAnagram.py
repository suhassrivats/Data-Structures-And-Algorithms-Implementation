class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_frequency_map = {}

        for c in s:
            char_frequency_map[c] = char_frequency_map.get(c, 0) + 1

        for c in t:
            if c not in char_frequency_map:
                return False
            char_frequency_map[c] -= 1

        for val in char_frequency_map.values():
            if val != 0:
                return False

        return True
