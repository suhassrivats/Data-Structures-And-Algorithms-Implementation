def generateSubsets(arr, n):
    all_subsets = []
    powerSet = pow(2,n)

    # For all possible masks or subsets
    for mask in range(powerSet):
        curr_set = []
        # For all possible bitmasks of n bits
        for j in range(n):
            if mask & (1<<j):
                curr_set.append(arr[j])
        all_subsets.append(curr_set)
    print(all_subsets)
    return all_subsets



arr = [1, 2, 3]
print("All the subsets are: ")
generateSubsets(arr, len(arr))
