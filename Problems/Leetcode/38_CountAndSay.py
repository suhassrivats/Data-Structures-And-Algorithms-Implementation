# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221


class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ""
        results = '1'

        for _ in range(n-1):
            char = results[0]
            temp = ''
            count = 0

            for l in results:
                # If there are consecutive numbers
                if char == l:
                    count += 1
                else:
                    temp += str(count) + char
                    # Go to the next different number. Ex: 111221, go to 2
                    char = l
                    count = 1

            temp += str(count) + char
            results = temp

        return results

class Solution:
    def countAndSay(self, n: int) -> str:

        def helper(s):
            result = ''
            count = 1
            for i in range(len(s)):
                if i == len(s)-1 or s[i] != s[i+1]:
                    result += str(count) + s[i]
                    count = 1
                else:
                    count += 1
            return result

        ans = '1'
        for _ in range(2, n+1):
            ans = helper(ans)
        return ans
