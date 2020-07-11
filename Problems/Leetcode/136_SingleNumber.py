class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n⋅1)=O(n). Time complexity of for loop is O(n). Time
        complexity of hash table(dictionary in python) operation pop is O(1).

        Space complexity (auxiliary): O(n). The space required by hash_table is
        equal to the number of elements in nums.
        """

        hashtable = dict()
        for num in nums:
            # If key does not exist in the dictionary, then add `num` as key
            # and its value as num's frequency
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1

        # Check if any key has value as 1
        for num in hashtable:
            if hashtable[num] == 1:
                return num
