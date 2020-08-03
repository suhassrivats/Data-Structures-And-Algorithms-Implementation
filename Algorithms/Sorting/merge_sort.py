# Reference: https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea

class Solution:
    def sortArray(self, nums):
        return self.merge_sort(nums)

    def merge(self, list_left, list_right):
        """
        Merge two sorted lists. This is a linear operation:
            O(len(list_right) + len(list_right))
        :param left_list: list
        :param right_list: list
        :return merged list
        """
        # Special case: one or both of lists are empty
        if len(list_left) == 0:
            return list_right
        elif len(list_right) == 0:
            return list_left

        # General case
        index_left = index_right = 0
        list_merged = []  # list to build and return
        list_len_target = len(list_left) + len(list_right)
        while len(list_merged) < list_len_target:
            if list_left[index_left] <= list_right[index_right]:
                # Value on the left list is smaller (or equal so it should be selected)
                list_merged.append(list_left[index_left])
                index_left += 1
            else:
                # Right value bigger
                list_merged.append(list_right[index_right])
                index_right += 1

            # If we are at the end of one of the lists we can take a shortcut
            if index_right == len(list_right):
                # Reached the end of right. Append the remainder of left and break
                list_merged += list_left[index_left:]
                break
            elif index_left == len(list_left):
                # Reached the end of left. Append the remainder of right and break
                list_merged += list_right[index_right:]
                break

        return list_merged

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            # The following line is the most important piece in this whole thing
            return self.merge(self.merge_sort(left), self.merge_sort(right))
