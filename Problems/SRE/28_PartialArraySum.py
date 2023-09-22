"""
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
"""

def splitArraySum_bruteforce(array):
    # Time: O(N^2), Space: O(N)
    total = sum(array)
    for i in range(len(array)):
        left_array, right_array = array[i:], array[:i]
        left_sum, right_sum = sum(left_array), sum(right_array)

        if left_sum == right_sum:
            print(left_array, right_array)
            return True

    return False

def splitArraySum_optimized(array):
    # Time: O(N), Space: O(1)
    left_sum = sum(array)
    right_sum = 0
    for i in range(len(array)-1, -1, -1):
        num = array[i]
        right_sum += num
        left_sum -= num
        if left_sum == right_sum:
            left_array, right_array = array[:i], array[i:]
            print(left_array, right_array)
            return True
    return False

    # n = len(array)
    # left_sum = sum(array)
    #
    # right_sum = 0
    #
    # for i in range(n - 1, -1, -1):
    #     right_sum += array[i]
    #     left_sum -= array[i]
    #
    #     if right_sum == left_sum:
    #         left_array, right_array = list(reversed(array[:i])), list(reversed(array[i:]))
    #         print(left_array, right_array)
    #         print ('True')
    #         return True
    #
    # return False

# Program execution
array = [5, 2, 3, 4]
# splitArraySum_bruteforce(array)
splitArraySum_optimized(array)