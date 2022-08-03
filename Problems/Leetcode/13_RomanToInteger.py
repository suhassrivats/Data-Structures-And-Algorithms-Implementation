class Solution:
    def romanToInt(self, s: str) -> int:
        """
        T: O(n)
        C: O(1)
        """
        # large to small -> add them up
        # small to large -> subtract smaller
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s)):
            if i < len(s)-1 and translations[s[i]] < translations[s[i+1]]:
                result -= translations[s[i]]
            else:
                result += translations[s[i]]
        return result
