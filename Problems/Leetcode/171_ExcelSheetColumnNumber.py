class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        total = 0

        # ACSII of A=65. Make it 1
        for exp, c in enumerate(s):
            total += (ord(c) - 65+1) * (26**exp)
        return total
