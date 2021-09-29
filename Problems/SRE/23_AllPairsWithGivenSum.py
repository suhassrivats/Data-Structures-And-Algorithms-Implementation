# https://www.geeksforgeeks.org/print-all-pairs-with-given-sum/


def pairedElements(arr, sum):
    arr.sort()
    results = set()
    low, high = 0, len(arr) - 1

    while low < high:
        current_sum = arr[low] + arr[high]
        if current_sum == sum:
            results.add((arr[low], arr[high]))
        if current_sum > sum:
            high -= 1
        else:
            low += 1

    return results


# Invoke function
arr = [2, 3, 4, -2, 6, 8, 9, 11, 8, -2, 8]
sum = 6
pairedElements(arr, sum)
