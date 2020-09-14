from heapq import *


def find_k_largest_numbers(nums, k):
    min_heap = []
    # TODO: Write your code here
    for i in range(k):
        heappush(min_heap, nums[i])

    for j in range(k, len(nums)):
        if nums[j] > min_heap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
            # heapreplace(min_heap, nums[j])  # alternate method

    return list(min_heap)


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
