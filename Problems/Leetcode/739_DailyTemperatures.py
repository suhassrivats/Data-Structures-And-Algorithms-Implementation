class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Time Complexity: O(N), where N is the length of T and W is the number
            of allowed values for T[i]. Each index gets pushed and popped at
            most once from the stack.

        Space Complexity: O(W). The size of the stack is bounded as it
            represents strictly increasing temperatures.
        """
        # initialize the result array with all '0's considering when there is
        # no bigger temperature
        results = [0] * len(T)
        stack = []

        for T_index, T_value in enumerate(T):
            # check whether current val is greater than the last appended stack
            # value. We will pop all the elements which is lesser than the
            # current temperature
            while stack and stack[-1][1] < T_value:
                stack_index, stack_value = stack.pop()
                # we are checking how many indices we have crossed since we
                # last have a lesser temperature
                results[stack_index] = T_index - stack_index

            # Remember since we are comparing all the stack elements before
            # inserting, all the stack elements will have temperatures greater
            # than the current value
            stack.append((T_index, T_value))

        return results
