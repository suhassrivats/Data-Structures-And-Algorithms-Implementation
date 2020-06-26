def calculateSpan(arr):
    output = []
    stack = []

    for i in range(len(arr)):
        if not stack:
            output.append(-1)
        elif stack and stack[-1][0] > arr[i]:
            output.append(stack[-1][1])
        elif stack and stack[-1][0] < arr[i]:
            while stack and stack[-1][0] < arr[i]:
                stack.pop()
            if not stack:
                output.append(-1)
            else:
                output.append(stack[-1][1])
        stack.append((arr[i], i))

    # Final output
    for i in range(len(output)):
        output[i] = i - output[i]

    print(output)
    return output


# Tests
arr = [100, 80, 60, 70, 60, 75, 85]
# arr = [11, 13, 21, 3]
calculateSpan(arr)
