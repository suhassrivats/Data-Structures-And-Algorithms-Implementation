class Solution:
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
