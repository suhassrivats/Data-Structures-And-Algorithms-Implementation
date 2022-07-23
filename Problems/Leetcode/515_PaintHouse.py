class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    [[17,2,17],[16,10,5],[14,3,19]]

         Color    R     B       G
    ==============================
    House
    0             17    2       17
    1           16+2    10+17   5+2
    2           14+7    3+7     19+18

    Time Complexity:
        Each house can be painted in 3 different colors. There can be 'N' houses.
    Therefore the time complexity is O(3N) => O(N)

    Space Complexity:
        We are only storing one row's computational data in a list of constant
    length (3) per iteration. Therefore, the space complexity is O(1).
    """

    def min_cost(self, costs: List[List[int]]) -> int:
        # costs[i][j] i is house, j is color

        dp = [0, 0, 0]
        for i in range(len(costs)):
            dpR = costs[i][0] + min(dp[1], dp[2])
            dpB = costs[i][1] + min(dp[0], dp[2])
            dpG = costs[i][2] + min(dp[0], dp[1])
            dp = [dpR, dpB, dpG]
        return min(dp)
