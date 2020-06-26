class Solution:
    """
    # @param {integer} rowIndex
    # @return {integer[]}

    Time Complexity: O(n^2) For every iteration of outer loop, inner loop also
    is executed.
    Space Complexity (auxiliary): O(n^2)
        Numbers: 1 + 11 + 121 + 1331 + 14641
        # of digits: 1 + 2 + 3 + 4 + ... + n => n(n+1)/2 => O(n^2)
    """

    def getRow(self, rowIndex):
        result = [1]

        for i in range(1, rowIndex + 1):
            cur = []
            for j in range(1, i):
                cur.append(result[j - 1] + result[j])
            result = [1] + cur + [1]

        return result
