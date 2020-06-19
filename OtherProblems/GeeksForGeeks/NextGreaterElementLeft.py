# https://www.geeksforgeeks.org/closest-greater-or-same-value-on-left-side-for-every-element-in-array/
# https://www.youtube.com/watch?v=T5s96ynzArg&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=3


def nge_left(arr):
    """
    Time Complexity: O(n)
    Space Complexity (auxiliary): O(n + n) // stack and output

    Bruteforce:
    for i in range(0, len(arr)-1):
        for j in range(i-1, len(arr)-1)

    Note that j is dependent on i. Therefore it can be optimized using stack.
    Couple of modifications from NGE_Right are that:
        1. Iterate for loop from 0 to n
        2. Do not reverse output array

    Rest of the code remains same.
    """
    stack = []
    output = []

    for i in range(len(arr)):
        if not stack:
            output.append(-1)
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

    print(output)
    return output


# Tests
arr = [1, 3, 2, 4]
# arr = [10, 9, 8, 7]
# printNGE(arr)
nge_left(arr)
