def generateSubsequences(arr, index, subarray):
    # Print the subsequences when we reach the end of the recursion tree.
    if index == len(arr):
        if len(subarray) != 0:
            for i in subarray:
                print(i, end=" ")
            print()
        else:
            print("[]")

    else:
        # not adding the current element into the subsequence.
        generateSubsequences(arr, index + 1, subarray)

        # adding the current index into the subsequence and calling the recursive function.
        generateSubsequences(arr, index + 1,
                             subarray+[arr[index]])

    return


arr = [1, 2, 3]
print("All the subsequences are: ")
generateSubsequences(arr, 0, [])
