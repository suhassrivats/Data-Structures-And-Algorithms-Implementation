# CodingBat: Recursion 2

"""
Source: https://codingbat.com/java/Recursion-2

1) groupSum:
Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target? This is a classic backtracking
recursion problem. Once you understand the recursive backtracking strategy in
this problem, you can use the same pattern for many problems to search a space
of choices. Rather than looking at the whole array, our convention is to
consider the part of the array starting at index start and continuing to the
end of the array. The caller can specify the whole array simply by passing
start as 0. No loops are needed -- the recursive calls progress down the array.


groupSum(0, [2, 4, 8], 10) → true
groupSum(0, [2, 4, 8], 14) → true
groupSum(0, [2, 4, 8], 9) → false

##############################################################################

2) groupSum6:
Given an array of ints, is it possible to choose a group of some of the ints,
beginning at the start index, such that the group sums to the given target?
However, with the additional constraint that all 6's must be chosen.
(No loops needed.)


groupSum6(0, [5, 6, 2], 8) → true
groupSum6(0, [5, 6, 2], 9) → false
groupSum6(0, [5, 6, 2], 7) → false

##############################################################################

3) groupNoAdj:
Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target with this additional constraint:
If a value in the array is chosen to be in the group, the value immediately
following it in the array must not be chosen. (No loops needed.)


groupNoAdj(0, [2, 5, 10, 4], 12) → true
groupNoAdj(0, [2, 5, 10, 4], 14) → false
groupNoAdj(0, [2, 5, 10, 4], 7) → false

##############################################################################

4) groupSum5:
Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target with these additional
constraints: all multiples of 5 in the array must be included in the group.
If the value immediately following a multiple of 5 is 1, it must not be
chosen. (No loops needed.)


groupSum5(0, [2, 5, 10, 4], 19) → true
groupSum5(0, [2, 5, 10, 4], 17) → true
groupSum5(0, [2, 5, 10, 4], 12) → false

##############################################################################

5) groupSumClump:
Given an array of ints, is it possible to choose a group of some of the ints,
such that the group sums to the given target, with this additional constraint:
if there are numbers in the array that are adjacent and the identical value,
they must either all be chosen, or none of them chosen. For example, with the
array {1, 2, 2, 2, 5, 2}, either all three 2's in the middle must be chosen
or not, all as a group. (one loop can be used to find the extent of the
identical values).


groupSumClump(0, [2, 4, 8], 10) → true
groupSumClump(0, [1, 2, 4, 8, 1], 14) → true
groupSumClump(0, [2, 4, 4, 8], 14) → false

##############################################################################

6) splitArray:
Given an array of ints, is it possible to divide the ints into two groups,
so that the sums of the two groups are the same. Every int must be in one
group or the other. Write a recursive helper method that takes whatever
arguments you like, and make the initial call to your recursive helper from
splitArray(). (No loops needed.)


splitArray([2, 2]) → true
splitArray([2, 3]) → false
splitArray([5, 2, 3]) → true

##############################################################################

7) splitOdd10:
Given an array of ints, is it possible to divide the ints into two groups, so
that the sum of one group is a multiple of 10, and the sum of the other group
is odd. Every int must be in one group or the other. Write a recursive helper
method that takes whatever arguments you like, and make the initial call to
your recursive helper from splitOdd10(). (No loops needed.)


splitOdd10([5, 5, 5]) → true
splitOdd10([5, 5, 6]) → false
splitOdd10([5, 5, 6, 1]) → true

##############################################################################

8) split53:
Given an array of ints, is it possible to divide the ints into two groups, so
that the sum of the two groups is the same, with these constraints: all the
values that are multiple of 5 must be in one group, and all the values that
are a multiple of 3 (and not a multiple of 5) must be in the other.
(No loops needed.)


split53([1, 1]) → true
split53([1, 1, 1]) → false
split53([2, 4, 2]) → true

"""


def groupSum(start, nums, target):
    # If we have traversed the whole array, there are two possibilities. One
    # is that target is 0 or not. If yes return True, else return False
    if start == len(nums):
        return target == 0

    # For every element, we can either pick an element or not pick it
    picked = groupSum(start+1, nums, target-nums[start])
    notpicked = groupSum(start+1, nums, target)

    # If element is found in either one of the combinations then True.
    return (picked or notpicked)


def groupSum6(start, nums, target):
    if start == len(nums):
        return target == 0

    # Making sure that we always pick when the value is 6
    if nums[start] == 6:
        return groupSum6(start+1, nums, target-nums[start])

    picked = groupSum6(start+1, nums, target-nums[start])
    notpicked = groupSum6(start+1, nums, target)

    return (picked or notpicked)


