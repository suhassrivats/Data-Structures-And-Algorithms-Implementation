class Solution:
    """
    Intuition:
        This problem follows the Sliding Window pattern and is quite similar to
    Longest Substring with K Distinct Characters. In this problem, we need to
    find the length of the longest subarray with no more than two distinct
    characters (or fruit types!). This transforms the current problem into
    Longest Substring with K Distinct Characters where K=2.

    Time Complexity:
        The above algorithm’s time complexity will be O(N), where ‘N’ is the
    number of characters in the input array. The outer for loop runs for all
    characters, and the inner while loop processes each character only once;
    therefore, the time complexity of the algorithm will be O(N+N), which is
    asymptotically equivalent to O(N).

    Space Complexity:
        The algorithm runs in constant space O(1) as there can be a maximum of
    three types of fruits stored in the frequency map.
    """

    def totalFruit(self, tree):
        window_start = 0
        max_length = 0
        fruit_frequency = {}

        # try to extend the range [window_start, window_end]
        for window_end in range(len(tree)):
            right_fruit = tree[window_end]
            fruit_frequency[right_fruit] = fruit_frequency.get(right_fruit, 0) + 1

            # shrink the sliding window, until we are left with '2' tree in the fruit frequency dictionary
            while len(fruit_frequency) > 2:
                left_fruit = tree[window_start]
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]
                window_start += 1  # shrink the window
            max_length = max(max_length, window_end-window_start + 1)

        return max_length
