class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        # Put all items and its respective frequency into a dictionary
        for ch in s:
            dict[ch] = dict.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if dict[ch] == 1:
                return i
        return -1
