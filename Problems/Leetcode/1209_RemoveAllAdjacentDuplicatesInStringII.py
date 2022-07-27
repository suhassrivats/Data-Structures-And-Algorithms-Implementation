class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Time Complexity:
            In the worst case, we will be adding and removing every element to 
        the stack. O(n) + O(n) => O(2n) => O(n)

        Space Complexity:
            We are using stack as extra space. In the worst case, we will store
        all the characters in it. O(n)
        """
        stack = []  # [[char, count]]
        res = ""

        for c in s:
            if stack and stack[-1][0] == c:  # if it is the same char, increment count by 1
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            # remove if the identical consecutive chars are equal to k
            if stack[-1][1] == k:
                stack.pop()

        # Join chars and output in desired format
        for c, count in stack:
            res += (c*count)

        return res
