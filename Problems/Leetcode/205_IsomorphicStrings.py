class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m != n:
            return False

        dict = {}
        for i in range(n):
            # If there is a wrong mapping, then return False
            if s[i] in dict:
                # s = "foo", t = "bar" should return False as 'o' is already
                # mapped to 'a'. It cannot be mapped again with r
                if dict[s[i]] != t[i]:
                    return False
            # If the same mapping is used for other char, return False as well.
            # s="ab", t="aa" should return False as b can't be mapped to a.
            elif t[i] in dict.values():
                return False
            # Map every letter of s to t
            else:
                dict[s[i]] = t[i]

        return True
