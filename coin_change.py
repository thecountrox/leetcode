class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]


# amount = 5
# coins = [1,2,5]
# dp = [1,1,3,3,4,5]
# coin = 2
# x = 2 to 5
# x = 1
# dp[5] += dp[1]
