class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time complexity:
            Since, in each step, the number of subsets doubles as we add each
        element to all the existing subsets, therefore, we will have a total of
        O(2N) subsets, where ‘N’ is the total number of elements in the input
        set. And since we construct a new subset from an existing set,
        therefore, the time complexity of the above algorithm will be O(N*2^N).

        Space complexity:
            All the additional space used by our algorithm is for the output
        list. Since we will have a total of O(2^N) subsets, the space complexity
        of our algorithm is also O(2^N).
        """

        subsets = []
        # start by adding the empty subset
        subsets.append([])

        for current_num in nums:
            for i in range(len(subsets)):
                # create a new subset from the existing subset and insert the
                # current element to it
                new_subset = list(subsets[i])
                new_subset.append(current_num)
                subsets.append(new_subset)

        return subsets
