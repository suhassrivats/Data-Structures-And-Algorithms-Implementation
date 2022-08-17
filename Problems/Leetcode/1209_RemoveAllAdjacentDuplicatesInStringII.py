class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Idea:
            - Create a stack with [c, count]
            - If the last element in stack, is the same as the current char, then increment its count
            - If not, append the new element with its count
            - Check if the count of last element in the stack is same as k. If so, it can be removed from stack

        Example: 
        s= "abbcd", k=2
        stack=[[a,1], [b,2]-pop, [c,1], [d,1]]
        output = "acd"

        Time Complexity:
            In the worst case, we will be adding and removing every element to 
        the stack. O(n) + O(n) => O(2n) => O(n)

        Space Complexity:
            We are using stack as extra space. In the worst case, we will store
        all the characters in it. O(n)
        """

        stack = []  # [[char, count]]
        res = ''

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            # Remove identical consecutive chars if they are equal to k
            if stack[-1][1] == k:
                stack.pop()

        # Join characters and output in desired format
        for c, count in stack:
            res += (c*count)

        return res
