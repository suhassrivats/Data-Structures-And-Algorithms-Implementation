"""
Problem Statement:
Given an array of sorted numbers and a target sum, find a pair in the array
whose sum is equal to the given target.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Time Complexity:
The time complexity of the above algorithm will be O(N), where ‘N’ is the
total number of elements in the given array.

Space Complexity:
The algorithm runs in constant space O(1).

Solution:
Since the given array is sorted, a brute-force solution could be to iterate
through the array, taking one number at a time and searching for the second
number through Binary Search. The time complexity of this algorithm will be
O(N*logN). Can we do better than this?

We can follow the Two Pointers approach. We will start with one pointer
pointing to the beginning of the array and another pointing at the end. At
every step, we will see if the numbers pointed by the two pointers add up to
the target sum. If they do, we have found our pair; otherwise, we will do one
of two things:
1) If the sum of the two numbers pointed by the two pointers is greater than the
target sum, this means that we need a pair with a smaller sum. So, to try more
pairs, we can decrement the end-pointer.
2) If the sum of the two numbers pointed by the two pointers is smaller than
the target sum, this means that we need a pair with a larger sum. So, to try
more pairs, we can increment the start-pointer.
"""


def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1  # we need a pair with a bigger sum
        else:
            left += 1  # we need a pair with a smaller sum
    return [-1, -1]
