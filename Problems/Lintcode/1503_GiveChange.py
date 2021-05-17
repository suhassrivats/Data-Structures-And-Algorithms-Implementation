class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        coins = [1, 4, 16, 64]
        leftover = 1024 - amount
        num_coins = 0
        for value in reversed(coins):
            num_coins += leftover // value
            leftover = leftover % value
        return num_coins
