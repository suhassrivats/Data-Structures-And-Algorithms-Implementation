'''
Giving an array with only "g" (means good) and "b" (means bad), "g"s are always
before "b"s, and will always have both "g" and "b". Find the index of first "b"
Or explain it another way: you are giving a revision history, find the first bad
revision. "g" stands for good revision and "b" stands for bad revision.

Example:
arr = ["g", "g", "g", "b", "b"]
return 3 (zero based index)
'''

def find_first_bad_version(arr):
    """
    TC: O(n)
    SC:
        - Input: O(n)
        - Auxiliary: O(1)
        - Total: O(n + 1) => O(n)
    """
    bad = None
    for i, char in enumerate(arr):
        if char == "b":
            bad = i
            break
    return bad


def find_first_bad_version_optimized(arr):
    """
    TC: O(log n); using binary search
    SC:
        - Input: O(n)
        - Auxiliary: O(1)
        - Total: O(n + 1) => O(n)
    """
    index = None
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]
        if mid_element == "b":
            index = mid  # Store the index temporarily
            right = mid - 1
            left += 1
        else:
            left += 1
    return index
