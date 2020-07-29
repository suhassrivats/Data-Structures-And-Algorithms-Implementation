class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        return s


# Using Recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)
