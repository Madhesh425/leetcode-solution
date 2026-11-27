class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = amount + 1
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if coin <= x and dp[x - coin] + 1 < dp[x]:
                    dp[x] = dp[x - coin] + 1

        return dp[amount] if dp[amount] <= amount else -1