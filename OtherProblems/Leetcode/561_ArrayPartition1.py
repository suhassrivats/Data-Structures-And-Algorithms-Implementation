class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """
        Max sum of pairs can be obtained if we pair two minimum elements
        together. For instance [1,4,3,2] can be paired as min(1,2)+min(3,4)=4.
        Any other combination of pairs will yeild lesser sum.

        Therefore, the algorithm is to sort the input and add alternative
        elements. In this case sorted input will become [1,2,3,4]. We just
        need to add 1 and 3.
        """

        total = 0
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            total += nums[i]
        return total

        # Alternate solution
        # return sum(sorted(nums)[::2])
