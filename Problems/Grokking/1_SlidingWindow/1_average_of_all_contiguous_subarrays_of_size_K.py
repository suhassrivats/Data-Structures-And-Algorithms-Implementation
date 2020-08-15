# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5


# Brute-force
def find_averages_of_subarrays(K, arr):
    """
    Time complexity: Since for every element of the input array, we are
    calculating the sum of its next ‘K’ elements, the time complexity of the
    above algorithm will be O(N*K) where ‘N’ is the number of elements in the
    input array.
    """
    result = []
    for i in range(len(arr)-K+1):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        result.append(_sum/K)  # calculate average

    return result


# Sliding-window
def find_averages_of_subarrays(K, arr):
    """
    Time complexity: O(N)
    """
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]  # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K)  # calculate the average
            windowSum -= arr[windowStart]  # subtract the element going out
            windowStart += 1  # slide the window ahead

    return result


def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
