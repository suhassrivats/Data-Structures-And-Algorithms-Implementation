import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ocurrences, n = collections.defaultdict(int), len(s)
        for i in range(n):
            for j in range(i+minSize-1, min(i+maxSize, n)):
                sub = s[i:j+1]
                if len(set(sub)) <= maxLetters:
                    ocurrences[sub] += 1
        return max(ocurrences.values(), default=0)
