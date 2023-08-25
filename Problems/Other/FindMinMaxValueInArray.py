def minimize_max_value_bruteforce(arr):
    """
    i: 2<=i<=n
    x: 1<=x<=arr[i]
    set arr[i-1] to arr[i-1]+x
    set arr[i] to arr[i]-x

    Example:
    arr = [10, 3, 5, 7], n=4, Assume index starts from 1 for arrays

    i=2, x=3
    arr[2]-=x => 3-3 => 0
    arr[2-1]+=x => 10+3 => 13

    arr = [13, 0, 5, 7]
    =====

    i=3, x=5
    arr[3]-=x => 5-5 => 0
    arr[3-1]+=x => 0+5 => 5
    arr = [13, 5, 0, 7]
    =====

    i=4, x=7
    arr[4]-=x => 7-7 => 0
    arr[4-1]+x =>  0+7 => 7
    arr = [13, 5, 7, 0]
    """

    # By equally distributing the value we can find the minimized maximum value
    max_min_sum = 0  # Represents the maximum value after redistribution
    total_sum = 0    # Keeps track of the running total sum
    for i, value in enumerate(arr):
        total_sum += value
        i += 1
        calculated_value = math.ceil(total_sum/i)
        if max_min_sum < calculated_value:
            max_min_sum = calculated_value

    print(max_min_sum)
    return max_min_sum

#############
def isPossible(arr, k):
    brr = arr[::-1]  # store the reversed array
    for i in range(len(brr)-1):  # Try to make all elements equal to k
        if brr[i] > k:
            diff = brr[i] - k
            brr[i] = k
            brr[i+1] += diff

    # Check if any of the elements is >k after redistribution
    for num in brr:
        if num > k:
            return False  # Indicating that it is not possible to make all elements smaller than k

    return True

def minimize_max_value_optimized(arr):
    low = min(arr)
    high = max(arr)
    ans = 0
    while (low <= high):
        mid = (low + high) // 2
        if isPossible(arr, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
    return ans

# Test cases
arr1 = [1, 5, 7, 6]
print(minimize_max_value_bruteforce(arr1))  # Output: 5

arr2 = [5, 15, 19]
print(minimize_max_value_bruteforce(arr2))  # Output: 13

arr3 = [10, 3, 5, 7]
print(minimize_max_value_bruteforce(arr3))  # Output: 10