def groupNoAdj(start, nums, target):
    if start >= len(nums):
        return target == 0

    # Pick only alternate numbers
    picked = groupNoAdj(start+2, nums, target-nums[start])
    notpicked = groupNoAdj(start+1, nums, target)

    return (picked or notpicked)


def groupSum5(start, nums, target):
    if (start >= len(nums)):
        return target == 0

    if nums[start] % 5 == 0:
        if (start < len(nums) - 1) and (nums[start+1] == 1):
            return groupSum5(start+2, nums, target - nums[start])
        else:
            return groupSum5(start+1, nums, target - nums[start])

    # Make sure that there is no fail case by returning True
    if (groupSum5(start+1, nums, target - nums[start])):
        return True
    else:
        return groupSum5(start+1, nums, target)


def groupSumClump(start, nums, target):
    if start >= len(nums):
        return target == 0
    add = nums[start]

    while(start < len(nums)-1 and nums[start] == nums[start+1]):
        add += nums[start+1]
        start += 1

    notpicked = groupSumClump(start+1, nums, target-add)
    picked = groupSumClump(start+1, nums, target)

    return notpicked or picked


def splitArray(nums):
    total = 0

    # Calculate the sum of all numbers
    for num in nums:
        total += num

    # If we cannot split the number in two halves, then return False
    if (total % 2 != 0):
        return False

    return splitArrayHelper(nums, 0, 0, total)


def splitArrayHelper(nums, start, sum_res, total):

    # If half times 2 is total, then return True
    if sum_res*2 == total:
        return True

    # Base case
    if (sum_res > total/2) or (start >= len(nums)):
        return False

    return splitArrayHelper(nums, start+1,
                            sum_res, total) or splitArrayHelper(
        nums, start+1,
        sum_res + nums[start], total)


def splitOdd10(nums):
    start = 0
    sum1 = 0
    sum2 = 0
    return splitOdd10Helper(nums, start, sum1, sum2)


def splitOdd10Helper(nums, start, sum1, sum2):

    # If traversed through the entire array
    if start >= len(nums):
        return (sum1 % 10 == 0 and sum2 % 2 != 0) or (sum2 % 10 == 0 and sum1 % 2 != 0)

    value = nums[start]
    return splitOdd10Helper(nums, start+1, sum1+value, sum2) or splitOdd10Helper(nums, start+1, sum1, sum2+value)


def split53(nums):
    start = 0
    sum5 = 0
    sum3 = 0

    return split53Helper(nums, start, sum5, sum3)


def split53Helper(nums, start, sum5, sum3):
    if start >= len(nums):
        return sum5 == sum3

    value = nums[start]

    if value % 5 == 0:
        return split53Helper(nums, start+1, sum5+value, sum3)

    elif value % 3 == 0:
        return split53Helper(nums, start+1, sum5, sum3+value)

    else:
        return split53Helper(nums, start+1, sum5+value, sum3) or split53Helper(nums, start+1, sum5, sum3+value)


def main():
    print('GroupSum:')
    print(groupSum(0, [2, 4, 8], 10))
    print(groupSum(0, [2, 4, 8], 14))
    print(groupSum(0, [2, 4, 8], 9))
    print('#' * 10)

    print('GroupSum6:')
    print(groupSum6(0, [5, 6, 2], 8))
    print(groupSum6(0, [5, 6, 2], 9))
    print(groupSum6(0, [5, 6, 2], 7))
    print('#' * 10)

    print('GroupNoAdj:')
    print(groupNoAdj(0, [2, 5, 10, 4], 12))
    print(groupNoAdj(0, [2, 5, 10, 4], 14))
    print(groupNoAdj(0, [2, 5, 10, 4], 7))
    print('#' * 10)

    print('groupSum5:')
    print(groupSum5(0, [2, 5, 10, 4], 19))
    print(groupSum5(0, [2, 5, 10, 4], 17))
    print(groupSum5(0, [2, 5, 10, 4], 12))
    print('#' * 10)

    print('groupSumClump:')
    print(groupSumClump(0, [2, 4, 8], 10))
    print(groupSumClump(0, [1, 2, 4, 8, 1], 14))
    print(groupSumClump(0, [2, 4, 4, 8], 14))
    print('#' * 10)

    print('splitArray:')
    print(splitArray([5, 2, 3, 7, 1]))
    print(splitArray([2, 3]))
    print(splitArray([5, 2, 3]))
    print('#' * 10)

    print('splitOdd10:')
    print(splitOdd10([5, 5, 5]))
    print(splitOdd10([5, 5, 6]))
    print(splitOdd10([5, 5, 6, 1]))
    print('#' * 10)

    print('split53:')
    print(split53([1, 1]))
    print(split53([1, 1, 1]))
    print(split53([2, 4, 2]))
    print('#' * 10)


if __name__ == '__main__':
    main()
