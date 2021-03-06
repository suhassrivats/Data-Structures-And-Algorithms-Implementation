# https://www.youtube.com/watch?v=85LWui3FlVk&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=4

def next_smaller_element_left(arr):
    """
    Time Complexity: O(n)
    Space Complexity (auxiliary): O(n + n) // stack and output
    """
    output = []
    stack = []

    for i in range(len(arr)):
        if not stack:
            output.append(-1)
        elif stack and stack[-1] < arr[i]:
            output.append(stack[-1])
        elif stack and stack[-1] >= arr[i]:
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if not stack:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])

    print(output)
    return output


# Tests
# arr = [4, 5, 2, 10, 8]
arr = [1, 3, 2, 5, 4]
next_smaller_element_left(arr)
