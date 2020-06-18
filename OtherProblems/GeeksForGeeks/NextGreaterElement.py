# https://www.geeksforgeeks.org/next-greater-element/
# https://www.youtube.com/watch?v=NXOOYYwpbg4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=2


def printNGE(arr):
    """
    Time Complexity: O(n^2)
    Space Complexity (auxiliary): O(n)
    """
    output = []
    for i in range(len(arr)):
        next = -1
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        output.append(next)
    return output


def printNGE_using_stack(arr):
    """
    Why use stack?
    In the algorithm above we realized that two loops are dependent on each
    other. Note that j will start from i+1. When we see such bruteforce options
    it can be optimized by using stack. Trick is to iterate from the end.

    Time Complexity: O(n)
    Space Complexity (auxiliary): O(n + n) // for stack and output
    """
    stack = []
    output = []

    for i in range(len(arr)-1, -1, -1):
        if not stack:
            output.append(-1)
            stack.append(arr[i])
        elif stack and stack[-1] > arr[i]:
            output.append(stack[-1])
        elif stack and stack[-1] < arr[i]:
            while stack and stack[-1] < arr[i]:
                stack.pop()
            if not stack:
                output.append(-1)
            else:
                output.append(stack[-1])

        stack.append(arr[i])

    print(output[::-1])
    return output[::-1]


# Tests
arr = [1, 3, 2, 4]
# printNGE(arr)
printNGE_using_stack(arr)
