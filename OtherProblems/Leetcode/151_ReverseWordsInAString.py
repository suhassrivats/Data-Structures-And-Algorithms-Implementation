class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = s.strip().split()
        return ' '. join(new_s[::-1])
