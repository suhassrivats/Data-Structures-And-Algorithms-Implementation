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
                # If there are consevutive numbers
                if char == l:
                    count += 1
                else:
                    temp += str(count) + char
                    # Go to the next differnt number. Ex: 111221, go to 2
                    char = l
                    count = 1

            temp += str(count) + char
            results = temp

        return results
